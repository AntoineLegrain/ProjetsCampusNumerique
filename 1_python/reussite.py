# Ecrivez votre programme ci-dessous.
# Bouton Fullscreen pour passer en plein ecran
# Ensuite Save + Run puis Save + Evaluate
# Pour des raisons techniques, laissez une ligne blanche avant de commencer votre programme.

import random
from random import choice
from turtle import *

def carte_to_chaine(carte):
    """Renvoie le numéro de carte avec le joli symbôle. Met un espace devane le numéro si il 
    y a qu'un seul chiffre."""
    valeur_carte=str(carte['valeur'])
    if carte['couleur']=='P':
        symbole_carte=chr(9824)
    elif carte['couleur']=='C':
        symbole_carte=chr(9825)
    elif carte['couleur']=='K':
        symbole_carte=chr(9826)
    elif carte['couleur']=='T':
        symbole_carte=chr(9827)
    if len(valeur_carte)==1:
        return " "+valeur_carte+symbole_carte
    else:
        return valeur_carte+symbole_carte
        
def afficher_reussite(liste_reussite):
    """Affiche la réussite comme sur une table.cListe des cartes en argument 
    (la première carte à gauche a comme index 0)."""
    if not liste_reussite:
        print("\n")
    else:
        reussite=[]
        for carte in liste_reussite:
            reussite.append(carte_to_chaine(carte))
        print (" ".join(reussite),"\n")

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

def une_etape_reussite(liste_tas,pioche,affiche=False):
    liste_tas.append(pioche[0])
    del pioche[0]
    if affiche:
        afficher_reussite(liste_tas)
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
                    afficher_reussite(liste_tas) 
                break
        saut= retour
        
def reussite_mode_auto(pioche,affiche=False):
    pioche_c=pioche.copy()
    liste_tas=[]
    if affiche:
        afficher_reussite(pioche_c)
    while bool(pioche_c)==True:
        une_etape_reussite(liste_tas,pioche_c,affiche)
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
    reussite_mode_auto(init_pioche_alea(),True)
    bu=input()
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

    # coordonnées de démarrage
    xinit = -300
    yinit =  100

    largeur_carte = 44
    hauteur_carte = 64
    separation = 5      # espace à laisser entre les cartes



    up()          # on ne trace pas les déplacement
    speed(3)      # changer la vitesse d'affichage 0-10

    tampons = {}  # dictionnaire pour se souvenir où on a placé les cartes

    # Affichage de toutes les cartes dans l'ordre
    y = yinit
    for c in couleurs:
            x = xinit

            for v in valeurs:
                    print ("Affichage de", v, "-", c, "à la position", (x,y))

                    shape( dos )      # pour faire joli: on affiche le dos des cartes pendant
                                                      # le déplacement de la tortue
                    goto (x, y)                 # on déplace la tortue à l'endroit voulu
                    shape( carte[c, v] )      # on change la "forme" de la tortue pour
                                                                            # l'image de la carte correspondante
                    tampons[c, v] = stamp()  # on "tamponne" la forme et on sauvegarde le
                                                                            # numéro du tampon

                    x = x + largeur_carte + separation

            y = y - hauteur_carte - separation

    hideturtle()  # on cache la tortue

    print (tampons)

    # On efface toutes les cartes dans un ordre aléatoire
    while tampons != {}:
            v = choice (valeurs)   # valeur au hasard
            c = choice (couleurs)  # couleur au hasard

            if (c, v) in tampons:   # si on n'a pas déjà effacé le tampon
                    print ("Efface la carte", v, "-", c)
                    clearstamp ( tampons[c, v] )  # on l'efface
                    tampons.pop ((c, v))            # puis on l'enlève du dictionnaire

    goto(0,0)
    write("Cliquez dans la fenêtre pour terminer.", align='center')
    exitonclick() # on attend un clic et on ferme la fenetre

