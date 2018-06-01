from collections import MutableMapping
from .observable import Observable


class ObservableDictionary(Observable, MutableMapping):
    """
    A class meant to be API compatible with a Dictionary, with the addition
    of the add remove and notify observers
    """

    def __init__(self, *args, **kwargs):
        super(ObservableDictionary, self).__init__()
        self._dict = dict()
        self._dict.update(*args, **kwargs)

    def __getitem__(self, key):
        return self._dict[key]

    def __setitem__(self, key, value):
        self._dict[key] = value
        self.notify_observers()

    def __delitem__(self, key):
        del self._dict[key]
        self.notify_observers()

    def __iter__(self):
        return self._dict.__iter__()

    def __len__(self):
        return self._dict.__len__()

    def __repr__(self):
        return self._dict.__repr__()

    def __str__(self):
        return self._dict.__str__()
