from camelcase import CamelCase #debimos hacer previamente: pip3 install camelcase

c = CamelCase()
oracion = 'esta oracion necesita camelCase!'

camelCased = c.hump(oracion) #el .hump nos permite que cada palabra comience con una mayuscula en caso de no tenerla
print(camelCased)