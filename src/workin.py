from atomDicts import periodic_table
for elem in periodic_table:
    if 'colour' in elem:
        print(str(elem['anum'])+': \''+str(elem['colour'])+'\'', end=",\n")
    else:
        print(str(elem['anum'])+': \'black\'', end=",\n")