#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string : str) -> bool:
	return True if len(string)%2==0 else False


def get_num_char(string : str, char : str) -> int:
	num_char = 0
	for x in string:
		if x == char:
			num_char+=1
	return num_char


def get_first_part_of_name(name : str) -> str:
	first_name = ""
	for lettre in name:
		ascii_ = ord(lettre)
		if 64<ascii_<91 or 96<ascii_<123:
			first_name+=lettre
		else:
			break
	return first_name


def get_random_sentence(animals : tuple, adjectives : tuple, fruits : tuple) -> list:
	phrases = []
	for x in range(len(animals)):
		phrases.append(f"Le {animals[x]} {adjectives[x]} mange des {fruits[x]}.")
	return phrases

if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
