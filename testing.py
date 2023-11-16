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
    def testSuperPotionMixing(self):
        laboratory = main.Laboratory()
        alchemist = main.Alchemist(1.0,1.0,1.0,1.0,1.0,1.0,laboratory)
        herb = main.Herb("Irit",1.0)
        laboratory.addReagent(herb,1)
        catalyst = main.Catalyst("Eye Of Newt",1.0,4.0)
        laboratory.addReagent(catalyst,1)
        alchemist.mixPotion("Super Attack","Attack",herb,catalyst)
        self.assertEqual(laboratory.getPotions(),['Super Attack'])

    def testExtremePotionMixing(self):
        laboratory = main.Laboratory()
        alchemist = main.Alchemist(1.0,1.0,1.0,1.0,1.0,1.0,laboratory)
        herb = main.Herb("Irit",1.0)
        laboratory.addReagent(herb,1)
        catalyst = main.Catalyst("Eye of Newt",4.3,1.0)
        herb2 = main.Herb("Aventoe", 3.0)
        laboratory.addReagent(herb2,1)
        laboratory.addReagent(catalyst,1)
        potion = main.SuperPotion("Super Attack", "Attack",0,herb,catalyst)
        alchemist.mixPotion("Extreme Attack", "Attack",herb2,potion)
        self.assertEqual(laboratory.getPotions(),["Extreme Attack"])
        self.assertEqual(potion.calculateBoost(),7.45)
"""
class testDrinkPotion(unittest.TestCase):
    
    def testSuperPotionDrink(self):
        laboratory = main.Laboratory
        alchemist = main.Alchemist(1.0,1.0,1.0,1.0,1.0,1.0,laboratory)
        herb = main.Herb()
        potion = main.SuperPotion
"""

unittest.main()

