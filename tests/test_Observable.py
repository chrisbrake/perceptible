from mock import Mock
from unittest import TestCase
from perceptible import Observable


class TestObservableDictionary(TestCase):

    def test_init(self):
        """ Confirm we can initialise successfully """
        o = Observable()
        self.assertIsInstance(o, Observable)

    def test_add_observer(self):
        """ Confirm observers are added as expected """
        o = Observable()
        mock_method = Mock()
        o.add_observer(mock_method)
        self.assertSetEqual({mock_method}, o.observers)
        self.assertEqual(1, len(o.observers))

    def test_add_remove_observer(self):
        """ Confirm observers are added and removed expected """
        o = Observable()
        mock_method = Mock()
        o.add_observer(mock_method)
        self.assertSetEqual({mock_method}, o.observers)
        self.assertEqual(1, len(o.observers))
        o.add_observer(mock_method)
        self.assertSetEqual({mock_method}, o.observers)
        self.assertEqual(1, len(o.observers))
        o.remove_observer(mock_method)
        self.assertSetEqual(set(), o.observers)
        self.assertEqual(0, len(o.observers))

    def test_remove_absent_observer(self):
        """ Confirm behavior upon attempt to remove an absent observer """
        o = Observable()
        mock_method = Mock()
        o.add_observer(mock_method)
        with self.assertRaises(KeyError):
            o.remove_observer('not real')
        self.assertSetEqual({mock_method}, o.observers)
        mock_method.assert_not_called()

    def test_notify_observers(self):
        """ Confirm observers are notified as expected"""
        o = Observable()
        mock_method = Mock()
        o.add_observer(mock_method)
        o.notify_observers()
        mock_method.assert_called_once_with(o)
