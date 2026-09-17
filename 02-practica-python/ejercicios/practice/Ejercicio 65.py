softwares = ["Excel", "Python", "Tableau", "SQL Server", "Power BI"]

softwares.append("Docker")
softwares.remove("Tableau")
softwares.sort()

print(f'{softwares}')
cantidad = len(softwares)
print(f'En total hay {cantidad} softwares','\n')