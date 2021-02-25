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
    c = HexBytes(tx)
    block = w3.eth.getTransaction(tx) 
    return block

def getGasPrice(tx):
    block = w3.eth.getTransaction(tx) 
    gasPrice = 0
    return gasPrice

  # Next, complete the function getGas that takes a transaction and returns the amount of gas used by the transaction.
  # Note: The amount of gas used by a transaction is different from the maximum amount of gas that the transaction 
  # sender was willing to spend. You will need to use w3.eth.getTransactionReceipt(tx) to obtain the 
  # data structure that has the right field.
def getGas(tx):
    block = w3.eth.getTransactionReceipt(tx)
    gas = block.gasUsed
    print(gas)
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


# '0xa1cb58ac3d7457994feecb5680088d2aa26dc0ac1af54560a2d131925713a820'  

# '0xe58711fc27daecbc3b099c6d5ebb0e92646e784fc30d653f006ee93ba30ffd52' 
#used gas 21000 but your function returned 166666

# '0x8926ced59631388cbb356ecf67d23e5d89a36f93eade2e4163e983545c3fc5b9' 
#used gas 21000 but your function returned 23100

tx = '0xf1be309c46a7c982a02b44e894f1a80b5d4e7c8d9bb240d03046eaa5f705854e'
# 1000000000 but your function returned 50000

block = w3.eth.getTransaction(tx) 
print(block.blockNumber)
getGasPrice(tx)
print(block.gas)
