from datetime import date
import os
import time

lista_tarea = []

#complicadaso

def agregar_tarea():
    descripcion = input("Ingrese una tarea: ")

    tarea = {"descripcion": descripcion,
       "fecha": date.today().strftime("%d-%m-%y"),
        "completada": False}
    
    lista_tarea.append(tarea)
    print("La tarea", descripcion, "ha sido agregada a la lista")

def listar_tarea():
    print("Lista de tareas:")
    abcd = 0
    for aa in lista_tarea:
        print(abcd, aa)
        abcd += 1

def eliminar_tarea():
    listar_tarea()
    eliminar = int(input("Eliminar la tarea: "))
    lista_tarea.pop(eliminar)
    print("La tarea ha sido eliminada de la lista")

def completar_tarea():
    listar_tarea()
    completar = int(input("Completar la tarea: "))
    lista_tarea [completar] ["completada"] = True
    print("La tarea ha sido completada")

def menu():
    funciones = ["Agregar tarea", "Eliminar tarea", "Lista de tareas", "Completar tarea", "Salir" ]
    print("Menu")
    contador = 1
    for opciones in funciones:
        print(contador, opciones)
        contador += 1    
    
def main():
    i=0
    while i==0:
        time.sleep(2)
        os.system("cls")
        menu()
        elegir = int(input("Elija una opcion: "))
        if elegir == 1:
            agregar_tarea()
        elif elegir == 2:
            eliminar_tarea()
        elif elegir == 3:
            listar_tarea()
        elif elegir == 4:
            completar_tarea()
        elif elegir == 5:
            print("chao <3")
            i=2
        else:
            print("Opcion invalida")
        
main()