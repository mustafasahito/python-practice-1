def word_counter():
    sentence = input("Enter any sentence: ")
    dicta = {}  # It will store our key-value pairs
    
    for word in sentence.split():  # It will split each word and assign it to 'word'
        dicta[word] = dicta.get(word, 0) + 1  # Increment the count for the word
#syntax of get is "dict.get(key,default value)"
    print("Word counts:", dicta)

word_counter()