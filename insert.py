a = ["Master","Online"]
b = "Code"
a.insert(1, "Code")
print(a)
c = [1, 2, 3]
c = [4, 5, 6]
d = [1, 2, 3]
c.insert(0, d)
print(c)

Lobos = ["Joseph","Hyrum","Alan","Rogelio","Rafa","Levi","Abinadi","Moroni","Nico","Benja","Angel"]
Lobos.sort()
print(Lobos)

Lobos = ["Joseph","Hyrum","Alan","Rogelio","Rafa","Levi","Abinadi","Moroni","Nico","Benja","Angel"]
Lobos.sort(reverse = True, key=len)
print(Lobos)