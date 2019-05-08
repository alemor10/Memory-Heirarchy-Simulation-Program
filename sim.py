from dataclasses import dataclass

#helper functions 
def readLine(line):
    opCode = slice(6)
    rs = slice(6,11,1)
    rt = slice(11,16,1)
    offset = slice(16,32,1) 
    offsetValue = int(line[offset],2)
    rsValue = int(line[rs],2)
    byteAddress = computeByteAddress(rsValue,offsetValue) 
    wordAddress = computeWordAddress(byteAddress)
    cacheSet = int (determineCacheSet(wordAddress))
    tag = int(determineTag(wordAddress))
    opCodeInt = int(line[opCode],2)





def computeByteAddress(rs, offset):
    
    byteAddress = rs + offset
    return byteAddress


def computeWordAddress(byteAddress):
    wordAddress = byteAddress / 4
    return wordAddress

def determineCacheSet(wordAddress):
    cacheset = wordAddress % 8
    return cacheset

def determineTag(wordAddress):
    tag = wordAddress / 8 
    return tag


def searchCache(opCode, index):
    if opCode == 35:
        print ("Load")
    elif opCode == 43:
        print("Store")


# data structures
@dataclass
class Block:
    valid : int
    tag: int
    data: int 

cache = [[Block(0,None,None), Block(0,None,None) ]for _ in range(8)]
regFile=[0 for i in range(8)]
mainMemory = [i+5 for i in range(128)]


# this would be similar to the main.cpp in c++
with open ("input.txt", "r") as myfile:
    for line in myfile:
        readLine(line)

