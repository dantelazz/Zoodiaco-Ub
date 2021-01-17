
def zodiaco(dia,mes):
    signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
    fechas = (20, 19, 20, 20, 20, 21, 23, 23, 23, 22, 22, 21)
    mes=mes-1
    if dia>fechas[mes]:
        mes=mes+1
    if mes==12:
        mes=0
    print ("Tu signo es: " + signo[mes])
    
print(zodiaco(19,2))



#fechas: dias hasta
'''
    signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
    fechas = (  20,   19,   20,   20,   20,   21,   23,   23,   23,   22,   22,   21)
    indices      0      1    2     3     4     5     6     7     8     9    10    11
    meses        1      2    3     4     5     6     7     8     9     10   11    12
'''


