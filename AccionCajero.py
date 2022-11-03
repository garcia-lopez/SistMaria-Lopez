import os
import time
import DataBase as database
import Funciones as functions


def accion(numTrt, nombre):
    try:
        time.sleep(5)
        os.system("cls")
        print("¿Desea realizar algo más?")
        op = int(input("1. Si - 2. No >> "))
        if(op == 1):
          functions.menu(nombre, numTrt)
        elif(op == 2):
           print("<> Gracias por su visita <>")
           time.sleep(3)
           functions.registro()
        else:
           accion(numTrt, nombre)   
    except Exception as ex:
        print(str(ex))
        accion(numTrt, nombre)
        

def buscarSaldo(numTrt):
    for usu in database.usuarios:
        if(usu.NumTarjeta == numTrt):
            saldoUsuario = usu.Saldo
            nombre = usu.Nombre
    return saldoUsuario, nombre


def actualizar(numTrt, saldoNuevo):
   for usu in database.usuarios:
        if(usu.NumTarjeta == numTrt):
            usu.Saldo = saldoNuevo
 
            
def multiploCien(monto):
    if monto % 100 == 0 :
        return True
    print("El monto debe ser multiplo de 100")
    time.sleep(5)
    return False


def imprimirSaldo(numTrt):
    os.system("cls")
    saldoActual, nombre = buscarSaldo(numTrt)
    print("Saldo actual >> ", saldoActual)
    accion(numTrt, nombre)
 
    
def imprimirRecibo(code, monto, disponible, numTrt, nombre):
    print("")
    print("---RED DE CAJEROS ATM---")
    if(code == 1):
        print("----DEPOSITO----")
    else:
        print("----RETIRO----")
    print(f"MONTO: {monto}")
    print(f"DISPONIBLE: {disponible}")
    accion(numTrt, nombre)


def depositar(numTrt):
   try:
        os.system("cls")
        code = 1
        saldoActual, nombre = buscarSaldo(numTrt)
        deposito = int(input("Digite cantidad a depositar >> "))
        if multiploCien(deposito):
           saldoNuevo = saldoActual + deposito
           actualizar(numTrt, saldoNuevo)
           print("Deposito realizado exitosamente")
           imprimirRecibo(code, deposito, saldoNuevo, numTrt, nombre)
           accion(numTrt, nombre)     
        else:
           depositar(numTrt)      
   except Exception as ex:
       print(str(ex))
       time.sleep(3)
       depositar(numTrt)
       
  
def retirar(numTrt):
    try:
        os.system("cls")
        code = 2
        saldoActual, nombre = buscarSaldo(numTrt)
        retiro = int(input("Digite la cantidad a retirar >> "))
        if multiploCien(retiro):
           if(retiro <= saldoActual):
              saldoNuevo = saldoActual - retiro
              actualizar(numTrt, saldoNuevo)
              print("Retiro realizado exitosamente")
              imprimirRecibo(code, retiro, saldoNuevo, numTrt, nombre)
           else:
             print("El valor a retirar debe ser menor que el saldo actual")
             time.sleep(5)
             retirar(numTrt)
        else:
         retirar(numTrt) 
    except Exception as ex:
        print(str(ex))
        time.sleep(3)
        retirar(numTrt)
   

    

    
        
        
    
    

    

  
            
            

 

