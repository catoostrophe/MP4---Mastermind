from random import *

def mastermind():
    print("------------------------------------")
    print("Vous devez trouver la combinaison secrète de 4 chiffres. Vous avez gagné si vous y parvenez en un maximum de 12 coups.")
    print()
    print("Six nombres sont a votre disposition: 0 1 2 3 4 5")
    print()
    codesecret=[]
    alignementoriginal(codesecret)
    x=0
    while x < 13:
        if essai(codesecret,x)==True:
            print()
            print("Vous avez trouvé! Bravo! Vous ralentissez le hacker encore un peu plus. Hehe.")
            x=50
            x=x+1
    if x<30:
        print()
        print("Vous n'avez pas réussi à trouver le code! C'est dommage. Votre ordinateur est maintenant pleins de virus. Je vous félicite pas.")
        
    print("Le code était:", codesecret)
    time.sleep(5)
    exit()


def alignementoriginal(codesecret):
    for x in range(0,4):
        codesecret.append(randint(0,5))
    return codesecret


def essai(codesecret,x):
    L=['0','1','2','3','4','5']
    strcodeessai=input()
    codeessai=[(strcodeessai[0]),strcodeessai[1],strcodeessai[2],strcodeessai[3]]
    #verification de l'input
    for i in range(0,4):
        if codeessai[i] not in L:
            print("Veuillez entrer uniquement des nombres à votre disposition")
            essai(codesecret,x)
    codeessai=[int(codeessai[0]),int(codeessai[1]),int(codeessai[2]),int(strcodeessai[3])]
    if verification(codesecret,codeessai)==True:
        return True

def verification(codesecret,codeessai):
    if codeessai==codesecret:
        return True
    else:
        bon2=bon=faux=0
    for i in range(0,4):
        if codeessai[i]==codesecret[i]:
            bon2=bon2+1
            bon=bon+1
        elif codeessai[i] in codesecret:
            bon=bon+1
        else:
            faux=faux+1
    print()
    print("Il y a", bon2, "bons nombres bien places dans le code,", bon," nombres contenu dans le code, et", faux, "nombres non dans le code.")
    print()


mastermind()
