ventas = [100, 1200, -50, 500, 0, 2000]
total_ventas = 0

for i in ventas:
    
    if i < 0:
        continue
    if i == 0:
        break
    if i > 1000:
        i += i * 0.10

    total_ventas += i
       
print(f"El total de ventas final es: {total_ventas:.2f}")