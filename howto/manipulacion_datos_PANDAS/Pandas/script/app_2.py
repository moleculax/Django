import pandas as pd

serie_empleados = pd.Series({
    101 : "amartinez@empresa.com",
    102 : "lperez@empresa.com",
    103 : "mgonzalez@empresa.com",
    104 : None,
    105 : "lfernandez@empresa.com",
    106 : "jsanchez@empresa.com",
    107 : "clopez@empresa.com",
    108 : None,
    109 : None,
    110 : "pruiz@empresa.com"
})

print("Serie de empleados:")
print(serie_empleados)

print("\nIdentificar valores faltantes:")
print(serie_empleados.isna())

print("\nTotal de valores faltantes:")
print(serie_empleados.isna().sum())
