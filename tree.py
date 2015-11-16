import copy
from random import randint
from random import random

class arbre:
    def __init__(self):
        self.etat = 0

    def symboleAffichage(self):
        if self.etat == 0:
            return "."
        elif self.etat == 1:
            return "A"
        elif self.etat == 2:
            return "F"
        elif self.etat == 3:
            return "C"
        return "."

    def prochainEtat(self, is_next_one_in_fire):
        if self.etat == 0:
            return 0
        elif self.etat == 1:
            if is_next_one_in_fire:
                return 2
            else:
                return 1
        elif self.etat == 2:
            return 3
        elif self.etat == 3:
            return 3
        return 0


class foret:
    def __init__(self, n, m, p):
        self._x = n
        self._y = m
        self._gen = 0
        self._plateau = [[arbre() for l in range(m)] for k in range(n)]
        ''' Initialialise des arbres celon la proportion p '''
        for k in range(n):
            for l in range(m):
                ''' la fonction random permet de respect la consigne d'initalisation des arbres en
                fonction d'une proportionalitée p. Randint ne retourne qu'un entier de proportion 0,5 '''
                if random() < p:
                    self._plateau[k][l].etat = 1
        ''' Affiche la première génération avant le départ du jeu '''
        self._gen = 1
        self.affichage()
        ''' Choisit un arbre à mettre en feu '''
        self._gen = 2
        rX = randint(0, n-1)
        rY = randint(0, m-1)
        while self._plateau[rX][rY].etat != 1:
            rX = randint(0, n-1)
            rY = randint(0, m-1)
        self._plateau[rX][rY].etat = 2

    def __duplication(self, nextPlateau):
        self._gen += 1
        self._plateau = copy.deepcopy(nextPlateau)

    def affichage(self):
        print("Génération", self._gen, ":")
        for k in range(self._x):
            for l in range(self._y):
                print(self._plateau[k][l].symboleAffichage(), end=' ')
            print("", end='\n')
        print("proportion d'arbres", self.proportionActuel())
        if self.hasTheFireGone():
            print("Le feu est éteint")
        else:
            print("Le feu est toujours là")

    def hasNextOneInFire(self, n, m):
        if n-1 < 0:
            north = 0
        else:
            north = self._plateau[n-1][m].etat

        if n+1 >= self._x:
            south = 0
        else:
            south = self._plateau[n+1][m].etat

        if m-1 < 0:
            west = 0
        else:
            west = self._plateau[n][m-1].etat

        if m+1 >= self._y:
            est = 0
        else:
            est = self._plateau[n][m+1].etat

        if north == 2 or south == 2 or west == 2 or est == 2:
            return True
        return False

    def generationSuivante(self):
        plateauNext = copy.deepcopy(self._plateau)
        for k in range(self._x):
            for l in range(self._y):
                plateauNext[k][l].etat = plateauNext[k][l].prochainEtat(self.hasNextOneInFire(k,l))
        self.__duplication(plateauNext)

    def proportionActuel(self):
        p = 0
        q = 0
        for k in range(self._x):
            for l in range(self._y):
                q += 1
                if self._plateau[k][l].etat == 1:
                    p += 1
        return p/q

    def __lt__(self, other):
        return self.proportionActuel() < other.proportionActuel()

    def hasTheFireGone(self):
        for k in range(self._x):
            for l in range(self._y):
                if self._plateau[k][l].etat == 2:
                    return False
        return True

class foretTorique(foret):
    def hasNextOneInFire(self, n, m):
        north = self._plateau[(n-1)%self._x][m%self._y].etat
        south = self._plateau[(n+1)%self._x][m%self._y].etat
        west = self._plateau[n%self._x][(m-1)%self._y].etat
        est = self._plateau[n%self._x][(m+1)%self._y].etat
        if north == 2 or south == 2 or west == 2 or est == 2:
            return True
        return False

f = foretTorique(10, 10, 0.5)
f.affichage()
while input() != "stop":
    f.generationSuivante()
    f.affichage()