#!/bin/env python
#
# Testo :
# Scrivere un programma che definisca 3 variabili intere chiamate operand1, operand2 e result, e:
# a) Acquisisca da tastiera il valore di operand1 e operand2 tramite la funzione raw_input
# b) Ne calcoli la somma e la salvi nella variabile result
# c) Visualizzi a video il valore della variabile result utilizzando la funzione print
#
#

def main ( ) :
    operand1 = input ("Valore : ")
    operand2 = input ("Valore : ")
    result = operand1+operand2
    print ( "risultato : "+ str(result) )
    return

if __name__ == "__main__" :
    main( )
