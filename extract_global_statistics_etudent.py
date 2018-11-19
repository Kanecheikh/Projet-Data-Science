from xlwt import Workbook
import xlrd


# création
book = Workbook ()

# création de la feuille 1
feuil1 = book.add_sheet ('feuille 1')

# ajout des en-têtes
#feuil1.write (0, 0, 'id')

# ajout des valeurs dans la ligne suivante


# ajustement éventuel de la largeur d'une colonne
feuil1.col(0).width = 10000

# éventuellement ajout d'une autre feuille 2
#feuil2 = book.add_sheet ('feuille 2')



#Lecture des donnees de la premiere feuille
wb = xlrd.open_workbook('Information_ecole.xlsx')
sh = wb.sheet_by_name(u'Feuil1')
colonne_age = sh.col_values(5)
nom_elev= sh.col_values(1)
prenom_elev= sh.col_values(2)
# création matérielle du fichier résultant
# ajout des en-têtes

x = 0
y = 0
for i in range(0,60):
    n = nom_elev[i]
    p = prenom_elev[i]
    m = str (colonne_age[i])
    if m< "20":
        continue
    feuil1.write (x,y, n)
    y+=1
    feuil1.write (x, y, p)
    y+=1
    feuil1.write (x, y, m)
    y=0
    x+=1



book.save('agesimple.xls')

'''for i in range(0,60):
    n = nom_elev[i]
    p = prenom_elev[i]
    m = str (colonne_age[i])
    print (n, p, m)'''