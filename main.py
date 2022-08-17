import top10tweets
import topusers

while True:
    print("Que función desea ejecutar?")
    print("1, 2, 3, 4")
    print("0 para salir")
    opcion = input("Opcion: ")
    if opcion == 0:
        break
    elif opcion == 1:
        top10tweets.toptweets()
    elif opcion == 2:
        topusers.topusers()