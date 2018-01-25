# -*- coding: utf-8 -*-

def compte_gap__insertion(file):
    """"
    La fonction compte_gap_insertion permet d'identifier et compter les gap et 
    les insertions. Elle retourne une liste qui contient soit les coordonnées de l'atomes
    Calpha, soit du nombre de gap ou nombre d'insertion.
    """
    fo=open(file,"r")
    lignes=fo.readlines()
    gap=0
    insertion=0
    liste=[]
    for ligne in lignes:
        if ligne=="-":
            gap+=1
            continue
            liste.append(gap)
        elif ligne[0:4]!="ATOM" and ligne!="-":
            insertion+=1
            continue
            liste.append(insertion)
        elif ligne[0:4]=="ATOM":
            liste.append("TRUE")
    print(len(liste))  
    return (liste)

