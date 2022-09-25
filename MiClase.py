# variables de clase en python
class MiClase:
    variable_clase = "variable clase"

    def __init__(self, var_instancia):
        self.var_instancia = var_instancia

    @staticmethod
    def metodo_statico():
        print(MiClase.variable_clase)
        """
        metodo estatico, gracias al decorador hacemos que este metodo
        se asocie con la clase y no con los objetos, y como se ve ya no 
        hay que poner el param self, pero por esto no puede acceder
        a las variables de instancia, solo a las var de clase
        """

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)
        """
        podemos acceder a los metodos de clase
        con cls, que significa class
        """

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_statico()










# las variables de clase se asocian a la clase misma y NO al objeto
# print(MiClase.variable_clase)
# para acceder a una var de instancia tenemos que crear un objeto
# objeto1 = MiClase("accediendo al la var instancia")
# print(objeto1.var_instancia)
# tambien desde nuestro objeto podemos acceder a la var de clase
# print(objeto1.variable_clase)

#tambien las var de instancia tienen diferentes valores por cada objeto a menos que se le asignen los mismos valores
# si un objeto modifica el valor de una var de clase, este cambio se vera reflejado en todos los demas obj


# llamada a un metodo statico de clase
MiClase.metodo_statico()
# llamada a un metodo de clase
MiClase.metodo_clase()


miobjeto1 = MiClase('Variable instancia')
miobjeto1.metodo_clase()
miobjeto1.metodo_instancia()