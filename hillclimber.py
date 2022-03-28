from solution import SOLUTION
import constants
import os
import copy

class HILLCLIMBER:

    def __init__(self):
        self.parent = SOLUTION()

    def Evolve(self):
        directOrGUI = "DIRECT"
        self.parent.Evaluate(directOrGUI)

        for currentGeneration in  range(constants.numberOfGenerations):
            self.Evolve_For_One_Generation()

        # for currentGeneration in  range(1):
        #     self.Evolve_For_One_Generation()





    def Evolve_For_One_Generation(self):
        self.Spawn()

        self.Mutate()

        directOrGUI = "DIRECT"

        self.child.Evaluate(directOrGUI)

        self.Print()

        self.Select()




    def Spawn(self):
        self.child =  copy.deepcopy(self.parent)


    def Mutate(self):
        self.child.Mutate()




    def Select(self):
        if self.child.fitness > self.parent.fitness:
            self.parent = self.child


    def Print(self):
        print(self.parent.fitness,self.child.fitness)



    def Show_Best(self):
        os.system("python3 simulate.py GUI")