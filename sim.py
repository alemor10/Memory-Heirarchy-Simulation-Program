from dataclasses import dataclass

# data structures
@dataclass
class Block:
    valid : int
    tag: int
    data: int 
    history: bool

cache = [[Block(0,None,None, True), Block(0,None,None, False) ]for _ in range(8)]
regFile=[0 for i in range(8)]
mainMemory = [i+5 for i in range(128)]

#helper functions 
def readLine(line):
    opCode = slice(6)
    rs = slice(6,11,1)
    rt = slice(11,16,1)
    offset = slice(16,32,1) 
    offsetValue = int(line[offset],2)
    rsValue = int(line[rs],2)
    rtValue = int(line[rt],2)
    byteAddress = int (computeByteAddress(rsValue,offsetValue)) 
    wordAddress = int(computeWordAddress(byteAddress))
    cacheSet = int (determineCacheSet(wordAddress))
    tag = int(determineTag(wordAddress))
    opCodeInt = int(line[opCode],2)
    searchCache(opCodeInt, cacheSet, tag, rtValue,wordAddress)
    




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


def calculateMemoryAddress(index, tag):
    memoryAddress = tag * 8 + index
    return memoryAddress

def searchCache(opCode, index, tag, rtValue, wordAddress):
    if opCode == 35:
        if cache[index][0].valid == 1 or cache[index][1].valid == 1:
            if cache[index][0].tag == tag:
                handleLoadHit(index,rtValue, 0)
            elif cache[index][1].tag == tag:
                handleLoadHit(index,rtValue,1)
        else:
            handleLoadMiss(index,tag)
    elif opCode == 43:
        if cache[index][0].valid == 1 or cache[index][1].valid == 1:
            if cache[index][0].tag == tag:
                handleStoreHit(rtValue, index,0)
            elif cache[index][1].tag == tag:
                handleStoreHit(rtValue, index, 1)
        else:
            handleStoreMiss(rtValue,wordAddress)


def handleLoadMiss(index, tag):
     if cache[index][0].history == True and cache[index][1].history == False:
     elif cache[index][0].history == True and cache[index][1].history == False:
         print("here3")

def handleLoadHit(index,rtValue, victimBlock):
    regFile[rtValue-16] = cache[index][victimBlock].data


def handleStoreHit(rtValue, index, victimBlock): 
    cache[index][victimBlock].data = regFile[rtValue-16]

def handleStoreMiss(rtValue, wordAddress):
    mainMemory[wordAddress] = regFile[rtValue-16]


# this would be similar to the main.cpp in c++
with open ("input.txt", "r") as myfile:
    for line in myfile:
        readLine(line)

