# comparative_modeling
 Ce programme permet de construire un modèle comparative developpé en python 3.
Le programme est en cours de développement

# PRINCIPE
On a besoin comme données de départ le fichier fasta de la protéine à modéliser ainsi
que le fichier fasta et le fichier pdb de la structure support.
Placer ces fichiers dans le dossier data pour pouvoir tester le programme.
Pour parser le fichier pdb, on prend en compte uniquement que du carbone alpha 
pour générer une structure initiale.
Les fichiers fasta seront utiles pour effectuer l'alignement de la protéine cible et de du support.


# MODULE:
Alignement: __Pairwaise de Biopython__
On utilise Biopython pour effectuer l'alignement. Pour installer Biopython:

Pour le système unix:
'''{r,engine='bash',count_lines}
$ sudo apt-get install python3-pip
$ python3 -m pip install 'biopython'
'''

Pour le système macos:
'''{r,engine='bash',count_lines}
  $ Install Xcode from appstore 
 $ Install numpy, and biopython
$ Install MacPorts: https://www.macports.org/install.php
$ pip3 install numpy
$ pip3 install biopython
''''

# UTILISATION
Pour utiliser ce programme placer dans le dossier principal:
'''{r,engine='bash',count_lines}
$ python3 src/main.py
'''
