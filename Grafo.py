'''Grafo implementado con programación funcional, se muestra un menú de opciones para ejecutar cada función'''
from functools import reduce

def newGrafo():
    return {}

def newVertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice]=[]
    return grafo

def newArista(grafo, vInicial, vFinal):
    if vInicial in grafo:
        grafo[vInicial].append(vFinal)
    else:
        grafo[vInicial]=[vFinal]

    return grafo

def delete_vertice(grafo, vertice):
    if vertice in grafo:
        del grafo[vertice]
        for v in grafo:
            grafo[v]=[x for x in grafo[v] if x != vertice]
    return grafo

def delete_arista(grafo, vInicial, vFinal):
    if vInicial in grafo and vFinal in grafo[vInicial]:
        grafo[vInicial].remove(vFinal)
    return grafo

def get_vertice(grafo):
    return list(grafo.keys())

def get_arista(grafo):
    arista=[(vInicial, vFinal) for vInicial in grafo for vFinal in grafo[vInicial]]
    return arista


def invertir_grafo(grafo):
    inverted_grafo=newGrafo()
    for vInicial in grafo:
        for vFinal in grafo[vInicial]:
            newArista(inverted_grafo, vFinal, vInicial)
    return inverted_grafo

def sucesores(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    return []

def antecesores(grafo, vertice):
    antecesores=[v for v in grafo if vertice in grafo[v]]
    return antecesores

def show_grafo(grafo):
    for vertice in grafo:
        print(f"{vertice}: {', '.join(grafo[vertice])}")


'''grafo=newGrafo()
grafo=newVertice(grafo, "A")
grafo=newVertice(grafo, "B")
grafo=newVertice(grafo, "C")
grafo=newVertice(grafo, "D")

grafo=newArista(grafo, "A", "C")
grafo=newArista(grafo, "B", "C")
grafo=newArista(grafo,"C", "D")
grafo=newArista(grafo,"B", "A")
print("Grafo\n", grafo) 
'''

def show_menu():
    print("1. Crear vertice")
    print("2. Crear arista")
    print("3. Eliminar vertice")
    print("4. Eliminar arista")
    print("5. Obtener vertice")
    print("6. Obtener arista")
    print("7. Invertir grafo")
    print("8. Sucesores del vertice")
    print("9. Antecesores del vertice")
    print("10. Mostrar grafo")
    print("11. Salir")

    return input("Seleccione una opción: ")


def main():
    grafo=newGrafo()

    while True:
        opcion = show_menu()

        if opcion == '1':
            vertice = input("Ingrese el nuevo vertice: ")
            grafo = newVertice(grafo, vertice)
        
        elif opcion == '2':
            vInicial = input("Ingrese el vertice inicial: ")
            vFinal = input("Ingrese el vertice final: ")
            grafo = newArista(grafo,vInicial,vFinal)

        elif opcion == '3':
          vertice = input("Ingrese el nombre del vértice a eliminar: ")
          grafo = delete_vertice(grafo, vertice)  

        elif opcion == '4':
            vInicial = input("Ingrese el nombre del vértice de origen: ")
            vFinal = input("Ingrese el nombre del vértice de destino: ")
            grafo = delete_arista(grafo, vInicial, vFinal)

        elif opcion == '5':
            vertice = get_vertice(grafo)
            print("Vertice: ", vertice)

        elif opcion =='6':
            arista = get_arista(grafo)
            print("Arista: ", arista)

        elif opcion == '7':
            grafo_invertido = invertir_grafo
            print("El grafo invertido es: ", grafo_invertido)

        elif opcion == '8':
            vertice = input("Ingrese el nombre del vértice: ")
            sucesores_vertice = sucesores(grafo, vertice)
            print("Los sucesores de ", vertice + "son: ", sucesores_vertice)

        elif opcion == '9':
            vertice = input("Ingrese el nombre del vértice: ")
            antecesores_vertice = antecesores(grafo, vertice)
            print("Los antecesores de ", vertice + "son: ", antecesores_vertice)

        elif opcion == '10':
            show_grafo(grafo)

        elif opcion == '11':
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()

