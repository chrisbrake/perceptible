class Observable(object):
    """
    A class meant to be API compatible with a Dictionary, with the addition
    of the add remove and notify observers
    """

    def __init__(self):
        super(Observable, self).__init__()
        self.observers = set()

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
