from datetime import datetime


from datetime import date

hoy = date(2022, 10, 14)
otraFecha = date(2021,8,6)

delta = hoy - otraFecha

print(delta)
print(delta.days)