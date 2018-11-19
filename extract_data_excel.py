import xlrd

#ouverture du fichier excel
wb= xlrd.open_workbook('Information_ecole.xlsx')

#feuille dans le classeur
print (wb.sheet_names())
[u'Feuil1']

#Lecture des donnees de la premiere feuille
sh = wb.sheet_by_name(u'Feuil1')
colonne_moyenne = sh.col_values(4)
nom_elev= sh.col_values(1)
prenom_elev= sh.col_values(2)
print ("voci la liste des eleves ayant la moyenne")




from xlwt import Workbook
#creation
list_moy_eleve = Workbook()

#creation de la feuil moyen
feuil1 = list_moy_eleve.add_sheet('feuil1')

# ajout des en-têtes
feuil1.write(0,0,'id')
feuil1.write(0,1,'x')
feuil1.write(0,2,'y')
feuil1.write(0,3,'test')

for i in range(0,60):
    n = nom_elev[i]
    p = prenom_elev[i]
    m = str (colonne_moyenne[i])
    print (n, p, m)






















"""import xlrd

#ouverture du fichier excel
wb= xlrd.open_workbook('Information_ecole.xlsx')

#feuille dans le classeur
print (wb.sheet_names())
[u'Feuil1']

#Lecture des donnees de la premiere feuille
sh = wb.sheet_by_name(u'Feuil1')
'''for rownum in range(sh.nrows):
    print ("|--------------------------------------------------------------------------------------------------------------------------------|)")
    print (sh.row_values(rownum))
    [u'Feuil']
    [2.0, 245.0, 444.0, u'b']'''

#Lecture des eleves ayant la moyenne
colonne_moyenne = sh.col_values(4)
nom_elev= sh.col_values(1)
prenom_elev= sh.col_values(2)
print ("voci la liste des eleves ayant la moyenne")
for i in range(0,60):

    n=nom_elev[i]
    p=prenom_elev[i]
    m = str(colonne_moyenne[i])
    print(n+"     ", p+"   ", m)"""



