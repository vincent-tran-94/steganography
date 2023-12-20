import string

"""
random.seed() Permet de fixer un nombre aléatoire 
"""

string.printable = string.printable.replace('\r','é')

def caesar_cipher(message, key):
	"""
	this function takes a message and key then it generates a crypted message
	step 0 : verify inputs:  # good
		+ message must be a str
		+ key must be an int
	step 1: define the caesar disc (alphabet) # good
	step 2 : create a list to contain the crypted caracs
	step 3: for loop where we cipher carac by carac the message
	"""
	if type(message) != str:
		raise Exception("The message must be a str")
	if type(key) != int:
		raise Exception("The key must be an int")

	#return "".join([string.printable[(string.printable.index(carac) + key)%len(string.printable)] for carac in message])
	list_of_crypted_caracs = []
	number_caracs_disc = len(string.printable)
	for carac in message:
		# on recherche la position du caractère à chiffrer dans notre disque (string.printable)
		position_carac_in_alphabet = string.printable.index(carac)
		
		# on calcul la position du caractère dans le disque une fois chiffré
		position_crypted_carac = (position_carac_in_alphabet + key) % number_caracs_disc

		# on reccupère le caractère chiffré dans le disque on utilisant sa position calculée à l'étape précédente
		crypted_carac = string.printable[position_crypted_carac]
		
		# on stocke le caractère chiffé dans la liste contenant tous les caractères chiffrés
		list_of_crypted_caracs.append(crypted_carac)

	crypted_message = "".join(list_of_crypted_caracs)
	return crypted_message


def caesar_decrypt(crypted_message, key):
	"""
	on réutilise la fonction de chiffrement, avec un clef négative : 
	cela représente de tourner le disque dans le sens opposé.
	On respecte le principe DRY : don't repeat yourself
	"""
	return caesar_cipher(crypted_message, -key)

def caesar_hacking(crypted_message):
	"""
	Il y a autant de clef que de caractères dans mon disque : (string.printable)
	On utilise toutes les clefs possibles
	"""

	number_of_possible_keys = len(string.printable)
	for possible_key in range(1, number_of_possible_keys):
		print(caesar_decrypt(crypted_message, possible_key))
		print("_"*80)


def viginere_cypher(message,password): 
	"""
	Step 0: Verify the input
	message : must be string
	password must be string
	Step 1: Convert the password into a list of keys
	Step 2: Cipher carac by carac the message using the different keys and will respect DRY"
	using the previous caeser function warning we must manage the case where the password is short the message
	"""
	if type(message) != str:
		raise Exception("The Message must be str")
	if type(password) != str:
		raise Exception("The password must be str")

	list_of_keys = [string.printable.index(carac) for carac in password]
	list_of_crypted_caracs = []
	for index_carac, carac in enumerate(message): 
		current_key = list_of_keys[index_carac % len(list_of_keys)]
		current_crypted_carac = caesar_cipher(carac, current_key)
		list_of_crypted_caracs.append(current_crypted_carac)
		crypted_message = "".join(list_of_crypted_caracs)
	
	return crypted_message

#print(viginere_cypher("coucou les loulous","Azerty12345"))	
#print(caesar_hacking("VN8DKWdqoeyuNGUnJpp"))