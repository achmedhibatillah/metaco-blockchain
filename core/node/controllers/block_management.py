import os
import json
import hashlib

class BlockManagement:

    def __init__(self):
        self.BLOCK_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "data", "blocks")
        self.BLOCKCHAIN

    def block_load(self):
        os.makedirs(self.BLOCK_DIR, exist_ok=True)
        files = sorted(os.listdir(self.BLOCK_DIR))
        blocks = []

        for f in files:
            with open(os.path.join(self.BLOCK_DIR, f), "r") as bf:
                blocks.append(json.loads(bf))

        self.BLOCKCHAIN = blocks
    
    def block_save(self, newblock):
        filename = f"block{len(self.BLOCKCHAIN)+1}.json"
        with open(os.path.join(self.BLOCK_DIR, filename), "w") as f:
            json.dump(newblock, f)
        self.BLOCKCHAIN.append(newblock)

    def block_hash(self, block):
        return hashlib.sha256(json.dumps({k:v for k,v in block.items() if k!="hash"}, sort_keys=True).encode()).hexdigest()