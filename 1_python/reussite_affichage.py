# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.

import random
from random import choice
from turtle import *

def afficher_reussite(liste_reussite,iteration):
    # coordonnées de démarrage
    xinit = -300
    yinit =  250

    largeur_carte = 44
    hauteur_carte = 64
    separation = 5      # espace à laisser entre les cartes
    separation_y = 25  



    up()          # on ne trace pas les déplacement
    speed(2)      # changer la vitesse d'affichage 0-10

    tampons = {}  # dictionnaire pour se souvenir où on a placé les cartes

    # Affichage de toutes les cartes dans l'ordre
    y = yinit-(separation_y)*iteration
    if iteration%15==0:
        clearstamps()
    if y<-250:
        y=y+500
    x=xinit
    for tas in liste_reussite:
        shape(dos)
        goto(x,y)
        c=tas['couleur']
        v=str(tas['valeur'])
        shape(carte[c,v])
        tampons[c,v] = stamp()
        x=x+largeur_carte+separation
    #hideturtle()
    #print(tampons)

def init_pioche_fichier(nom_fichier):
    """Manipulation d'un fichier .txt pour conversion en dictionnaires de cartes.
        Lecture du fichier puis extraction de la ligne. Chaque carte est stocké dans un élément d'une liste.
        Conversion des cartes en dictionnaire et sr=tockage dans une nouvelle liste qui sera retournée."""
    with open(nom_fichier) as f:
        cartes_full = f.readlines()
    for line in cartes_full:
        cartes_split=line.split()
    cartes_clean=[]
    for carte in cartes_split:
        carte_list=list(carte)
        if carte_list[1]!='-':
            cartes_clean.append({'couleur':carte_list[-1],'valeur': int(carte_list[0]+carte_list[1])})
        elif ord(carte_list[0])>57:
            cartes_clean.append({'couleur':carte_list[-1],'valeur': carte_list[0]})
        else:
            cartes_clean.append({'couleur':carte_list[-1],'valeur': int(carte_list[0])})
    return cartes_clean
    
def ecrire_fichier_reussite(nom_fich,pioche):
    """ Ecrit la pioche dans un fichier au même format que le fichier init."""
    with open(nom_fich,"w") as f:
        for carte in pioche:
            f.write(str(carte['valeur']))
            f.write("-")
            f.write(carte['couleur'])
            f.write(" ")
            
def init_pioche_alea(nb_cartes=32):
    """ Crée une liste de cartes complétes d'un deck, les mélange et le renvoie.
    Argument optionnel : nb_cartes=52 pour créer un deck de 52 cartes.
    Toute autre valeur de nb_cartes sera ignoré."""
    deck=[]
    figures=['V','D','R','A']
    couleurs=['C','P','K','T']
    for i in range(7,11):
        for couleur in couleurs:
            deck.append({"valeur":i,'couleur':couleur})
    for figure in figures:
        for couleur in couleurs:
            deck.append({"valeur":figure,'couleur':couleur})
    if nb_cartes==52:
        for i in range(2,7):
            for couleur in couleurs:
                deck.append({"valeur":i,'couleur':couleur})
    random.shuffle(deck)
    return(deck)
    
def alliance(carte1,carte2):
    if carte1['valeur']==carte2['valeur'] or carte1['couleur']==carte2['couleur']:
        return True
    else:
        return False
        
def saut_si_possible(liste_tas,num_tas):
    retour=False
    if len(liste_tas)>=3:
        if num_tas>0 and num_tas<=len(liste_tas)-2:
            if alliance(liste_tas[num_tas-1],liste_tas[num_tas+1]):
                retour=True
                del liste_tas[num_tas-1]
    return retour

def une_etape_reussite(liste_tas,pioche,iteration,affiche=False):
    liste_tas.append(pioche[0])
    del pioche[0]
    if affiche:
        afficher_reussite(liste_tas,iteration)
    #saut=saut_si_possible(liste_tas,len(liste_tas)-2)
    #if saut:
    #    afficher_reussite(liste_tas)
    saut=True
    while saut:
        retour=False
        for tas in liste_tas:
            if saut_si_possible(liste_tas,liste_tas.index(tas)):
                retour=True
                if affiche:
                    afficher_reussite(liste_tas,iteration)
                break
        iteration+=1
        saut= retour
        
def reussite_mode_auto(pioche,affiche=False):
    pioche_c=pioche.copy()
    liste_tas=[]
    iteration=0
##    if affiche:
##        afficher_reussite(pioche_c)
    while bool(pioche_c)==True:
        une_etape_reussite(liste_tas,pioche_c,iteration,affiche)
        iteration+=1
    return liste_tas
    
def swapPositions(list1, pos1, pos2): 
    list2=list1.copy()
    list2[pos1], list2[pos2] = list2[pos2], list2[pos1] 
    return list2

def meilleur_echange_consecutif(pioche):
    nb_tas_init=len(reussite_mode_auto(pioche,affiche=False))
    nb_tas_min=nb_tas_init
    for i in range(len(pioche)-1):
        pioche_alt=swapPositions(pioche,i,i+1)
        nb_tas=len(reussite_mode_auto(pioche_alt,affiche=False))
        if nb_tas<=nb_tas_min:
            pioche_opti=pioche_alt.copy()
            tas_econom=nb_tas_init-nb_tas
            nb_tas_min=nb_tas
    return pioche_opti, tas_econom
        
if __name__=="__main__": # NE PAS SUPPRIMER CETTE LIGNE
    # Vous pouvez utiliserle programme principal
    # pour tester votre pr'ogramme en faisant les appels de votre choix.
    print("Debut du prog. principal")

    valeurs  = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'V', 'D', 'R', 'A']
    couleurs = ['P', 'C', 'K', 'T']
    fenetre = Screen()
    # On charge toutes les images des cartes dans le dictionnaire _carte_
    carte = {}
    for c in couleurs:
            for v in valeurs:
                    fichier = "imgs/carte-" + v + '-' + c + '.gif'
                    carte[c, v] = fichier
                    fenetre.register_shape( fichier ) # nouvelle forme pour le pointeur
    # On charge aussi l'image du dos des cartes
    dos = "imgs/carte-dos.gif"
    fenetre.register_shape( dos )

    reussite_mode_auto(init_pioche_alea(),True)
    
    exitonclick() # on attend un clic et on ferme la fenetre

