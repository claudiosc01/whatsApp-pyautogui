import time
import pyautogui
import subprocess
import importlib

try:
    importlib.import_module('pyautogui')
    print("La librería pyautogui ya está instalada.")
except ImportError:
    print("La librería pyautogui no está instalada. Instalando...")
    subprocess.run(["pip", "install", "pyautogui"])
    print("La librería pyautogui ha sido instalada.")

print("")
print("  ***********************************************************************************************************")
print("  * "".___            __               __             ._____      __             __   .__                    "" *")
print("  * ""|   | ____     |__| ____   _____/  |_  ____   __| _/  \    /  \___________|  | _|__| ____    ____   /\ "" *")
print("  * ""|   |/    \    |  |/ __ \_/ ___\   __\/ __ \ / __ |\   \/\/   /  _ \_  __ \  |/ /  |/    \  / ___\  \/ "" *")
print("  * ""|   |   |  \   |  \  ___/\  \___|  | \  ___// /_/ | \        (  <_> )  | \/    <|  |   |  \/ /_/  > /\ "" *")
print("  * ""|___|___|  /\__|  |\___  >\___  >__|  \___  >____ |  \__/\  / \____/|__|  |__|_ \__|___|  /\___  /  )/ "" *")
print("  * ""         \/\______|    \/     \/          \/     \/       \/                   \/       \//_____/      "" *")
print("  * ""                                                                                                       "" *")
print("  * " ".InjectedWorking 0.0.1""                                                                                 "" *")
print("  ***********************************************************************************************************")
print("")


def building():
    user=input("Ingrese su usuario: ")
    contra=input("Ingrese su contraseña de usuario: ")
    print("")

    while user != "admin" or contra != "admin":
        print("Contraseña o usuario incorrecto")
        return building()

    salir=False
    time.sleep(3)
    while not salir:
        print("CHOOSE OPTIONS")
        print("---------------")
        print("1. DESKTOP OFF")
        print("2. MultiSpam Whatsappp - Resolution(1920x1080) and Other Resolution is off")
        print("3. INFORMACION")
        print("4. SALIR")
        print("-------------------")
        opcion= int(input("Ingrese un numero para ejecutarlo: "))
        if opcion == 1:
            time.sleep(2)
            print("Wait for runing...")
            input("")
            time.sleep(3)
            pyautogui.alert("executed successfully")
            pyautogui.press("Win")
            pyautogui.write("cmd")
            pyautogui.press("ENTER")
            pyautogui.alert("Accept for run")
            pyautogui.write("shutdown /r")
            pyautogui.press("enter")       
            salir=True
        elif opcion==2:
            pyautogui.alert("Solo funciona si se muestra en tu Whatsapp o si lo tienes agendado")
            time.sleep(2)
            lista = []
            while True:
                numero = float(input("Ingresa un número y para terminar ingresa -1: "))
                if numero >= 0:
                    lista.append(numero)
                else:
                    break
            print(lista)
            publicidad= str(input("Escribe su publicidad para hacer el spam: "))
            time.sleep(2)
            pyautogui.alert("successfully ejecuted 0.0.1")
            time.sleep(1)
            pyautogui.alert("Abre tu whatsapp - No cierres esto mientras no hayas abierto tu Whatsapp")
            time.sleep(2)
            for listas in range(len(lista)):
                time.sleep(3)
                pyautogui.moveTo(310,200,duration=0)
                pyautogui.click()
                pyautogui.write(str(int(lista[listas])))
                pyautogui.press("ENTER")
                pyautogui.write(publicidad)
                pyautogui.press("ENTER")
            salir=True
        elif opcion==3:
            time.sleep(1)
            print("")
            print("------------------------------------------------------")
            print("TODAS LAS OPCIONES FUNCIONAN BIEN. ENJOIT :3 ")
            print("-----------------------------------------------------")
            print("")
            input()
            salir=True
        elif opcion==4:
            salir=True
building()



