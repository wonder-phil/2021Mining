from Block import *

class TestMine():
    def __init__(self, difficulty):
        self.difficulty = difficulty
        b=Block("empty","genesis block")
        newBlock=b.mineBlock(difficulty)
        print("start:"+newBlock.bHash+":end")


tm = TestMine(3);
