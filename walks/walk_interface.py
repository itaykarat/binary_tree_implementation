from abc import ABC, abstractmethod


class walk_interface(ABC):
    # Note that each walk methods takes O(n) time because we iterate over all elements in the DS.
    @abstractmethod
    def walk(self):
        pass
