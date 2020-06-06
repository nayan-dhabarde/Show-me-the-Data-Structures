import hashlib
import time

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self, data):
        sha = hashlib.sha256()

        hash_str = data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class Blockchain:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_block(self, data):
        if data == "" or data is None:
            return

        if self.head is None:
            self.head = Block(time.time(), data, None)
            self.tail = self.head
        else:
            block = Block(time.time(), data, self.tail.hash)
            self.tail = block

        return self.tail.hash, self.tail.previous_hash


block_chain = Blockchain()

block_hash, previous_hash = block_chain.add_block("test1")    # returns 1b4f0e9851971998e732078544c96b36c3d01cedf7caa332359d6f1d83567014, None
print(str(previous_hash) + " <- " + str(block_hash))
block_hash, previous_hash = block_chain.add_block("test2")    # returns 60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752, 1b4f0e9851971998e732078544c96b36c3d01cedf7caa332359d6f1d83567014
print(str(previous_hash) + " <- " + str(block_hash))
block_hash, previous_hash = block_chain.add_block("test3")    # returns fd61a03af4f77d870fc21e05e7e80678095c92d808cfb3b5c279ee04c74aca13, 60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752
print(str(previous_hash) + " <- " + str(block_hash))

block_chain.add_block("")       # returns nothing
block_chain.add_block(None)     # returns nothing


