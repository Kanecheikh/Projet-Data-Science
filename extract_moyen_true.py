from xlwt import Workbook
import xlrd

# création
book = Workbook ()

# création de la feuille 1
feuil1 = book.add_sheet ('feuille 1')

# ajout des en-têtes
#feuil1.write (0, 0, 'id')
# ajout des valeurs dans la ligne suivante
#ligne1.write (0, '1')



# ajustement éventuel de la largeur d'une colonne
#feuil1.col (0).width = 10000

# éventuellement ajout d'une autre feuille 2
#feuil2 = book.add_sheet ('feuille 2')



#Lecture des donnees de la premiere feuille
wb= xlrd.open_workbook('Information_ecole.xlsx')
sh = wb.sheet_by_name(u'Feuil1')
colonne_moyenne = sh.col_values(4)
nom_elev= sh.col_values(1)
prenom_elev= sh.col_values(2)



# création matérielle du fichier résultant
book.save ('moy_simple.xls')
wb2 = xlrd.open_workbook('Information_ecole.xlsx')


for i in range(0,60):
    n = nom_elev[i]
    p = prenom_elev[i]
    m = str (colonne_moyenne[i])
    print(n, p, m)
