from web3 import Web3

eth = "http://127.0.0.1:8545"
w3 = Web3(Web3.HTTPProvider(eth))
print("This is the connection status: " + str(w3.isConnected()))

def get_latest_block():
    latest_block = w3.eth.get_block('latest')
    print("This is the latest block: ")
    print(latest_block)

    print("This is the latest block: ")
    for i,j in latest_block.items():
        print(i,j)

    print('This is the genesis block timestamp: ' + str(latest_block['timestamp']))

    print("THis is the block number: " + str(w3.eth.block_number))

get_latest_block()
