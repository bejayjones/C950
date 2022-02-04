# HashTable class using chaining.
class DirectHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=41):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append("")

    # Inserts a new item into the hash table.
    def insert(self, key, item):
        # insert the item to the end of the bucket list.
        self.table[key] = item

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # search for the key in the bucket list
        if self.table[key] is not None:
            return self.table[key]
        else:
            # the key is not found.
            return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # remove the item from the bucket list if it is present.
        if key in self.table[key]:
            self.table.remove(key)
