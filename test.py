#! /usr/bin/env python3
# coding: utf-8
def montant(nombre):
	repeter = messageacopier()
	texte = nombre * repeter
	print texte

message=[]
def messageacopier():
	message=input("entrer le message")
	return message
