import os
import time
import DataBase as database
import AccionCajero as cajero


def registro():
    try:
        os.system("cls")
        print("-----Red de cajeros ATM-----")
        cuenta = input("Digite su número de tarjeta de crédito >> ")
        pin = input("Número de pin >> ")
        if (cuenta.isdigit() and 
            pin.isdigit() and len(pin) == 4):
             validar(cuenta, pin)
        else:
           print("--Ocurrió un error--")
           print("--Intente nuevamente--")
           time.sleep(5)
           registro()
    except Exception as ex:
        print(str(ex))
        registro()


def validar(tarjeta,  pin):
    for usu in database.usuarios:
        if (usu.NumTarjeta == tarjeta and 
            usu.Pin == pin):
            nombre = usu.Nombre
            numTarjeta = usu.NumTarjeta
            menu(nombre, numTarjeta)
        elif (usu.NumTarjeta == tarjeta or usu.Pin == pin):
            print("\nNumero de cuenta o pin son incorrectos")
            print("\nPorfavor intente nuevamente")
            time.sleep(5)
            registro()


def menu(nom, numTrt):
    try:
        os.system("cls")
        op = 9
        while op > 4:
            print(f"------ Bienvenido {nom} -----")
            print("------¿Que deseas hacer hoy?------")
            print("1. Depositar")
            print("2. Retirar")
            print("3. Ver saldos")
            print("4. Salir")
            op = int(input(">> "))
            if(op == 0):
                menu(nom, numTrt)
        acciones(op, numTrt, nom)
    except Exception as ex:
        print(str(ex))
        menu(nom, numTrt)

        
def acciones(op, numTrt, nombre):
    if(op == 1):
        cajero.depositar(numTrt)  
    elif(op == 2):
        cajero.retirar(numTrt)
    elif(op == 3):
        cajero.imprimirSaldo(numTrt)
    elif(op == 4):
        registro()

        
        
