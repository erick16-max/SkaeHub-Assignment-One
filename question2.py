#find length of the last word in a sentence

str = input("Enter the sentence:")

def last_word_length(str):
    #converting string to list
    li = list(str.split(" "))

    #Get the last item of List
    last_word = li[-1]

    #length of the word
    last_word_length = len(last_word)
    
    return last_word_length


last_word_length = last_word_length(str)
print(f"The length of the last word is {last_word_length}")
    
  