import os
import json
import time

from core.node.controllers.mempool_management import MempoolManagement
from core.node.controllers.block_management import BlockManagement
from core.node.controllers.state_management import StateManagement

class ExecuteMining:
    def __init__(self):
        self.MEMPOOL_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "..", "mempool", "mempool.json")

        self.TARGET = "0001ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"
        self.obj_block_management = BlockManagement()
        self.obj_state_management = BlockManagement()

    def mining(self):
        mempool_management = MempoolManagement()
        mempool = mempool_management.mempool_load()
    
        if mempool == []:
            print(f"\n[!] Mempool is empty.")
            return None

        print("\nMining on proccess...")

        
        blockchain = self.obj_block_management.get_blockchain()
        prev_hash = blockchain[-1]["hash"] if blockchain else "0"*64
        
        block = {
            "ix": len(blockchain) + 1,
            "ph": prev_hash,
            "ts": int(time.time()),
            "nc": 0,
            "tx": []
        }

        print("\nMining on proccess...")

        while True:
            block["nc"] += 1
            hash = self.obj_block_management.block_hash(block)
            if hash < self.TARGET:
                block["hs"] = hash
                self.obj_block_management.block_save(newblock=block)
        
