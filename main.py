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
        self.__recipes = {}

    def getLaboratory(self):
        pass

    def getRecipes(self):
        pass

    def mixPotion(self,recipe):
        pass

    def drinkPotion(self,potion):
        pass

    def collectRaegent(self,reagent,amount):
        pass 

    def refineRaegent(self):
        pass

class Laboratory:
    def __init__(self, potion, herbs, catalysts):
        self.__potions = potion
        self.__herbs = herbs
        self.__catalysts = catalysts

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
        pass

    def getStat(self):
        pass

    def getBoost(self):
        pass

    def setBoost(self,boost):
        pass


class SuperPotion(Potion):
    def __init__(self, herb, catalyst):
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        pass
    
    def getHerb(self):
        pass

    def getCatalyst(self):
        pass

class ExtremePotion(Potion):
    def __init__(self,reagent, potion):
        self.__regeant = reagent
        self.__potion = potion

    def calculateBoost(self):
        pass

    def getReagent(self):
        pass

    def getPotion(self):
        pass


class Reagent(ABC):
    def __init__(self, name, potency):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        pass

    def getPotency(self):
        pass

    def setPotency(self):
        pass
class Herb(Reagent):
    def __init__(self):
        self.__grimy = True

    def refine(self):
        pass

    def getGrimy(self):
        pass

    def setGrimy(self):
        pass

class Catalyst(Reagent):
    def __init__(self, quality):
        self.__quality = quality
    
    def refine(self):
        pass
    
    def getQuality(self):
        pass