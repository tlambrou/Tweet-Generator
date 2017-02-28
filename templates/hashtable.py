#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table"""
        # Collect all values in each of the buckets
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        # Count number of key-value entries in each of the buckets
        length = 0
        for bucket in self.buckets:
            for key, value in bucket.items():
                length += 1
        return length

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # Check if the given key exists in a bucket
        # bucket = self.buckets[self._bucket_index(key)]
        # tup = bucket.find(lambda tup: tup[0] == key)
        # if value is not None:
        #     return True
        # return False
        for bucket in self.buckets:
            for hash_key, value in bucket.items():
                if hash_key == key:
                    return True
        return False


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # Check if the given key exists and return its associated value
        bucket = self.buckets[self._bucket_index(key)]
        tup = bucket.find(lambda tup: tup[0] == key)

        if tup is not None:
            return tup[1]
        # while bucket is not None:
        #     if bucket.data[0] == key:
        #         return bucket.data[1]
        #     bucket = bucket.next
        raise KeyError("Key not contained in this hash table")

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # Insert or update the given key-value entry into a bucket
        bucket = self.buckets[self._bucket_index(key)]
        tup = bucket.find(lambda tup: tup[0] == key)
        if tup is not None:
            bucket.delete(tup)
            tup = (key, value)
            bucket.append(tup)
            return
        tup = (key, value)
        bucket.append(tup)

        # while bucket.next is not None:
        #     if bucket.data[0] == key:
        #         bucket.data[1] = value
        #     bucket = bucket.next
        # ll = self.buckets[self._bucket_index(key)]
        # ll.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # Find the given key and delete its entry if found
        bucket = self.buckets[self._bucket_index(key)]
        tup = bucket.find(lambda tup: tup[0] == key)
        if tup is not None:
            bucket.delete(tup)
            return
        # while current is not None:
        #     if current.data[0] == key:
        #         ll.delete(current.data)
        raise KeyError("Key not contained in this hash table")


def test_hash_table():
    ht = HashTable()
    print(ht)

    print('Setting entries:')
    ht.set('I', 1)
    print(ht)
    ht.set('V', 5)
    print(ht)
    ht.set('X', 10)
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('length: ' + str(ht.length()))

    # Enable this after implementing delete:
    # print('Deleting entries:')
    # ht.delete('I')
    # print(ht)
    # ht.delete('V')
    # print(ht)
    # ht.delete('X')
    # print(ht)
    # print('contains(X): ' + str(ht.contains('X')))
    # print('length: ' + str(ht.length()))


if __name__ == '__main__':
    test_hash_table()
