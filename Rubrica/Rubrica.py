#!/bin/env python

class Voce ( object ) :
    def __init__( self ) :
        nome = ""
        cognome = ""
        telefono = ""

class Rubrica( object ) :
    def __init__ ( self ) :
        self.nome_rubrica = ""
        self.voci = []
        self.lunghezza = 0

    """ imposta il nome della rubrica """
    def rubrica( self, nome ):
        self.nome_rubrica= nome
        pass

    """ inserisce una nuova voce nella rubrica """
    def aggiungi ( self, nome, cognome, numero ) :
        #TODO : scrivere una funzione che istanzi un nuovo oggetto voce e che lo aggiunga all'elenco
        pass

    """  restituisce la prima voce inserita nella rubrica come stringa """
    def primo ( self ) :
        #TODO : scrivere una funzione che ritorna il primo elemento nella rubrica sotto forma di stringa , oppure se la rubrica e vuota un messaggio
        return ""

    """ ritorna il nome della rubrica """
    def nome( self ):
        return self.nome_rubrica

    """  Restituisce la voce i-esima inserita nella rubrica """
    def voce ( self, i ) :
        #todo
        return ""

    """  Restituisce una stringa con l'elenco delle voci  della rubrica separate da ", ". L'elenco inizia con '(' e termina con ')' """
    def elenco ( self ):
        #todo
        return ""

    """ Restituisce la stringa con la prima voce che  contiene il parametro daCercare come nome,  cognome oppure telefono."""
    def ricerca ( self, token ) :
        #todo
        return ""
