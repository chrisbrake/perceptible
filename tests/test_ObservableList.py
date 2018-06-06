from mock import Mock
from unittest import TestCase
from perceptible import ObservableList


class TestObservableLst(TestCase):

    def test_basic_init(self):
        """ Confirm we can initialise successfully """
        o_list = ObservableList()
        self.assertIsInstance(o_list, ObservableList)

    def test_init(self):
        """ Confirm we can initialise successfully """
        test_data = [i for i in range(10)]
        o_list = ObservableList(test_data)
        self.assertIsInstance(o_list, ObservableList)
        self.assertListEqual(test_data, o_list._list)
        test_data = 'potato'
        o_list = ObservableList(test_data)
        self.assertIsInstance(o_list, ObservableList)
        self.assertListEqual(list(test_data), o_list._list)

    def test_insert_item(self):
        """ Confirm an inserted item is accessible """
        o_list = ObservableList()
        test_data = 'value'
        o_list.insert(0, test_data)
        self.assertListEqual([test_data], o_list._list)
        self.assertEqual(1, len(o_list))
        self.assertEqual('value', o_list.pop())
        self.assertEqual(0, len(o_list))
        self.assertListEqual([], o_list._list)

    def test_append_item(self):
        """ Confirm an inserted item is accessible """
        o_list = ObservableList()
        test_data = 'value'
        o_list.append(test_data)
        self.assertListEqual([test_data], o_list._list)
        self.assertEqual(1, len(o_list))
        self.assertEqual('value', o_list.pop())
        self.assertEqual(0, len(o_list))
        self.assertListEqual([], o_list._list)

    def test_del_absent_item(self):
        """ Confirm behavior when an absent item is deleted """
        mock_method = Mock()
        o_list = ObservableList()
        o_list.add_observer(mock_method)
        with self.assertRaises(IndexError):
            del o_list[0]
        mock_method.assert_not_called()

    def test_del_existing_item(self):
        """ Confirm behavior when an item is deleted """
        mock_method = Mock()
        test_data = [i for i in range(10)]
        o_list = ObservableList()
        o_list += test_data
        self.assertListEqual(test_data, list(o_list))
        o_list.add_observer(mock_method)
        del o_list[7]
        del test_data[7]
        self.assertListEqual(test_data, list(o_list))
        mock_method.assert_called_once_with(o_list)

    def test_repr(self):
        """ Test conversion to a standard dictionary """
        test_data = [i for i in range(10)]
        o_list = ObservableList(test_data)
        self.assertEqual(repr(test_data), repr(o_list))

    def test_str(self):
        """ Test conversion to a standard dictionary """
        test_data = [i for i in range(10)]
        o_list = ObservableList(test_data)
        self.assertEqual(str(test_data), str(o_list))

    def test_iteration(self):
        """ Confirm iteration functions as expected """
        test_data = [i for i in range(10)]
        o_list = ObservableList(test_data)
        for o_item, item in zip(o_list, test_data):
            self.assertEqual(item, o_item)
