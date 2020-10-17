import json
from difflib import get_close_matches

dictionary_data = json.load(open("data.json"))
lis=[]
def get_the_meaning(word):
	word=word.lower()
	if word in dictionary_data:
		lis.append(word)
		lis.append(dictionary_data[word])
		return dictionary_data[word]
	elif len(get_close_matches(word,dictionary_data.keys()))>0:
		closest_match = get_close_matches(word,dictionary_data.keys())[0]
		is_this_match = input("Did you mean "+closest_match+" ?? TYPE Y OR N :")
		is_this_match=is_this_match.upper()
		if(is_this_match=="Y"):
			lis.append(closest_match)
			lis.append(dictionary_data[closest_match])
			return dictionary_data[closest_match]
		else:
			print("We could not process your request at the moment please enter another word")
			return "no"
	else:
		print("We could not process your request at the moment please enter another word")
		return "no"

flag = True
num_of_words=0

while(flag):
	types_of_no=["N","NO"]
	num_of_words+=1
	print()
	word = input("Enter the word you want to get the meaning for :")
	word_meaning = get_the_meaning(word)
	if word_meaning == type(str):
		word_meaning=word_meaning.upper()
	if word_meaning not in types_of_no:
		print()
		print("THE WORD ENTERED IS: "+word)
		print()
		print("The meaning of the word you are looking for is: ")
		if type(word_meaning)==list:
			for it in word_meaning:
				print(it," ")
	print()
	print()
	again = input("\n\nDo you want to search for the meaning of another word??\nTYPE Y or N : ")
	again=again.upper()
	if again == "Y":
		flag = True
	else:
		flag = False

	if flag==False:
		print()
		print()
		print("You have searched for "+str(num_of_words)+" words and thier meanings today!!!")
		print()
		print("They are:  ")
		print("----------------------------")
		for i in lis:
				if type(i)==type(" "):
					print(i.upper())
					print()
					continue

				for item in i:
					print(item," ")
				print("----------------------------")
		print()
		print("THANKS FOR USING THIS INTERACTIVE DICTIONARY!! :)")
		print("COME BACK SOON")
		break;
	
		


