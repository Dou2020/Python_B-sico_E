def jugar(intento = 1):
    print("\n intento:", intento)
    respuesta = input(" De que color es la fruta?: \n")
    if respuesta != "naranja":
        if intento < 3:
            print("\n fallaste intentalo de nuevo turno:")
            intento += 1
            jugar(intento)
        else:
            print("\n Perdiste")
    else: print("\n Ganaste en el intento:" , intento)
        

pregunta = "si"
print("tienes 3 intentos para adividar cual es color de la fruta")
while pregunta == "si":       
    jugar()
    pregunta = input("deseas Jugar de nuevo?: \n")