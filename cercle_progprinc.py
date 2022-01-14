from cercle_module import *

cyl = Cylindre(5,7)
print("{0:.2f}".format(Cercle.surface(cyl)))
print("{0:.2f}".format(Cylindre.surface(cyl)))
print("{0:.2f}".format(cyl.surface()))
print("{0:.2f}".format(cyl.volume())) #essai

co = Cone(5,7)
print("{0:.2f}".format(co.volume()))
# print(f"De cercle_progprinc:  __name__ == {__name__}.")
print("une nouvelle ligne")

x = 33
