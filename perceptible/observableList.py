from collections import MutableSequence
from .observable import Observable


class ObservableList(Observable, MutableSequence):
    """
    A class meant to be API compatible with a List, with the addition
    of the add remove and notify observers
    """

    def __init__(self, *args):
        super(ObservableList, self).__init__()
        self._list = list()
        for arg in args:
            self._list += arg

    def insert(self, index, item):
        self._list.insert(index, item)
        self.notify_observers()
        return self

    def __getitem__(self, key):
        return self._list[key]

    def __setitem__(self, index, item):
        self._list.__setitem__(index, item)
        self.notify_observers()
        return self

    def __delitem__(self, item):
        self._list.__delitem__(item)
        self.notify_observers()
        return self

    def __iter__(self):
        return self._list.__iter__()

    def __len__(self):
        return self._list.__len__()

    def __repr__(self):
        return self._list.__repr__()

    def __str__(self):
        return self._list.__str__()
