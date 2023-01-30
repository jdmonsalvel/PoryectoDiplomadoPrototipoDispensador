import utime

def programar_dispensado(hora_inicio, hora_fin, num_ejecuciones):
    contador = 0
    intervalo = (hora_fin - hora_inicio) / num_ejecuciones
    while True:
        hora_actual = utime.localtime()[3]
        if hora_inicio <= hora_actual < hora_fin:
            if contador < num_ejecuciones:
                check_dispense()
                contador += 1
                utime.sleep(intervalo * 60 * 60)
            else:
                contador = 0
                utime.sleep(1*60*60)
        else:
            utime.sleep(1*60*60)