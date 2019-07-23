def dict_length(word_list):

	dict_word = {x:len(x) for x in word_list}
	
	return dict_word

mylist = ["apple", "cat", "book", "CAR", "Dog", "School", "bike"]

print(dict_length(mylist))
