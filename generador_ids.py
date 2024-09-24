#Inf: El presente script genera todas las combinaciones posibles de cédulas Ecuatorianas
#teniendo un total de 150 millones de cédulas habidas y por haber, se creo este algoritmo con el objetivo
#de listar todos los usuarios de apps webs Ecuatorianas.

#Autor: Danilo Erazo 2021 - Reverse Everything @revers3everything
import random
import os
import sys
import time
num_provincias = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,30]

def generar_num_verificador(cedula):
    multiplicacion = []
    coeficientes = [2,1,2,1,2,1,2,1,2]
    for i in range(0,9):
        resul = coeficientes[i]*cedula[i]
        if resul>=10: #Si cualquier multiplicacion es mayor o igual a 10 se le resta 9
            resul=resul-9
        multiplicacion.append(resul)
    suma = sum(multiplicacion)
    modulo= suma % 10
    if modulo==0:
        ultimo_digito = 0
    else:
        ultimo_digito = 10 - modulo
    return ultimo_digito


def cedula2string(cedula):
    cedula_string = ""
    for i in cedula:
        cedula_string = cedula_string+str(i)
    return cedula_string

contador = 0
cedula = []

banner = """


             _____                         _                                   
            |  __ \                       (_)                                  
            | |__) |_____   _____ _ __ ___ _ _ __   __ _                       
            |  _  // _ \ \ / / _ \ '__/ __| | '_ \ / _` |                      
            | | \ \  __/\ V /  __/ |  \__ \ | | | | (_| |                      
   _____    |_|  \_\___| \_/ \___|_|  |___/_|_| |_|\__, |         _            
  / ____|       | |     | |           |  ____|      __/ |        | |           
 | |     ___  __| |_   _| | __ _ ___  | |__   ___ _|___/ __ _  __| | ___  _ __ 
 | |    / _ \/ _` | | | | |/ _` / __| |  __| / __| | | |/ _` |/ _` |/ _ \| '__|
 | |___|  __/ (_| | |_| | | (_| \__ \ | |___| (__| |_| | (_| | (_| | (_) | |   
  \_____\___|\__,_|\__,_|_|\__,_|___/ |______\___|\__,_|\__,_|\__,_|\___/|_|   
                                                                               
Author: Danilo Erazo @revers3everything - 2021

"""
print(banner)
for p in num_provincias:#Provincias
    print("\nProvincia numero: "+str(p))
    if p<10:
        cedula.append(0)
        cedula.append(p)
    else:
        p=str(p)
        cedula.append(int(p[0]))
        cedula.append(int(p[1]))
    for tres in range(0,6):#De 0 a 6> 0,1,2,3,4,5
        cedula.append(tres)
        for cuatro in range(0,10):
            cedula.append(cuatro)
            for cinco in range(0,10):
                cedula.append(cinco)
                for seis in range(0,10):
                    cedula.append(seis)
                    for siete in range(0,10):
                        cedula.append(siete)
                        for ocho in range(0,10):
                            cedula.append(ocho)
                            for nueve in range(0,10):
                                cedula.append(nueve)

                                cedula.append(generar_num_verificador(cedula))
                                contador = contador + 1
                                ced2string = cedula2string(cedula)

                                with open("/path/cedulas.txt","a") as f:
                                    f.write(ced2string+"\n")
                                print("Cedula "+str(contador)+" "+ced2string)
                                print()
                                cedula.pop()# digito verificador
                                cedula.pop()# noveno
                            cedula.pop()# ooctavo
                        cedula.pop()# septimo
                    cedula.pop()# sexto
                cedula.pop()# quinto
            cedula.pop()# cuarto
        cedula.pop()# tercero
    time.sleep(5)
    cedula = []#por cada provincia un nuevo vector
