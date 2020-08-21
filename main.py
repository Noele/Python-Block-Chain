from src.BlockChain.Chain import Chain
from src.BlockChain.Block import Block
from src.BlockChain.Miner import Miner
import string
import random

chain = Chain()
miner = Miner(chain)


def get_random_string(length):
    """Generates a random string, used to simulate data"""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


for i in range(0, 10000):  # Mine 10000 Blocks
    miner.mine(Block(get_random_string(i), i))
