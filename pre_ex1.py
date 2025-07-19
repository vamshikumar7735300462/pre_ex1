from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords 
txt="Any person who comes in the store today is eligible for the discount. offert at the eand"
lower_case=txt.lower()
tokenize_word=word_tokenize(txt)
tokenize_sent=sent_tokenize(txt)
print("word tokenize =:",tokenize_word)
print("sent tokenize :",tokenize_sent)
stop_words=stopwords.words("english")
print(stop_words)
print("*"*50)
lst=[]
for i in tokenize_word:
    if i in stop_words:
        lst.append(i)
print(lst)