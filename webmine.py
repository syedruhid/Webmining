f1=open( r"C:\Users\Asus\Desktop\digital.txt" ) 
paragraphs = f1.read() 

f2 = open( r"C:\Users\Asus\Desktop\departed.txt" ) 
sentence = f2.read() 

 
   

import nltk
nltk.download('punkt') 
import re
sentence_without_punc = re.sub( r'[^\w\s]' , '' ,sentence)
paragraph_without_punc =re.sub( r'[^\w\s]' , '' ,paragraphs)
print(" \n ")
print("Sentence without the pucntuation marks")
print(" \n ")
print(sentence_without_punc)
print(" \n ")
print("Paragraph without the pucntuation marks")
print(" \n ")
print(paragraph_without_punc)

from nltk.tokenize import word_tokenize
tokenized_sentence = word_tokenize(sentence_without_punc)
tokenized_paragraph = word_tokenize(paragraph_without_punc)
print(tokenized_sentence) 
print( '\n' )
print(tokenized_paragraph) 
print( '\n' )

import nltk 
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words_nltk = stopwords.words( 'english' )
print(stop_words_nltk)

no_stopwords_sentence = [m for m in tokenized_sentence if not m in stop_words_nltk ]
no_stopwords_paragraph = [n for n in tokenized_paragraph if not n in stop_words_nltk ]
print(no_stopwords_sentence) 
print( '\n' )
print(no_stopwords_paragraph) 
print( '\n' )
print( '\n' )
print( '\n' )

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
stemmed_sentence = []
stemmed_paragraph =[]
for word_nltk1 in no_stopwords_sentence:
    stemmed_sentence.append(stemmer.stem(word_nltk1))
for word_nltk2 in no_stopwords_paragraph:
    stemmed_paragraph.append(stemmer.stem(word_nltk2))
print('stemmed_sentence: \n') 
print(stemmed_sentence) 
print( '\n' )
print('stemmed_paragraph: \n') 
print(stemmed_paragraph) 
print( '\n' )
print( '\n' )
print( '\n' )

from collections import Counter
final_sentence = Counter(stemmed_sentence)
final_paragraph = Counter(stemmed_paragraph)
print( "Initial sentence: " +sentence)
print( '\n Final sentence: \n' )
print(final_sentence)
print( '\n' )
print( "Initial paragraph: " +paragraphs)
print( '\n Final paragraph : \n' )
print(final_paragraph)
print( '\n' )

