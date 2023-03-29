from datetime import timedelta
def agregar_cero_si_es_necesario(valor):
    return f"{valor:02d}"
num = 88.86689758300781

def getTiempos(segundos):
    segundos = num
    minutos, segundos_sobrantes = divmod(segundos, 60)
    return (agregar_cero_si_es_necesario(int(minutos)) + ":{0:.3f}".format(segundos_sobrantes))

print(getTiempos(88.86689758300781))