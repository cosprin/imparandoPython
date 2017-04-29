#!/bin/env python
#
# Scrivere un programma per il calcolo del modulo di un numero; in particolare il programma dovra':
# a) Acquisire da tastiera un valore intero, positivo o negativo, e memorizzarlo in una
# variabile opportunamente definita
# b) Stabilire utilizzando il costrutto condizionale if se tale variabile contiene un
# valore negativo e, in questo caso, trasformarlo nel corrispondente valore positivo
# c) Stampare a video il valore finale, ovvero il modulo del valore acquisito


def main ( ) :
    x = input ( "Valore : ")
    if int(x) < 0 :
        x = int(x) * -1
    print (x)

    return

if __name__ == "__main__" :
    main()
