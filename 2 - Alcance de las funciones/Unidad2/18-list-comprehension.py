# pares = [i for i in range(101) if i % 3 == 0]

meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

meses_o = [i for i in meses if i[-1:] == 'o'] 
meses_e = [i for i in meses if i[-1:] == 'e'] 

print(meses_o)
print(meses_e)