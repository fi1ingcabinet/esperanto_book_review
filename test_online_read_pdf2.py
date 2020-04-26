'''

The open pdf was copied from here: https://stackoverflow.com/questions/55767511/how-to-extract-text-from-pdf-in-python-3-7-3

'''
import pdfplumber
from os import listdir
from os.path import isfile, join
import string

#function to list a bunch of file names in a list (this is where a load of books are stored)
def list_books_from_dir(path):
   onlyfiles = listdir(path)
   #print(onlyfiles)
   return(onlyfiles)


#Function to output the number of words, unique words, and pages in a book
def count_words_in_book(path):
    try:
        #print("here3")
        pdf = pdfplumber.open(path)
        #print("hGere1")

        #WANT THE result array to look like [ [<title>, <num words total>, <num words unique> ] , [ <title 2>, <num words total 2>, <num words unique 2> ], [...], ... ]
        result_array = []

        num_words = 0
        unique_words = []

        for i in range(1, len(pdf.pages)):
            #print("here2")
            page = pdf.pages[i]
            text = page.extract_text()
            #text.replace("\\n"," ")

            if text == "":
                pass
            else: 
                #REMOVE ALL PUNCTUATION
                try:
                    text = text.translate(str.maketrans('', '', string.punctuation))
                    text = text.replace('"','')
                    text = text.replace("'","")
                    text = text.replace("”","")
                    #print(text)
                    #CREATE A LIST OF ALL OF THE WORDS
                    text2 = text.split(" ")
  
                    #for k in range(0,len(text2)):
                    #   text2[k].replace("\n"," ")
                    text3 = []
  
                    for k in range(0,len(text2)):
                       text2[k] = text2[k].replace("\n"," ")
                    for j in text2:
                       for k in j.split(" "):
                          text3.append(k)
                    '''      
                    if i == 7:
                       print("\n",text3)
  
                    if i == 5:
                       print(text)
                       print("\n",text2)
                       print("\n",text3)
                    '''
  
                    for j in text3:
                       if j not in unique_words:
                          unique_words.append(j)
  
                    #if i == 7:
                    #   print(unique_words)
  



                    #COUNT THE NUMBER OF SPACES TO GET THE NUMBER OF WORDS
                    #print(type(text))
                    count = 0
                    for j in text:
                       if(j.isspace()):
                          count=count+1
                    num_words = num_words + count
  
                    element = [num_words]
                    #print(len(unique_words))
                except:
                    #print(i)
                    pass
        
        
        
        pdf.close()
  
        result_array.append([[element],[len(unique_words)],[len(pdf.pages)]])
  
        return result_array
            
            
    except Exception as e:
        print("here")
        print(path)
        print(e)
'''
#To do a list of books:
books = list_books_from_dir("/users/petercurrie/Desktop/stuff/memory/esperanto")
#words = count_words_in_book("/users/petercurrie/Desktop/stuff/memory/esperanto/eo - bronte, charlotte - jane eyre 2.pdf")

for i in range(1,1000):
   filepath = "/users/petercurrie/Desktop/stuff/memory/esperanto/" + books[i]
   num_words = count_words_in_book(filepath)
   print(books[i], num_words)
'''
#To do a specific book:
filepath = "/users/petercurrie/Desktop/stuff/memory/esperanto/eo - carroll, lewis - la aventuroj de alico en mirlando.pdf"
num_words = count_words_in_book(filepath)
print(filepath, num_words)


