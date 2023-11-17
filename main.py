'''
File: main.py
Description: A part of a greater application in which is about Alchemists, laboratories and potion. alehcmistist have many functions such as
mixing potions,drinking potions, foraging reagents and refining regeants. alchemist also have stats which can be boost by drinking potions. The potions
are created in a laboratory by a alchemist. in the laboratory the correct ingredients are identified and the potion creation methods are called.
Author: Riley D'Onise
StudentID: 110409464
EmailID: donry019
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from abc import ABC, abstractmethod


class Alchemist:
    """
A class that represents a Alchemist

Attributes
----------------
attack: int
    assigned at declaration is the attack stat of the alchemist
strength: int
    assigned at declaration is the strength stat of the alchemist
defense: int
    assigned at declartion is the defense stat of the alchemist
magic: int
    assigned at declaration is the magic stat of the alchemist
ranged: int
    assigned at delcartion is the range stat of the alchemsit
necormancy: int
    assigned at declartion is the necromany stat of the alchemist
laboratory: Laboratory
    is the laboratory which the alchemist is associated with.

Methods
---------------
getLaboratory(self)
    returns the laboratory which was assigned to alchemist at declaration of the alchemist class

getRecipes(self)
    returns a list of the potion recipes avaliable with the key being the name and the value being the ingredients

mixPotion(self,recipe,stat,primaryIngredient,secondaryIngredient)
    makes sure that the recipe exsists and calls the mix potion function from Laboratory Class

getAttack(self)
    returns the attack stat(used in the testing)

drinkPotion(self, potion)
    alchemist drinks potion and adjusts the stats of the alchemist accordingly

collectReagent(self, reagent,amount)
    uses the addReagent function from laboratory to assign them to the correct list

refineReagent(self)
    calls the refine function from the Potion classes which increase the potency or quality depending on type of potion
"""

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

    #method is used for testing
    def getAttack(self):
        return self.__attack

    def collectRaegent(self,reagent,amount):
        self.__laboratory.addReagent(reagent,amount)

    def refineRaegent(self):
        for i in self.__laboratory.getHerbs():
            i.refine()
        for i in self.__laboratory.getCatalysts():
            i.refine()

class Laboratory:

    """
    A class which represents a laboratory

    Attributes
    potions: list
        intially empty is used to store the potions which have been created using collectReagent from alchemist
    herbs: list
        intially empty is used to store the herbs which have been collected using collectReagent from alchemist
    catalysts
        intially empty is used to store the catalysts which have been collected using collectReagent from alchemist
    
    Methods

    mixPotion(self,name,stat,primaryIngredient,secondaryIngredient)
        is called, checks if the ingredients have been collect and appened to the apportiate list, creates a instance of the apporiate type of potion and appends it to the apporiate list
    
    addReagent(self,reagent,amount)
        adds a reagent object to the apporiate list (herbs/catalysts)
    
    getHerbs(self)
        returns the herbs list

    getCatalysts(self)
        returns the catalysts list

    getPotions(self)
        returns the potions list

    """
    statNames = ["Attack","Strength","Defense","Magic","Ranged","Necormancy"]
    def __init__(self):
        self.__potions = []
        self.__herbs = []
        self.__catalysts = []
        #Key: name, Value: potency
        self.__herbStats = {"Arbuck": 2.6, "Avantoe": 3.0,"Cadantine":1.5,"Dwarf Weed": 2.5,"Irit":1.0,"Kwuarm": 1.2,"Lantadyme": 2.0,"Torstol": 4.5}
        #Key: name list[0]: potency, list[1]: quality
        self.__catalystsNames = {"Eye of Newt": [4.3,1.0], "Limpwurt Root": [3.6,1.7],
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

            elif secondaryIngredient in self.__potions:
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
    """
    Potion is a abstract class which the base for creating potions

    attributes
    ------------
    name: str
        the name of the potion
    stat: str
        the stat which the potion increases
    boost: float
        the amount which the stat is boosted by

    methods
    -----------
    calculateBoost(self)
        is a abstract class that is used in the superPotion and extremePotion classes ensures that a calculate boost method is defined
    
    getName(self)
        returns the name of the potion
    
    getStat(self)
        returns the stat which the potion boosts

    getBoost
        returns the amount the stat will be boosted by    
    """

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
    """
    Is a child class of Potion and Inherits the name, stat and boost attributes.

    Attributes
    -------------
    name: str
        name of the potion
    stat: str
        the stat which will be boosted by the potion
    boost: float
        how much the stat will be boosted by
    herb: Herb
        the herb which is used to create the potion
    catalyst: Catalyst
        the catalyst which is used to create the potion
    Methods
    ----------
    calculateBoost(self)
        calculates the amount a stat will be boosted using the potency of the catalyst and herb and the quality of the catalysts
    
    getHerb
        returns the herb which has been used in the potion
    
    getCatalyst(self)
        returns the catalyst which has been used in the potion

    getBoost(self)
        returns the boost value which was calculated using calculateBoost method
    
    """

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
    """
    Is a child class of Potion and Inherits the name, stat and boost attributes.

    Attributes
    -------------
    name: str
        name of the potion
    stat: str
        the stat which will be boosted by the potion
    boost: float
        how much the stat will be boosted by
    reagent: Reagent
        the Reagent which is used to create the potion
    potion: Potion
        the potion which is used to create the potion

    Methods
    ----------
    calculateBoost(self)
        using the reagentPotency and the potion boost calculates the boost of the extreme potion
        
    getReagent(self)
        returns the Reagent which is used in the potion

    getPotion(self)
        returns the potion whcih is used in the potion
        """

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

    """
    is the abstract class which is used when creating herbs and catalysts

    attributes
    ----------
    name: str
        the name of the reagent
    potency: float
        the strenght of the reagent used in calculating the boost of potions
    
    Methods
    ---------
    refine(self)
        abstract method which is used to refine the reagents in herb and catalysts classes
    
    getName(self)
        returns the name of the reagent
    
    getPotency(self)
        returns the potency of the reagent
    
    setPotency(self, potency)
        sets the potency value to a value which is specified by the user
    
    """
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

    """
    is the abstract class which is used when creating herbs and catalysts

    attributes
    ----------
    name: str
        the name of the reagent
    potency: float
        the strenght of the reagent used in calculating the boost of potions
    
    Methods
    ---------
    refine(self)
        calculates the refined  potency of the herb using the previous potency value    

    getGrimy(self)
        returns the grimy value
    
    setGrimy(self,grimy)
        sets the grimy value to the grimy value provided by the user
        
    """
    
    def __init__(self,name,potency):
        super().__init__(name,potency)
        self.__grimy = True

    def refine(self):
        self.setPotency(self.__potency * 2.5)
        self.setGrimy(False)

    def getGrimy(self):
        return self.__grimy

    def setGrimy(self,grimy):
        self.__grimy = grimy
        

class Catalyst(Reagent):
    
    """
    is the abstract class which is used when creating herbs and catalysts

    attributes
    ----------
    name: str
        the name of the catalyst
    potency: float
        the strenght of the catalyst used in calculating the boost of potions
    quality: float
        the quality of catalyst used to calculate boosts and potion values
        
    Methods
    ---------
    refine(self)
        uses the quality of catalyst to calculate the regined quality

    getQuality(self)
        returns the quality value of the catalyst and used to calcualate boost values
        """

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
