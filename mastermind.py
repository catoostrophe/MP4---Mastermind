from random import *

def mastermind():
  codesecret=[]
  alignementoriginal(codesecret)
  x=0
  while x < 13:
    if essai(codesecret,x)==True:
      print("Vous avez gagné")
      x=50
    x=x+1
  if x<30:
    print("Vous avez perdu")
  print("Le code était:", codesecret)


def alignementoriginal(codesecret):
  for x in range(0,4):
    codesecret.append(randint(0,5))
  print(codesecret)
  return codesecret
    

def essai(codesecret,x):
  strcodeessai=input()
  codeessai=[(strcodeessai[0]),strcodeessai[1],strcodeessai[2],strcodeessai[3]]
#verification de l'input
  for i in range(0,4):
    if codeessai[i] not in ['0','1','2','3','4','5']:
      print("Veuillez entrer uniquement des nombres a votre disposition")
      essai(codesecret)
  codeessai=[int(codeessai[0]),int(codeessai[1]),int(codeessai[2]),int(strcodeessai[3])]
  print(codeessai)
  print(x)
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
    print("Il y a", bon2, "bons nombres bien places dans le code,", bon," nombres contenu dans le code, et", faux, "nombres non dans le code.")

#introduction mastermind
print("Le joueur qui doit trouver la combinaison secrète de 4 chiffre gagne dès lors qu’il y parvient en maximum 12 coups.")
print("")
print("Quatre nombres sont a votre disposition: 0 1 2 3 4 5")

mastermind()
