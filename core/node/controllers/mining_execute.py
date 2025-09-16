import os
import json

from core.node.controllers.mempool_management import MempoolManagement

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

        prev_hash = 
        
