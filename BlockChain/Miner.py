class Miner:
    """Represents a miner that attempts to add a new block to the chain"""
    def __init__(self, chain):
        self.maxNonce = 2 ** 32
        self.chain = chain

    def mine(self, block):
        """Mines a new block"""
        for n in range(self.maxNonce):
            if int(block.generate_hash(), 16) <= self.chain.targetHash:
                self.chain.add(block)
                break
            else:
                block.nonce += 1
