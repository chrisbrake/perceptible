from collections import MutableMapping


class ObservableDictionary(MutableMapping):
    """
    A class meant to be API compatible with a Dictionary, with the addition
    of the add remove and notify observers
    """

    def add_observer(self, observer):
        """
        Add an observer to this data structure, the observer will be called
        whenever this instance of this data structure is modified, with this
        data structure as the only argument.

        :param Method observer:
            The method that should be called when this data structure changes.
        """
        self.observers.add(observer)

    def remove_observer(self, observer):
        """
        Remove an observer from this instance of this data structure.

        :param Method observer:
            The method to remove, so it will no longer be notified
        """
        self.observers.remove(observer)

    def notify_observers(self):
        """
        Call all current observers, and notify them of the current state of
        this instance of this data structure.
        """
        for observer in self.observers:
            observer(self)

    def __init__(self, *args, **kwargs):
        self.observers = set()
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
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)

    def __repr__(self):
        return self._dict.__repr__()

    def __str__(self):
        return self._dict.__str__()
