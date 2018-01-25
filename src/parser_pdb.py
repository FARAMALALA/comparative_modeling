# -*- coding: utf-8 -*-

class Atom:
	""" 
	Classe Atom qui contient les atomes avec les coordonnée
	"""
	def __init__(self,nom="",num=0,x=0.0,y=0.0, z=0.0,res_name="",res_num=0):
			"""
			Initialisation d'un objet
			Définition des attributs avec des valeurs par défaut
			"""
			self.nom_atome=nom
			self.num_atome=num
			self.x=x
			self.y=y
			self.z=z
			self.res_name=res_name
			self.res_num=res_num

def parse(file):

	"""
	Une fonction qui parse un fichier pdb et on garde que les carbones alpha
	avec ses coordonnées , on sauvegarde aussi les noms des résidus à 3 lettres 
	ainsi que le nom des résidus à une letre qu'on va utiliser une fois qu'on a 
	l'alignement de la protéine cible et la protéine support
	"""

	fichier=open(file,'r')
	lignes=fichier.readlines()
	liste=[]
	for ligne in lignes:
		#  
		if ligne[0:3]!="END" and ligne[0:4]=="ATOM" and ligne[13:16]=="CA " :
			at=Atom()
			at.entete=ligne[0:4]
			at.num_atome=ligne[6:11]
			at.x=ligne[30:38]
			at.y=ligne[38:46]
			at.z=ligne[46:54]
			at.nom_atome=ligne[12:16]
			at.res_name=ligne[17:20]
			at.res_num=ligne[22:26]
			if ligne[17:20]== "ARG":
				at.res_one_letter="R"
			elif ligne[17:20]== "ASN":
				at.res_one_letter="N"
			elif ligne[17:20]== "ASP":
				at.res_one_letter="D"
			elif ligne[17:20]== "GLU":
				at.res_one_letter="E"
			elif ligne[17:20]== "GLN":
				at.res_one_letter="Q"
			elif ligne[17:20]== "LYS":
				at.res_one_letter="K"
			elif ligne[17:20]== "PHE":
				at.res_one_letter="F"
			elif ligne[17:20]== "TRP":
				at.res_one_letter="W"
			elif ligne[17:20]== "TYR":
				at.res_one_letter="Y"
			else :
				at.res_one_letter=ligne[17:18]
			liste.append(at)

	return liste



 

