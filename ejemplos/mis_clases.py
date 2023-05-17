"""

"""

# Crear dos clases en Python
# Usted defina el nombre y los atributos
# Puede usar las mismas clases usadas en Java en los ejemplos estudiados

# clase 01

class Ciudad:

    def __init__(self,ciud,cantones):

        self.ciud = ciud
        self.cantones = cantones

    def __str__(self):

        return(f"La ciudad de {self.ciud} tiene {self.cantones} cantones.")

# clase 02

class Usuario:

    def __init__(self,name,ced):

        self.name = name
        self.ced = ced

    def __str__(self):

        return f"El numero de cedula de {self.name} es {self.ced}"
