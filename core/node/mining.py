import os
import json
from core.node.controllers.mining_txlist import TxListMempool
from core.node.controllers.mining_execute import ExecuteMining

class Mining:
    def __init__(self):
        self.MEMPOOL_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "mempool", "mempool.json")

    def index(self):
        with open(self.MEMPOOL_FILE, "r") as f:
            tx_count_mempool = len(json.load(f))

        print("===== Mining Configuration =====")
        print("Tx in mempool : ", tx_count_mempool)
        print("\nSelect option :")
        print("[1] Transaction list")
        print("[2] Start mining")

        selectedOption = int(input("Select : "))

        if selectedOption == 1:
            tx_list_mempool = TxListMempool()
            tx_list_mempool.index()
        elif selectedOption == 2:
            exe_mining = ExecuteMining()
            exe_mining.mining()
            
        else:
            print("Invalid selection.\n")