from mock import Mock
from unittest import TestCase
from observableDictionary.observableDictionary import ObservableDictionary


class TestObservableDictionary(TestCase):

    def test_basic_init(self):
        """ Confirm we can initialise successfully """
        o_dict = ObservableDictionary()
        self.assertIsInstance(o_dict, ObservableDictionary)

    def test_init(self):
        """ Confirm we can initialise successfully """
        test_data = {'key': 'value'}
        o_dict = ObservableDictionary(test_data)
        self.assertIsInstance(o_dict, ObservableDictionary)
        self.assertDictEqual(test_data, dict(o_dict))

    def test_set_get_item(self):
        """ Confirm an inserted item is accessible """
        o_dict = ObservableDictionary()
        o_dict['key'] = 'value'
        self.assertListEqual(['key'], list(o_dict.keys()))
        self.assertListEqual(['value'], list(o_dict.values()))
        self.assertDictEqual({'key': 'value'}, dict(o_dict))
        self.assertEqual(1, len(o_dict))
        self.assertEqual('value', o_dict.get('key'))
        self.assertIsNone(o_dict.get('not real'))

    def test_add_observer(self):
        """ Confirm observers are added as expected """
        o_dict = ObservableDictionary()
        mock_method = Mock()
        o_dict.add_observer(mock_method)
        self.assertSetEqual({mock_method}, o_dict.observers)
        self.assertEqual(1, len(o_dict.observers))

    def test_add_remove_observer(self):
        """ Confirm observers are added and removed expected """
        o_dict = ObservableDictionary()
        mock_method = Mock()
        o_dict.add_observer(mock_method)
        self.assertSetEqual({mock_method}, o_dict.observers)
        self.assertEqual(1, len(o_dict.observers))
        o_dict.add_observer(mock_method)
        self.assertSetEqual({mock_method}, o_dict.observers)
        self.assertEqual(1, len(o_dict.observers))
        o_dict.remove_observer(mock_method)
        self.assertSetEqual(set(), o_dict.observers)
        self.assertEqual(0, len(o_dict.observers))

    def test_notify_observers(self):
        """ Confirm observers are notified as expected"""
        o_dict = ObservableDictionary()
        mock_method = Mock()
        o_dict.add_observer(mock_method)
        o_dict['key'] = 'value'
        mock_method.assert_called_once_with(o_dict)
        o_dict.get('key')
        mock_method.assert_called_once_with(o_dict)

    def test_iteration(self):
        """ Confirm iteration functions as expected """
        test_data = {'key': 'value'}
        o_dict = ObservableDictionary(test_data)
        for key, value in o_dict.items():
            self.assertEqual('key', key)
            self.assertEqual('value', value)

    def test_update(self):
        """ Confirm update functions as expected """
        test_data = {'key': 'value'}
        o_dict = ObservableDictionary({'a': 'b'})
        mock_method = Mock()
        o_dict.add_observer(mock_method)
        o_dict.update(test_data)
        mock_method.assert_called_once_with(o_dict)
        self.assertDictEqual({'key': 'value', 'a': 'b'}, dict(o_dict))

    def test_dict_conversion(self):
        """ Test conversion to a standard dictionary """
        o_dict = ObservableDictionary()
        o_dict['key'] = 'value'
        self.assertDictEqual({"key": "value"}, o_dict.as_dict())

    def test_json_conversion(self):
        """ Test conversion to a JSON string """
        o_dict = ObservableDictionary()
        o_dict['key'] = 'value'
        self.assertEqual('{"key": "value"}', o_dict.as_json())
