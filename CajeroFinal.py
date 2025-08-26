intentos = 3
Saldo = int(1000)

def user_password():
   print("ingrese su PIN")
   return(int(input()))

def menu():
    print("""     
    1.-Consultar saldo
    2.-Retirar dinero
    3.-Depositar dinero
    4.-Salir""")
    return(int(input("")))

def Consultar():
    if seleccion == 1:
        print("su saldo actual es de",Saldo)

def Retirar():
    global Saldo
    print("Ingrese cantidad a retirar:")
    retiro = int(input())
    if retiro > Saldo:
        print("no se puede retirar esta cantidad")
                        
    else: 
        Saldo = Saldo-retiro
        print("Retiro exitoso. Saldo restante",Saldo)

def Depositar():
    global Saldo
    print("Ingrese cantidad a depositar:")
    deposito = int(input())
    if deposito == 0:
        print("no se puede depositar esta cantidad")
    else:
        Saldo = Saldo+deposito
        print("Deposito exitoso. Saldo actual",Saldo)

password = user_password()

while intentos < 4 :
   
   if password == 12345 :
      print("""

   Bienvenido al cajero automatico """)
      intentos = 5

      seleccion = menu()
      while seleccion != 5 :
            if seleccion > 4:
               print("opcion no valida")

            if seleccion == 1:
               Consultar()
               
               
            elif seleccion == 2:
                Retirar()
                        
            elif seleccion == 3:
               Depositar()
               

            elif seleccion == 4:
               print("Gracias por usar el cajero.")
               quit()

            seleccion = menu()

   else:
      print("PIN incorrecto")
      intentos = intentos-1
      print("intentos restantes:",intentos)
      password = user_password()
      
   
   if intentos == 1:
      print("Cuenta bloqueada")
      quit()