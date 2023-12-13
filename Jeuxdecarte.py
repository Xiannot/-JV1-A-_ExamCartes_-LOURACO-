class Personnage:
    def __init__(self,nom,pv,mana):
        self.__nom__ = nom
        self.__pv__ = pv
        self.__mana__ = mana

    def affiche(self):
        print(f"{self.__nom__} a {self.__pv__} pv et sont mana est de {self.__mana__}")

    def combat1(self):
        choix = int(input("Quelle carte choisie tu ?"))

        if choix == 1:
            print("Tu a choisie cristal tu augmente donc ton mana a 40!")
            self.__mana__ += 10


        if choix == 2:
            print("Tu a poser un dragon sur ton board")
            self.__mana__ -= 10
            dragon = 1
            attaque = int(input("Qui decide tu d'attaquer 1/ Le joueur 2/ Sa Creature"))
            if attaque == 1:
                print("Tu viens d'attaquer le joueur il perd donc 25 pv")
                mage2.__pv__ -=25
            if attaque == 2:
                print("Tu viens d'attaquer sa creature elle perd 25 Pv ")
                creature.__pv__ -=25
                


        if choix == 3:
            print("Tu envoie une boule de feu a ton ennemi il perd 10 pv!")
            mage2.__pv__ -= 10 

    def combat2(self):
        choix = int(input("Quelle carte choisie tu ?"))

        if choix == 1:
            print("Tu a choisie cristal tu augmente donc ton mana a 40!")
            self.__mana__ += 10


        if choix == 2:
            print("Tu a poser un dragon sur ton board")
            self.__mana__ -= 10
            dragon = 1
            attaque = int(input("Qui decide tu d'attaquer 1/ Le joueur 2/ Sa Creature"))
            if attaque == 1:
                print("Tu viens d'attaquer le joueur il perd donc 25 pv")
                mage1.__pv__ -=25
            if attaque == 2:
                print("Tu viens d'attaquer sa creature elle perd 25 Pv ")
                creature.__pv__ -=25        

    def mort(self):
        if mage1.__pv__ ==0:
            ("T'es point de vie sont a 0 tu a perdu.")
            vie = 0
        if mage2.__pv__ ==0:
            ("T'es point de vie sont a 0 tu a perdu.")
            vie = 0

class Carte(Personnage):
    def __init__(self,nom,cout,degat,mana,pv):
        self.__nom__ = nom
        self.__cout__ = cout
        self.__degat__ = degat
        self.__mana__ = mana
        self.__pv__= pv

    def affiche_cristal(self):
        print(f"Carte:")
        print(f"1/{self.__nom__}: coute {self.__cout__} mana et donne {self.__mana__} mana au joueur")

    def affiche_creature(self):
        print(f"2/{self.__nom__}: coute {self.__cout__} mana et fait {self.__degat__} dégat au joueur et sont nombre de pv est de {self.__pv__}")  

    def affiche_blast(self):
        print(f"3/{self.__nom__}: coute {self.__cout__} mana et fait {self.__degat__} dégat au joueur")
        
      
mage1 = Personnage("Bastien",100,30)
mage2 = Personnage("Marwann",100,30)

cristaux = Carte("Cristaux",0,0,10,0)
creature = Carte("Creature",10,25,0,50)
blast = Carte("Blast",10,10,0,0)


vie =1
while vie == 1:
    
    mage1.affiche()
    mage2.affiche()
    cristaux.affiche_cristal()
    creature.affiche_creature()
    blast.affiche_blast()
    mage1.combat1()

    mage1.affiche()
    mage2.affiche()
    cristaux.affiche_cristal()
    creature.affiche_creature()
    blast.affiche_blast()
    mage2.combat2()














