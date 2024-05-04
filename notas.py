lista_notas = []  
suma_notas = 0 
for i in range(4):
   
    while True:
        try: 
            notas = int(input('Introduce la nota: '))
            if not(-1 < notas < 101): 
                print('*El puntaje de las notas debe ser de entre 0 a 100 puntos*')
                continue
            break
        except ValueError:
            print('*Error!. Introduce solo valores numericos*')
        list
    
    lista_notas.append(notas) 
    lista_notas.sort(reverse=True)
    suma_notas = suma_notas + notas 

    resultado_total = suma_notas / 4 

print('Notas introducidas:', lista_notas)

print('Promedio:', resultado_total)