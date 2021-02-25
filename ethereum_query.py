from web3 import Web3
from hexbytes import HexBytes

IP_ADDR='18.188.235.196'
PORT='8545'

w3 = Web3(Web3.HTTPProvider('http://' + IP_ADDR + ':' + PORT))

# if w3.isConnected():
#    print( "Connected to Ethereum node" )
# else:
#    print( "Failed to connect to Ethereum node!" )

def getTransaction(tx):
    block = w3.eth.getTransaction(tx) 
    return block

# getGasPrice  takes a transaction and returns the gasPrice.
def getGasPrice(tx):
    block = w3.eth.getTransaction(tx) 
    gasPrice = block.gasPrice
    return gasPrice

# Next, complete the function getGas that takes a transaction and returns the amount of gas used by the transaction.
# Note: The amount of gas used by a transaction is different from the maximum amount of gas that the transaction 
# sender was willing to spend. You will need to use w3.eth.getTransactionReceipt(tx) to obtain the 
# data structure that has the right field.
def getGas(tx):
    block = w3.eth.getTransactionReceipt(tx)
    gas = block.gasUsed
    return gas

# Combine these to complete the function getTransactionCost that 
# calculates the cost (i.e. fees paid) for a given transaction (in Wei).
def getTransactionCost(tx):
    txCost = getGas(tx)* getGasPrice(tx)
    return txCost

# given a block number, returns the total cost of all transactions in that block.
# This is the amount that the miner of the block earns from transaction fees.
# (The miner will additionally earn a reward of a certain number of ether from having mined a new block.)
def getBlockCost(blockNum):
    blockCost = 0
    block = w3.eth.getBlock(blockNum)
    transactions = block.transactions
    for tx in transactions:
      blockCost = getTransactionCost(tx) + blockCost 
    return blockCost

# Return the hash of the most expensive transaction
# '0xf7f4905225c0fde293e2fd3476e97a9c878649dd96eb02c86b86be5b92d826b6'
def getMostExpensiveTransaction(blockNum):
    maxTx = 0
    block = w3.eth.getBlock(blockNum)
    transactions = block.transactions
    for tx in transactions:
      if HexBytes(getTransactionCost(tx)) > HexBytes(maxTx):
          maxTx = tx
    return HexBytes(maxTx)

