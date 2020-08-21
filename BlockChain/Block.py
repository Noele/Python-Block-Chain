import datetime
import hashlib

from src.Data.DataIO import DataIO


class Block:
    """Represents a block in the block-chain"""
    def __init__(self, data, id):
        self.id = id
        self.data = data
        self.next = None
        self.hash = None
        self.nonce = 0
        self.previousHash = 0x0
        self.timestamp = datetime.datetime.now()

    def generate_hash(self) -> str:
        """Generates a hash based on the nonce, data, previous hash, timestamp and id"""
        self.hash = hashlib.sha256()
        self.hash.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previousHash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.id).encode('utf-8')
        )
        return self.hash.hexdigest()

    def __str__(self):
        """Calls DataIO to save the latest block to output.json, and returns information to be print to the screen"""
        DataIO.save_latest_block(
            self.hash.hexdigest(),
            self.id,
            self.data,
            self.nonce)
        return f"Block Hash: {self.hash.hexdigest()}\nBlock Number: {self.id}\nBlock Data: {self.data}\nHashes: {self.nonce}\n{'─' * 120}"
