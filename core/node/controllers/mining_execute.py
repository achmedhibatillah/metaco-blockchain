import os
import json
import time

from core.node.controllers.mempool_management import MempoolManagement
from core.node.controllers.block_management import BlockManagement

class ExecuteMining:
    def __init__(self):
        self.MEMPOOL_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "data", "mempool", "mempool.json")

    def mining(self):
        mempool_management = MempoolManagement()
        mempool = mempool_management.mempool_load()
    
        if mempool == []:
            print(f"\n[!] Mempool is empty.")
            return None

        print("\nMining on proccess...")

        block_management = BlockManagement()
        blockchain = block_management.get_blockchain()
        prev_hash = blockchain[-1]["hash"] if blockchain else "0"*64
        
        block = {
            "index": len(blockchain) + 1,
            "prev_hash": prev_hash,
            "timestamp": int(time.time())
        }
        
