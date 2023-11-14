'''
File: main.py
Description: This is the main part of the programming and contains assignment 2 for OOP.
Author: Riley D'Onise
StudentID: 110409464
EmailID: donry019
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from abc import ABC, abstractmethod


class Alchemist:
    def __init__(self, attack,strength,defense,magic,ranged,necromancy,laboratory):
        self.__attack = attack
        self.__strength = strength
        self.__defense = defense
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = laboratory
        self.__recipes = {"Super Attack": "Irit, Eye_of_Newt","Super Strength": "Kwuarm, Limpwurt_Root","Super Defence": "Cadantine,White_Berries","Super Magic":"Lantadyme,Potato_Cactis","Super Ranging":"Dwaft_weed,Wine_Of_Zamorak","Super Necromancy": "Arbuck,Blood_of_Orcus"}

    def getLaboratory(self):
        return self.__laboratory

    def getRecipes(self):
        return self.__recipes

    def mixPotion(self,recipe):
        pass

    def drinkPotion(self,potion):
        pass

    def collectRaegent(self,reagent,amount):
        pass 

    def refineRaegent(self):
        pass

class Laboratory:
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []

    def mixPotion(self,name,stat,primaryIngredient,secondaryIngredient):
        pass

    def addReagent(self, reagent, amount):
        pass


class Potion(ABC):
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat
        self.__boost = boost

    @abstractmethod
    def calculateBoost(self):
        pass

    def getName(self):
        return self.__name

    def getStat(self):
        return self.__stat

    def getBoost(self):
        return self.__boost

    def setBoost(self,boost):
        self._boost = boost


class SuperPotion(Potion):
    def __init__(self, herb, catalyst):
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        pass
    
    def getHerb(self):
        return self.__herb

    def getCatalyst(self):
        return self.__catalyst

class ExtremePotion(Potion):
    def __init__(self,reagent, potion):
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self):
        pass

    def getReagent(self):
        return self.__reagent

    def getPotion(self):
        return self.__potion


class Reagent(ABC):
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        return self.__name

    def getPotency(self):
        return self.__potency

    def setPotency(self, potency):
        self.__potency = potency

class Herb(Reagent):
    def __init__(self):
        self.__grimy = True

    def refine(self):
        self.__potency = self.__potency * 2.5
        self.__grimy = False

    def getGrimy(self):
        return self.__grimy

    def setGrimy(self,grimy):
        self.__grimy = grimy
        

class Catalyst(Reagent):
    def __init__(self, quality):
        self.__quality = quality
    
    def refine(self):
        if self.__quality < 8.9:
            self.__quality = self.__quality * 1.1
            print(f"The quality is now: {self.__quality}")
        else:
            self.__quality = 10
            print(f"The quality is now {self.__quality} and cannot be refined any further")

    def getQuality(self):
        return self.__quality