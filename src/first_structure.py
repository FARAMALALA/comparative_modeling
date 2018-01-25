# -*- coding: utf-8 -*-

def first_structure(alignement,pdb):
    """
    cette fonction prend les coordonnées des atomes de C alpha correspondant 
    entre la séquence cible et la séquence support. A partir de l'alignement et 
    du fichier pdb parsé de la séquence support, on construit la structure initiale
    constituée uniquement de carbone alpha
    """
    query=list(alignement[0])
    template=list(alignement[1])
    j=0
    liste=[]
    for i in range(len(template)):
        for j in range(i,len(pdb)):
            if template[i]==query[i] and pdb[j].res_one_letter==template[i]:
                f=pdb[i].entete+pdb[i].num_atome+pdb[i].nom_atome\
                +pdb[i].res_name+pdb[i].res_num+pdb[i].x+pdb[i].y+pdb[i].z
                if f not in liste:
                    liste.append(f)
                    
    return liste