palabra = input("Escribe un texto: ").lower().replace(" ","")

palindromo = [i for i in palabra if palabra == palabra[::-1]]

if palindromo != []:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")