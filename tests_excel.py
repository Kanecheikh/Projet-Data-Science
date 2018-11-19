from xlwt import Workbook
import xlrd


# création
book1 = Workbook()

# création de la feuille 1
feuil1 = book1.add_sheet ('feuille 1')

# ajout des en-têtes
#feuil1.write (0, 0, 'id')

# ajout des valeurs dans la ligne suivante


# ajustement éventuel de la largeur d'une colonne
feuil1.col(0).width = 10000

#Lecture des donnees de la premiere feuille

wb1 = xlrd.open_workbook('Information_ecole.xlsx')
sh = wb1.sheet_by_name(u'Feuil1')
col_moy = sh.col_values(4)
nom_el= sh.col_values(1)
prenom_el= sh.col_values(2)
x = 0
y = 0

for i in range(0,60):
    n = nom_el[i]
    p = prenom_el[i]
    m = str(col_moy[i])
    if m < "10.0":
        continue
    feuil1.write(x, y, n)
    y+= 1
    feuil1.write(x, y, p)
    y += 1
    feuil1.write(x, y, m)
    y = 0
    x+=1

'''if m >"10":
       continue'''
book1.save ('moyenn.xls')




