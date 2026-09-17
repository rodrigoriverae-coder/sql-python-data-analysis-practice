temperaturas = [22, 28, 19, 31, 25, 27, 21]

dias_calurosos = []

maxima = temperaturas[0]

for i in temperaturas:
    if i > maxima:
        maxima = i
    if i > 25:
     dias_calurosos.append(i)

print(maxima)
print(dias_calurosos)