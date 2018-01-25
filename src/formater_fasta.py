# -*- coding: utf-8 -*-
from Bio import pairwise2
from Bio.pairwise2 import format_alignment




def recuperer_fasta(file):
    """
    recuperer_fasta est une fonction qui permet de récuperer uniquement les séquences 
    protéiques de la séquence cible ou de la séquence support, elle retourne une liste 
    qui contient la séquence provenant d'un fichier fasta
    """
    file_fasta=open(file,"r")
    lignes=file_fasta.readlines()
    liste=[]
    fasta=""
    for ligne in lignes:
	    liste.append(ligne)
    for i in range(1,len(liste)):
	    fasta=fasta+str(liste[i])
    fasta=fasta.replace('\n','')
    return fasta

def alignement(fasta_query,fasta_template):
    """
    La fonction alignement permet d'effectuer l'alignement entre la séquence
    cible et la séquence support. Elle prend en entréd deux listes qui contiennent
    les séquences à aligner. Lz fonction retourne une liste qui contient l'alignement
    effectuer par le module pairwise et stocke aussi dans un fichier le résultat de
    l'alignement
    """
    align=[]
    alignments = pairwise2.align.globalxx(fasta_query, fasta_template)
    for i in alignments[0][0:2]:
        align.append(i)
    f=open('result/align.out','w')
    f.write(str(align))
    f.close()
    return align




