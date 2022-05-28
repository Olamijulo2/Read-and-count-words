# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    openFile = open(filename, "r")
    return(openFile.read()) 
print(read_file_content('story.txt'))


def count_words():
    text = read_file_content('story.txt')
    text=text.lower()
  
    text=text.split(" ")
    
    word_frequency={}

    for i in text:
     
        if i in word_frequency:
            word_frequency[i]+=1
             
        else:
            word_frequency[i]=1
    return(word_frequency)
 
print(count_words())