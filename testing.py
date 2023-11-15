import main
import unittest

class testAddingReagentLab(unittest.TestCase):
#testing that herbs go into labatory
    def testAddingHerbs(self):
        laboratory = main.Laboratory()
        herb = main.Herb("Irit",1.0)
        laboratory.addReagent(herb,1)
        self.assertEqual(laboratory.getHerbs(),['Irit'])

#testing that catalysts go into the laboratory
    def testAddingCatalysts(self):
        laboratory = main.Laboratory()
        catalyst = main.Catalyst("Eye Of Newt",1.0,4.0)
        laboratory.addReagent(catalyst,1)
        self.assertEqual(laboratory.getCatalysts(),['Eye Of Newt'])



class testPotionMixing(unittest.TestCase):
    
    def testPotionMixing(self):
        laboratory = main.Laboratory
        alchemist = main.Alchemist(1.0,1.0,1.0,1.0,1.0,1.0,laboratory)
        herb1 = main.Herb("Irit",1)
        catalyst1 = main.Catalyst("Eye Of Newt",4.3,1)
        laboratory.addReagent(self,herb1,1)
        laboratory.addReagent(self,catalyst1, 1)
        alchemist.mixPotion("Super Attack","Attack",herb1,catalyst1)
        self.assertEqual(laboratory.getPotions(),['Super Attack'])

unittest.main()

