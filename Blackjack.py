'''
* Black Jack Game
* Completed by Brahim Kanouche , university of Ottawa
'''
from random import shuffle

class Blackjack:
 valeurs={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}

 def joue(self):
  '''jour un jeu'''
  k = JeuDeCartes()
  k.battre()

  banque = Main('Banque')
  joueur = Main('Joueur')

  # donne deux cartes chacun (banque et joueur)
  for i in range(2):
    joueur.ajouteCarte(k.tireCarte())
    banque.ajouteCarte(k.tireCarte())

  # affiche les cartes donnes
  banque.montreMain()
  joueur.montreMain()

  # tirage de carte par la banque tant que le joueur demande des cartes.
  reponse = input('Carte? Oui ou non? (Par défaut oui) ')
  while reponse in ['','o','O','oui','Oui']:
    L = k.tireCarte()
    print("Vous avez:")
    print(L)
    joueur.ajouteCarte(L)
    if self.total(joueur) > 21:
       print("Vous avez dépassé 21. Vous avez perdu.")
       return
    reponse = input('Carte? Oui ou non? (Par défaut oui) ')

  # la banque joue avec ses regles
  while self.total(banque) < 17:
    L = k.tireCarte()
    print("La banque a:")
    print(L)
    banque.ajouteCarte(L)
    if self.total(banque) > 21:
       print("La banque a dépassé 21. Vous avez gagné.")
       return

  # compare les main de la banque et du joueur au caus ou le 21 ne soit pas depasses afin de determine le vainqueur
  self.compare(banque, joueur)

 def total(self, main):
    ''' (Main) -> int
    calcule la somme des valeurs de toutes les cartes dans la main
    '''
    valeurs={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
    compteur = 0
    for i in main.main:
        compteur = compteur + valeurs[i.valeur]
    index = 0
    while index < len(main.main):
        if compteur > 21 and main.main[index].valeur == 'A':
            compteur = compteur - 10
        index = index + 1
    return compteur

 def compare(self, banque, joueur):
    ''' (Main, Main) -> bool
    Compare la main du joueur avec la main de la banque
    et affiche de messages
    '''
    banque = self.total(banque)
    joueur = self.total(joueur)

    if banque > joueur:
        print('Vous avez perdu.')
        return True
    elif joueur > banque:
        print('Vous avez gagnez.')
        return True
    else:
        print('Égalité')
        return True


class Main(object):
    '''represente une main des cartes a jouer'''
    main = []

    def __init__(self, joueur = 'joueur'):
        '''(Main, str)-> none
        initialise le nom du joueur et la liste de cartes avec liste vide'''
        self.joueur = joueur
        self.main = []



    def ajouteCarte(self, carte):
        '''(Main, Carte) -> None
        ajoute une carte a la main'''
        self.main.append(carte)



    def montreMain(self):
        '''(Main)-> None
        affiche le nom du joueur et la main'''
        print("{0} : {1}".format(self.joueur, self.main))



    def __eq__(self, autre):
        '''retourne True si les main ont les meme cartes
           dans la meme ordre'''
        return self.joueur == autre.joueur and self.main == autre.main


    def __repr__(self):
        '''retourne une representation de l'objet'''
        return(self.joueur + ' : ' + self.main)


class Carte:
    '''represente une carte a jouer'''

    def __init__(self, valeur, couleur):
        '''(Carte,str,str)->None
        initialise la valeur et la couleur de la carte'''
        self.valeur = valeur
        self.couleur = couleur  #  trefle, carreau pique ou  coeur

    def __repr__(self):
        '''(Carte)->str
        retourne une representation de l'objet'''
        return 'Carte('+self.valeur+', '+self.couleur+')'

    def __eq__(self, autre):
        '''(Carte,Carte)->bool
        self == autre si la valeur et la couleur sont les memes'''
        return self.valeur == autre.valeur and self.couleur == autre.couleur

class JeuDeCartes:
    '''represente une jeu de 52 cartes'''
    #  valeurs et   couleurs sont des variables de classe
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    # couleurs regroupe 4 symboles Unicode qui representent les 4 couleurs
    # trefle, carreau pique ou  coeur

    def __init__(self):
        'initialise le paquet de 52 cartes'
        self.paquet = []          # nouveau paquet vide lors du debut
        for couleur in JeuDeCartes.couleurs:
            for valeur in JeuDeCartes.valeurs: # variables de classe
                # ajoute une Carte de valeur et couleur
                self.paquet.append(Carte(valeur,couleur))

    def tireCarte(self):
        '''(JeuDeCartes)->Carte
        distribue une carte, la premiere du paquet'''
        return self.paquet.pop()

    def battre(self):
        '''(JeuDeCartes)->None
        pour battre le jeu des cartes'''
        shuffle(self.paquet)

    def __repr__(self):
        '''retourne une representation de l'objet'''
        return 'Paquet('+str(self.paquet)+')'

    def __eq__(self, autre):
        '''retourne True si les paquets ont les meme cartes
           dans la meme ordre'''
        return self.paquet == autre.paquet


j = Blackjack()
print("Hello braiteny , welcome to my room ! now you gonna play blackjack ")
j.joue()

