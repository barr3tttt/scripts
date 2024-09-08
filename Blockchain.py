#!/usr/bin/python3
from hashlib import sha256
import random
import time as t

# GLOBAL VARIABLES
maximumNonce=2**32
currentDifficulty = 3
numberOfBlocks = 5
currentHash = "0"*64        #0000000000000000000000000000000000000000000000000000000000000000
currentNonce = 0


def Sha256(message):
    return sha256(message.encode("ascii")).hexdigest()
           
def createBlock(message,prevHash="0"*64,nonce=0):
    payload = prevHash + message + str(nonce)
    return Sha256(payload)

def mine(message,prevHash, difficulty=3):
    assert difficulty >= 1
    prefix = '0' * difficulty
    for nonce in range(maximumNonce):
        #text = str(message) + str(nonce)
        #newHash = Sha256(text)
        newHash = createBlock(message,prevHash,nonce)
        if newHash.startswith(prefix):
            #print ("Nonce:", nonce)
            #print("Hash value:", newHash)
            return newHash + ":" + str(nonce)
    return "Can't"


if __name__ == "__main__":

    beginTotal = t.time()
    
    for count in range(numberOfBlocks):
        print("Block ",count +1,":")
        msg = "This is the payload, with a random number of As:" + "A"*random.randint(1,25)
        previousHash = currentHash
        currentHash= createBlock(msg,currentHash,currentNonce)
        begin=t.time()
        (minedHash,minedNonce) = mine(msg,previousHash,currentDifficulty).split(":")  #Replace currentHash with Mined Hash
        time_taken=t.time()- begin
        
        print("\tPrevious Hash: " + previousHash + "\n\tMessage: " + msg + "\n\tNonce: ",minedNonce)
        print("\tHash before mining:" + currentHash)
        
        currentHash = minedHash
        print("\nMined Hash: " + currentHash)
        
        print("The mining process took", time_taken, "seconds.\n")
        #print("Replacing current hash with mined hash.\n")
        
        
    endTotal = t.time() - beginTotal
    print("\nThe total block creation process took", endTotal,"seconds\n\n")

    