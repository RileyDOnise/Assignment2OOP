'''
File: testing.py
Description: This file is being used to test the main.py file. the main methods are tested which includes the mixing of potions,
the drinking of potions, adding reagents to the laboratory and the alchemist being able to collect reagents. this ensures the main file
is always working and reduces the need for manual testinh
Author: Riley D'Onise
StudentID: 110409464
EmailID: donry019
This is my own work as defined by the University's Academic Misconduct Policy.
'''


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
        catalyst = main.Catalyst("Eye of Newt",1.0,4.0)
        laboratory.addReagent(catalyst,1)
        self.assertEqual(laboratory.getCatalysts(),['Eye of Newt'])

class testPotionMixing(unittest.TestCase):
    def testSuperPotionMixing(self):
        laboratory = main.Laboratory()
        alchemist = main.Alchemist(1.0,1.0,1.0,1.0,1.0,1.0,laboratory)
        herb = main.Herb("Irit",1.0)
        laboratory.addReagent(herb,1)
        catalyst = main.Catalyst("Eye of Newt",1.0,4.0)
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
        potion = main.SuperPotion("Super Attack", "Atack",0,herb,catalyst)
        alchemist.mixPotion("Extreme Attack", "Attack",herb2,potion)   
class testDrinkPotion(unittest.TestCase):
    
    def testSuperPotionDrink(self):
        laboratory = main.Laboratory
        alchemist = main.Alchemist(1.0,1.0,1.0,1.0,1.0,1.0,laboratory)
        herb = main.Herb("Irit",1)
        catalyst = main.Catalyst("Eye of Newt",4.3,1)
        potion = main.SuperPotion("Super Attack","Attack",0,herb,catalyst)
        alchemist.drinkPotion(potion)
        self.assertEqual(alchemist.getAttack(),8.45)

    def testExtremePotionDrink(self):
        laboratory = main.Laboratory
        alchemist = main.Alchemist(1.0,1.0,1.0,1.0,1.0,1.0,laboratory)
        herb = main.Herb("Irit",1)
        catalyst = main.Catalyst("Eye of Newt",4.3,1)
        potion = main.SuperPotion("Super Attack","ttack",0,herb,catalyst)
        herb1 = main.Herb("Avantoe",3.0)
        extremePotion = main.ExtremePotion("Extreme Attack","Attack",0,herb1,potion)
        alchemist.drinkPotion(extremePotion)
        self.assertEqual(alchemist.getAttack(),68.05)


class testAddingReagent(unittest.TestCase):
        
        def testCollectingHerb(self):
            laboratory = main.Laboratory()
            alchemist = main.Alchemist(1.0,1.0,1.0,1.0,1.0,1.0,laboratory)
            herb = main.Herb("Irit",1)
            alchemist.collectRaegent(herb,1)
            self.assertEqual(laboratory.getHerbs(),['Irit'])

        def testCollectMultipleCatalyst(self):
            laboratory = main.Laboratory()
            alchemist = main.Alchemist(1.0,1.0,1.0,1.0,1.0,1.0,laboratory)
            catalyst = main.Catalyst("Eye of Newt",4.3,1)
            catalyst2 = main.Catalyst("White Berries",1.2,2.0)
            alchemist.collectRaegent(catalyst,1)
            alchemist.collectRaegent(catalyst2,1)
            self.assertEqual(laboratory.getCatalysts(),["Eye of Newt","White Berries"])

class testRefining(unittest.TestCase):

    def testRefineCatalysts(self):
        laboratory = main.Laboratory()
        alchemist = main.Alchemist(1.0,1.0,1.0,1.0,1.0,1.0,laboratory)
        catalyst = main.Catalyst("Eye of Newt",4.3,1)
        catalyst2 = main.Catalyst("White Berries",1.2,2.0)
        catalyst.refine()
        catalyst2.refine()
        self.assertEqual(catalyst.getQuality(),1.1)
        self.assertEqual(catalyst2.getQuality(),2.2)


unittest.main()



