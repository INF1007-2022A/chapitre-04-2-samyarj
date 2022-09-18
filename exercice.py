#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name: str) -> str:
	name = name.lower()
	name = name[0].upper()+name[1::]
	k = int() # detects the position of '-'
	for i in name:
		if i == '-':
			break
		else:
			k+=1
	result= name[:k] # return name until the '-' position
	return result

def get_random_sentence(animals: tuple, adjectives: tuple, fruits: tuple) -> list[str] :
	ran_animal = random.choice(animals)
	ran_adj = random.choice(adjectives)
	ran_fruit = random.choice(fruits)
	List = [ran_animal, ran_adj, ran_fruit] # set of generated random elements of tupples
	sentence = f"Aujourd’hui, j’ai vu un {ran_animal} s’emparer d’un panier {ran_adj} plein de {ran_fruit}."
	return sentence

def encrypt(text: str, shift: int) -> str:
	encrypted = str() # retrun value; all uppercase
	text = text.upper()
	for i in text:
		if 65 <= ord(i) < (90-shift):
			k = ord(i) + shift
			encrypted += chr(k)
		elif (90-shift) <= ord(i) <= 90:
			k = ord(i) - (26-shift)
			encrypted += chr(k)
		else:
			encrypted += i
	return encrypted

def decrypt(encrypted_text: str, shift: int) -> str:
	decrypted = str()

	for i in encrypted_text:
		if (65+shift) <= ord(i) < 90:
			k = ord(i) - shift
			decrypted += chr(k)
		elif 65 <= ord(i) <= (65+shift):
			k = ord(i) + (26-shift)
			decrypted += chr(k)
		else:
			decrypted += i
	return decrypted


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
