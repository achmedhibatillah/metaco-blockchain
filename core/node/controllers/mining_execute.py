import os
import json
import time

from core.node.controllers.mempool_management import MempoolManagement
from core.node.controllers.block_management import BlockManagement
from core.node.controllers.state_management import StateManagement
from core.node.controllers.mining_broadcast import MiningBroadcast
from core.node.controllers.mining_difficulty import MiningDifficulty

class ExecuteMining:
    def __init__(self):
        self.MEMPOOL_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "..", "mempool", "mempool.json")

        self.obj_block_management = BlockManagement()
        self.obj_state_management = StateManagement()
        self.obj_mining_broadcast = MiningBroadcast()
        self.obj_mining_difficulty = MiningDifficulty()

    def mining(self):
        mempool_management = MempoolManagement()
        mempool = mempool_management.mempool_load3()
    
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
            target = self.obj_mining_difficulty.get_difficulty()

            if hash < target:
                block["hs"] = hash
                self.obj_block_management.block_save(newblock=block)
                self.obj_state_management.state_update(block=block)

                for tx in mempool:
                    mempool_management.mempool_delete(tx.get("hs"))
                    self.obj_mining_broadcast.broadcasting_node(block=block)
                return block
                    

        
