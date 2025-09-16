import os
from core.node.main import Main as Node
from core.wallet.main import Main as Wallet

class Main:
    print('Welcome to metaco core!')

    print(f"""
    Access option:
    [1] Start the node
    [2] Start mining
    [3] Create a new transactions""")

    selectedOption = int(input('Select : '))

    print('')

    if (selectedOption == 1):
        print('Starting a node...')
        node = Node()
        node.start()
    elif (selectedOption == 2):
        node = Node()
        node.mining()
    elif (selectedOption == 3):
        print('wallet')
    else:
        print('Input is invalid!')