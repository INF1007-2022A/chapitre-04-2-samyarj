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

def get_random_sentence(animals, adjectives, fruits):
	return ""

def encrypt(text, shift):
	return ""

def decrypt(encrypted_text, shift):
	return ""


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
