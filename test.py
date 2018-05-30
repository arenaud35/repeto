
def montant(nombre):
	repeter = messageacopier(nombre)
	texte = nombre * repeter
	print (texte)



def messageacopier(nombre):
	message=selection_message(nombre)
	if len(message)>5:
		return "trop long ! "
	else:
		return message
 
def selection_message(nombre):
	ma_list=["Bla","Bouh","Zut"]
	if nombre<4 and nombre>0:
		return ma_list[nombre-1]
	else:
		return "ça va être trop long"
