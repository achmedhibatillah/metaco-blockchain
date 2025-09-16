import os
import json
from datetime import datetime

class TxListMempool:
    def __init__(self):
        self.MEMPOOL_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "..", "mempool", "mempool.json")

    def index(self):
        with open(self.MEMPOOL_FILE, "r") as f:
            tx_mempool = json.load(f)

        count_tx = len(tx_mempool)
        print(f"\nTransaction List ({count_tx})")
        print(f"{datetime.now()}\n")
        
        i = 1
        for x in tx_mempool:
            print(f"[{i}] => {x["amount"]}")
            print(f"I : {x["from"]}")
            print(f"O : {x["to"]}\n")
            i += 1