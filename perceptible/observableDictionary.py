import json
from collections.abc import MutableMapping


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
        :param observer: Method that should be called when this data structure
            changes.
        """
        self.observers.add(observer)

    def remove_observer(self, observer):
        """
        Remove an observer from this instance of this data structure.
        :param observer: The method to remove, so it will no longer be notified
        """
        try:
            self.observers.remove(observer)
        except KeyError:
            pass

    def notify_observers(self):
        """
        Call all current observers, and notify them of the current state of
        this instance of this data structure.
        """
        for observer in self.observers:
            observer(self)

    def as_json(self):
        """
        Converts the data stored in this object to a json string.
        :return: String, JSON compatible
        """
        return json.dumps(self.as_dict())

    def as_dict(self):
        """
        Converts the data stored in this object to a standard dictionary.
        :return: Dictionary
        """
        return self._dict

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
