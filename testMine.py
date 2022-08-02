from Block import *

class TestMine():
    def __init__(self, previousHash, data, difficulty):
        self.difficulty = difficulty
        b=Block(previousHash,data)
        newBlock=b.mineBlock(difficulty)
        print("start:"+newBlock.bHash+":end")


tm = TestMine(3);
