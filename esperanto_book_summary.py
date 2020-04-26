
'''
Want to do this:

1. List all the files in a directory (this is where all the books are)
2. Get the name of the files as the "title" in the list
3. For each book count the number of words and add that to "num words"
4. For each book count the number of unique words and add that to "unique words"
5. For each book get the longest word and shortest word and average word length
6. For each book get the average sentence length

'''

# Part 1: get a list of all the files 
import PyPDF2
from os import listdir
from os.path import isfile, join
onlyfiles = listdir("/users/petercurrie/Desktop/stuff/memory/esperanto")
#print(onlyfiles)


f = open("/users/petercurrie/Desktop/stuff/memory/esperanto/eo - bronte, charlotte - jane eyre 2.pdf","rb")

pdfReader = PyPDF2.PdfFileReader(f)
print(pdfReader)
