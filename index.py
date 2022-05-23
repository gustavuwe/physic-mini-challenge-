type = str(input('O que você quer saber? velocidade media, distancia percorrida ou tempo?: '))

if type == 'velocidade media':

    ΔS = float(input('em metros, qual foi a distancia percorrida?: '))

    ΔT = float(input('em segundos, qual foi o tempo?: '))

    calc = ΔS / ΔT

    print(f'a velocidade média foi de: {calc:.2f} metros')

elif type == 'distancia percorrida':
    
    Vm = float(input('em metros por segundo, qual foi a velocidade média?: '))

    ΔT = float(input('em segundos, qual foi o tempo?: '))

    calc = Vm * ΔT

    print(f'a distancia percorrida foi de: {calc:.2f} metros')

elif type == 'tempo':

    ΔS = float(input('em metros, qual foi a distância percorrida? '))
    
    Vm = float(input('em metros por segundo, qual foi a velocidade média?: '))

    calc = ΔS / Vm

    print(f'o tempo foi de: {calc:.2f} segundos')

