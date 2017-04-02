#!/bin/env python

import Rubrica

def main ( ) :
    #definisco il nome della mia nuova rubrica
    r_nome = "rubrica nostra"

    # instanzio la rubrica
    r = Rubrica.Rubrica()

    # configuro il nome della rubrica
    r.rubrica( r_nome )

    # inserisco dei dati nella rubrica
    r.aggiungi("Giovanni", "Bianchi", "123 45 67")
    r.aggiungi("Mario", "Rossi", "321 98 76")
    r.aggiungi("Giuseppe", "Verdi", "456 789 123")


    # stampo il nome della rubrica
    print ( "Nome : " + r.nome())

    # estraggo e stampo il contenuto della prima voce
    prima_voce = r.primo()
    print ( "prima voce : " + prima_voce )

    # estraggo i dati per indice
    voce1 = str ( r.voce(1) )
    voce2 = r.voce(2)
    voce3 = r.voce(3)

    # li stampo
    print ("voce(1) --> " + voce1)
    print ("voce(2) --> " + voce2)
    print ("voce(3) --> " + voce3)

    # stampo l'elenco intero delle voci
    print ("Elenco: " + r.elenco())

    # ricerco "Verdi" allinterno del risultato e lo stampo
    print ("Ricerca 'Verdi': " + r.ricerca("Verdi"))

if __name__ == "__main__" :
    main()