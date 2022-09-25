class Persona:
    contador_personas = 0

    @classmethod
    def _generar_sig_val(cls):
        cls.contador_personas+=1
        return  cls.contador_personas

    def __init__(self, nombre,edad):
        self.id_persona = Persona._generar_sig_val()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona {self.id_persona}, {self.nombre}, {self.edad}'



per1 = Persona('Duncan',20)
print(per1)
per2 = Persona('Clara',16)
print(per2)

