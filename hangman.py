"This is a hangman game."

import re
import random
from datetime import datetime

class Hangman:

	def __init__(self,path_to_word_list):
		self.path = path_to_word_list
		self.chances = []
		self.chances_index = 0
		for number in range(1,6):
			self.chances.append("")


	def load_from_file(self):
		with open(self.path,"r") as self.file:
			word_list = self.file.read()
		word_list_array = re.findall(".*\s*",word_list)
		return word_list_array

	def random_word_chooser(self,word_list_array):
		random.seed(datetime.now())
		chosen_index = random.randint(0,len(word_list_array)-2)
		chosen_word = word_list_array[chosen_index]
		self.word_to_guess_by_character = []

		for character in chosen_word:
			if (character == "\n"):
				break
			else:
				self.word_to_guess_by_character.append(character)
		word_size = len(self.word_to_guess_by_character)
		return word_size

	def empty_word_creator(self,word_size):
		self.empty_array = []
		for character in range(0,word_size):
			self.empty_array.append("")

	def give_user_choice(self):
		self.remaining_chances = (len(self.chances) - (self.chances_index + 1))
		#converting the letter_word_list into a word string
		word = ""
		for element in self.word_to_guess_by_character:
			word = word +element
		print(self.empty_array)
		
		letter = input("Enter a letter: ")[0]
		if letter in self.word_to_guess_by_character:
			print("[+] Correct letter chosen!!!!")	
			letter_list = re.findall(letter,str(self.word_to_guess_by_character))
			index_list = []
			for specific_letter in re.finditer(letter,word):
				index_list.append(specific_letter.start())

			counter = 0
			for i in range(0,len(index_list)):
				self.empty_array[index_list[counter]] = letter_list[counter]
				counter = counter + 1
			print(self.empty_array)
		else:
			print("[-] Wrong letter chosen!!!! " + str(self.chances_index + 1) + " chance(s) used up. " + str(self.remaining_chances) + " chance(s) left!!!!" )
			self.chances[self.chances_index] = "X"
			self.chances_index = self.chances_index + 1
			if (self.remaining_chances ==0):
				print("[-] Game over, you lost!!!!")
				print("The word was " + word)
				exit()

	def checker(self):
		if self.empty_array == self.word_to_guess_by_character:
			print ("[+] Congratulations you won the game and had " + str(self.remaining_chances) + " chances remaining.")
			exit()
		else:
			return True

	def start(self):		
		WL = self.load_from_file()
		WS = self.random_word_chooser(WL)
		self.empty_word_creator(WS)
		while True:
			self.give_user_choice()
			self.checker()



game = Hangman("wordz_for_hangman.txt")
game.start()