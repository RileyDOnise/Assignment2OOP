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
        self.__recipes = {"Super Attack":["Irit","Eye of Newt"],
    "Super Strength": ["Kwuarm","Limpwurt Root"],
    "Super Defence": ["Cadantine", "White Berries"],
    "Super Magic":["Lantadyme","Potato Cactus"],
    "Super Ranging":["Dwaft weed","Wine Of Zamorak"],
    "Super Necromancy": ["Arbuck","Blood Of Orcus"],
    "Extreme Attack":["Avanoe","Super Attack"],
    "Extreme Strength":["Dwarf Weed","Super Strength"],
    "Extreme Defence": ["Lantadyme","Super Defence"],
    "Extreme Magic": ["Ground Mud Rune","Super Magic"],
    "Extreme Ranging": ["Grenwall Spike", "Super Ranging"],
    "Extreme Necromancy": ["Ground Miasma Rune","Super Necormancy"]}

    def getLaboratory(self):
        return self.__laboratory

    def getRecipes(self):
        return self.__recipes

    def mixPotion(self,recipe,stat,primaryIngredient,secondaryIngredient):
        for i in self.__recipes:
            if i == recipe:
                #if primaryIngredient.getName() in self.__recipes[i] and secondaryIngredient.getName() in self.__recipes[i]: 
                self.__laboratory.mixPotion(recipe,stat,primaryIngredient,secondaryIngredient)

    def drinkPotion(self,potion):
        stat = potion.getStat()
        boost = potion.calculateBoost()
        if stat == "Attack":
            self.__attack = self.__attack + boost
        elif stat == "Strength":
            self.__strength = self.__strength + boost
        elif stat == "Defense":
            self.__defense = self.__defense + boost
        elif stat == "Magic":
            self.__magic = self.__magic + boost
        elif stat == "Ranged":
            self.__ranged = self.__ranged + boost
        elif stat == "Necormancy":
            self.__necromancy = self.__necromancy + boost
        else:
            #raise exception here
            pass

    #method is used for testing
    def getAttack(self):
        return self.__attack

    def collectRaegent(self,reagent,amount):
        pass

    def refineRaegent(self):
        pass

class Laboratory:
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []
        #Key: name, Value: potency
        self.__herbStats = {"Arbuck": 2.6, "Avantoe": 3.0,"Cadantine":1.5,"Dwarf Weed": 2.5,"Irit":1.0,"Kwuarm": 1.2,"Lantadyme": 2.0,"Torstol": 4.5}
        #Key: name list[0]: potency, list[1]: quality
        self.__catalystsNames = {"Eye Of Newt": [4.3,1.0], "Limpwurt Root": [3.6,1.7],
                                "White Berries": [1.2,2.0],"Potato Cactus": [7.3,0.1],
                                "Wine Of Zamorak": [1.7, 5.0],"Blood Of Orcus": [4.5,2.2],
                                "Ground Mud Rune": [2.1,6.7],"Grenwall Spike":[6.3,4.9], 
                                "Ground Miasma Rune": [3.3,5.2]}

    def mixPotion(self,name,stat,primaryIngredient,secondaryIngredient):
        if primaryIngredient in self.__herbs or primaryIngredient in self.__catalysts:
            
            if secondaryIngredient in self.__catalysts:
                newPotion = SuperPotion(name,stat,0,primaryIngredient,secondaryIngredient)
                self.__potions.append(newPotion)
                tempBoost = self.__potions[len(self.__potions)-1].calculateBoost()
                self.__potions[len(self.__potions)-1].setBoost(tempBoost)
                
                if primaryIngredient in self.__herbs:
                    self.__herbs.remove(primaryIngredient)
                else:
                    self.__catalysts.remove(primaryIngredient)
                if secondaryIngredient in self.__herbs:
                    self.__herbs.remove(secondaryIngredient)
                else:
                    self.__catalysts.remove(secondaryIngredient)
                return newPotion

        else:
            newPotion = ExtremePotion(name,stat,0,primaryIngredient,secondaryIngredient)
            self.__potions.append(newPotion)
            tempBoost = self.__potions[len(self.__potions)-1].calculateBoost()
            self.__potions[len(self.__potions)-1].setBoost(tempBoost)
            return newPotion

#adds the reagent to the apporiate list
    def addReagent(self, reagent, amount):
        if reagent.getName() in self.__herbStats:
            for i in range(amount):
                self.__herbs.append(reagent)
                
        elif reagent.getName() in self.__catalystsNames:
            for i in range(amount):
                self.__catalysts.append(reagent)

#returns all the objects in __herbs list
    def getHerbs(self):
        return ([x.getName() for x in self.__herbs])
    
#returns all the objects in __catalysts list
    def getCatalysts(self):
        return ([x.getName() for x in self.__catalysts])
        
#returns all objects in the __potions list
    def getPotions(self):
        return([x.getName() for x in self.__potions])

class Potion(ABC):
    def __init__(self, name, stat, boost):
        self.__name = name
        self.__stat = stat
        self.__boost = boost

    @abstractmethod
    def calculateBoost(self):
        pass

#returns name of the potion
    def getName(self):
        return self.__name

#returns stat of the potion
    def getStat(self):
        return self.__stat

#returns the boost of the potion
    def getBoost(self):
        return self.__boost

#sets the boost of the potion
    def setBoost(self,boost):
        self.__boost = boost

class SuperPotion(Potion):
    def __init__(self,name,stat,boost,herb, catalyst):
        super().__init__(name,stat,boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        return round((self.__herb.getPotency() + (self.__catalyst.getPotency()* self.__catalyst.getQuality() * 1.5)) ,2)
    
    def getHerb(self):
        return self.__herb

    def getCatalyst(self):
        return self.__catalyst

    def getBoost(self):
        return self._Potion__boost

class ExtremePotion(Potion):
    def __init__(self,name,stat,boost,reagent, potion):
        super().__init__(name,stat,boost)
        self.__reagent = reagent
        self.__potion = potion

    def calculateBoost(self):
                        #3.0                        7.45
        return round((self.__reagent.getPotency() * self.__potion.calculateBoost())*3, 2)

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
    def __init__(self,name,potency):
        super().__init__(name,potency)
        self.__grimy = True

    def refine(self):
        self.__potency = self.__potency * 2.5
        self.__grimy = False

    def getGrimy(self):
        return self.__grimy

    def setGrimy(self,grimy):
        self.__grimy = grimy
        

class Catalyst(Reagent):
    def __init__(self,name,potency, quality):
        super().__init__(name,potency)
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

