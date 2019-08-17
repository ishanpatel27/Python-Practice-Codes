#__author__ = "ISHAN PATEL"
#__version__ = "3.5.2"
#__email__ = "ishanpatel415@gmail.com"
# Program for Room_number ( assignment for n gram)
try:
     open_gram=open("abc.txt","r")                                              
     no=int(input("Enter the no. of grams to be done:"))
     ngrams=[]
     for delination in open_gram:
             for i in range(len(delination.split()) - no+1):
                     ngrams.append(delination.split()[i:i + no])
             for grams in ngrams:
                     print(" ".join(grams))
except FileNotFoundError:
    print("File Not Found")
except ValueError:
    print("Enter correct data ")

# end 

'''
*** this can be directly done by
from nltk import ngrams

open_gram=open("abc.txt","r")
n=int(input("Enter the no. of grams to be done:"))
for sentence in open_gram:
            sixgrams = ngrams(sentence.split(), n)
            for grams in sixgrams:
                  print (grams)
'''
