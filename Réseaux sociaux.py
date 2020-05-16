from csv import *
import os
import matplotlib.pyplot as plt


# On se place dans le bon dossier
os.chdir("C:\\Users\\othma\\OneDrive\\Bureau\\Vues fusionnées\\")
# Création de liste
pge_fb=[]
pge_likedin=[]
pge_twitter=[]

with open('1_informations_generales.csv', 'r',encoding="utf8") as file:
    hey = reader(file,delimiter=';')
    for something in hey:
        fb=something[10]
        pge_fb.append(fb)
        liki=something[11]
        pge_likedin.append(liki)
        twi=something[12]
        pge_twitter.append(twi)

def range_moi_ca(L):
    P=[]
    for elt in L:
        if elt not in P and elt !='':
            P.append(elt)
    return P

fb=range_moi_ca(pge_fb)
twitter=range_moi_ca(pge_twitter)
linkedin=range_moi_ca(pge_likedin)

fig = plt.figure()
x=['Facebook','Twitter','Likedin']
height=[len(fb),len(twitter),len(linkedin)]
width = 0.005
widths = 20

plt.scatter(x, height, widths, color='b' )
plt.bar(x, height, width, color='b' )
plt.show()

