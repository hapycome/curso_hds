nombre= "lizbeth"
edad = 30
cadena = "Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años."
print(cadena) # Hola, mi nombre es lizbeth y tengo 30 años

################
#formato con %

nombre = "lizbeth"
edad = 30
cadena = "Hola, mi nombre es " + nombre + " y tengo " + str(edad) + " años."
print(cadena) # Hola, mi nombre es lizbeth y tengo 30 años

############
# formateo con formato ()

nombre = "lizbeth"
edad = 30
cadena = "Hola, mi nombre es {} y tengo {} años.".format(nombre, edad)
print(cadena) # Hola, mi nombre es lizbeth y tengo 24 años

#############
#f-string

name = "lizbeth"
age = 30
text = f"My name is {name} and I am {age} years old."
print(text)
# Output: My name is lizbeth and I am 24 years old.