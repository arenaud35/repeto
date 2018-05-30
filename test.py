#! /usr/bin/env python3
# coding: utf-8
def montant(nombre):
	repeter = messageacopier()
	texte = nombre * repeter
	print (texte)



def messageacopier():
	message=input("entrer le message")
	if len(message)>5:
		return "trop long"
	Else:
		return message
