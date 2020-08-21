from src.BlockChain.Block import Block


class Chain:
    """Represents the block-chain"""
    def __init__(self):
        self.block = Block("Genesis", 0)
        self.difficulty = 20
        self.targetHash = 2 ** (256 - self.difficulty)

    def add(self, block):
        """Adds a block to the chain"""
        if int(block.generate_hash(), 16) <= self.targetHash:
            print(block)
            block.previousHash = self.block.generate_hash()
            self.block.next = block
            self.block = self.block.next
