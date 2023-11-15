import main
import unittest

class testAddingReagentLab(unittest.TestCase):
#testing that herbs go into labatory
    def test_adding_herbs(self):
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



unittest.main()