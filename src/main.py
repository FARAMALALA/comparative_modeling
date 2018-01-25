
# -*- coding: utf-8 -*-
import parser_pdb
import formater_fasta
import gap_insertion
import first_structure






if __name__ == '__main__':
    #pour recuperer uniquement la séquence de la protéine cible
    fasta_query=formater_fasta.recuperer_fasta("data/glut8.fasta")
    #pour récuperer uniquement la séquence protéique du support 
    fasta_template=formater_fasta.recuperer_fasta("data/4pyp.fasta")
    #alignement deux à deux entre la cible et le support
    align=formater_fasta.alignement(fasta_query,fasta_template)
    #parser le fichier pdb du support
    p= parser_pdb.parse("data/4pyp.pdb")
    #pour construire la structure initiale
    f= first_structure.first_structure(align,p)
    #on stocke dans un fichier la structure initiale obtenue
    out=open("result/first_structure.pdb","w")
    for i in range(len(f)):
        out.write(f[i]+'\n')
    out.close()

    #print(gap_insertion.compte_gap__insertion("result/first_structure.pdb"))
    #print (align[0])
    #print(align[0][0])
    #print(format_alignment(*align[0]))
    