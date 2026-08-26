import json


class Person:
    def __init__(self, name="", age=0, mail=""):
        self.name = name
        self.age = age
        self.mail = mail

    def __str__(self):
        return f"{self.name} ({self.age}) - {self.mail}"

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "mail": self.mail
        }


# Crear varias personas
personas = [
    Person("Tobias", 25, "elmail"),
    Person("Ana", 30, "ana@mail.com"),
    Person("Luis", 28, "luis@mail.com")
]

# Convertir toda la lista a diccionarios
datos = [p.to_dict() for p in personas]

# Convertir a JSON

json_data = json.dumps(datos, indent=2)
print("\nDatos como JSON:")
print(json_data)