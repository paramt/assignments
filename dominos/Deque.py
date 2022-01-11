import re


class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.insert(0, item)

    def remove_front(self):
        return self.items.pop(0)

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def get(self, index):
        return self.items[index]

    def pprint(self):
        return "  ".join(self.items)
