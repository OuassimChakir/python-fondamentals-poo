from TravailleurCommission import TravailleurCommission
from TravailleurHoraire import TravailleurHoraire
from Patron import Patron
emp1 = TravailleurCommission("Smith","John",3000,10,30)
patron = Patron("Alami","Mohammed",10000)
emp2 = TravailleurHoraire("Ipsum","Lorem",100,40)

print(emp1)
print("\tSalaire:",emp1.gains())
print(patron)
print("\tSalaire:",patron.gains())
print(emp2)
print("\tSalaire:",emp2.gains())