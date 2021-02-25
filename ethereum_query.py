from web3 import Web3
from hexbytes import HexBytes

IP_ADDR='18.188.235.196'
PORT='8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

if w3.isConnected():
    print( "Connected to Ethereum node" )
else:
    print( "Failed to connect to Ethereum node!" )

def getTransaction(tx):
    block = w3.eth.getBlock(tx)
    block.number = block.number
    return tx

def getGasPrice(tx):
    block = w3.eth.getBlock(tx)
    gasPrice = block.gasPrice
    print(gasPrice)
    return gasPrice

def getGas(tx):
    gas = 1 #YOUR CODE HERE
    return gas

def getTransactionCost(tx):
    txCost = 1 #YOUR CODE HERE
    return txCost

def getBlockCost(blockNum):
    blockCost = 1  #YOUR CODE HERE
    return blockCost

# Return the hash of the most expensive transaction
def getMostExpensiveTransaction(blockNum):
    maxTx = HexBytes('0xf7f4905225c0fde293e2fd3476e97a9c878649dd96eb02c86b86be5b92d826b6')  #YOUR CODE HERE
    return maxTx




