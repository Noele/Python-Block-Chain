import json
from pathlib import Path

current_path = Path(__file__).parents[0]
data_file = Path(current_path / 'output.json')


class DataIO:
    """Helper class for saving blocks in the block-chain"""
    def __init__(self):
        self.path = data_file
        with data_file.open() as file:
            self.data = json.load(file)

    def save_block(self):
        """Opens and dumps the json data in self.data"""
        with open(self.path, 'w') as fp:
            json.dump(self.data, fp, indent=1)

    def save_latest_block(self, blockHash, blockID, blockData, hashes):
        """Save the latest Blocks info to data.json"""
        block_default_inventory = {"Block ID": blockID, "Block Data": blockData, "Hashes": hashes}
        new_block_inventory = {blockHash: block_default_inventory}
        self.data.update(new_block_inventory)
        self.save_block()


DataIO = DataIO()
