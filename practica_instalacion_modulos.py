from camelcase import CamelCase

c = CamelCase()

s="esta oracion es para probar CamelCase"

camelCase = c.hump(s)

print(camelCase)