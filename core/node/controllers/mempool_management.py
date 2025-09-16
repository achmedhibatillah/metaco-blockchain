import os
import json

class MempoolManagement:
    def __init__(self):
        self.MEMPOOL_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "data", "mempool", "mempool.json")
        self.MEMPOOL = []

    def mempool_load(self):
        with open(self.MEMPOOL_FILE, "r") as f:
            self.MEMPOOOL = json.load(f)
        
    def mempool_save(self):
        with open(self.MEMPOOL_FILE, "w") as f:
            json.dump(self.MEMPOOL,f)