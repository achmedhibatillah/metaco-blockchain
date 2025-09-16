import os
import json

class MempoolManagement:
    def __init__(self):
        self.MEMPOOL_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "..", "mempool", "mempool.json")
        self.MEMPOOL = []

    def mempool_load(self):
        with open(self.MEMPOOL_FILE, "r") as f:
            self.MEMPOOOL = json.load(f)

    def mempool_load3(self):
        with open(self.MEMPOOL_FILE, "r") as f:
            data = json.load(f)
            self.MEMPOOL = data[:3]
        
    def mempool_save(self):
        with open(self.MEMPOOL_FILE, "w") as f:
            json.dump(self.MEMPOOL,f)

    def mempool_delete(self, txid):
        with open(self.MEMPOOL_FILE, "r") as f:
            data = json.load(f)

        data = [obj for obj in data if obj.get("hs") != txid]

        with open(self.MEMPOOL_FILE, "w") as f:
            json.dump(data, f, indent=4)