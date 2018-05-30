#! /usr/bin/env python3
# coding: utf-8
import complement
def montant(nombre):
	repeter = messageacopier(nombre)
	texte = nombre * repeter
	print (texte)



def messageacopier(nombre):
	message=complement.selection_message(nombre)
	if len(message)>5:
		return "trop long ! "
	else:
		return message
 
