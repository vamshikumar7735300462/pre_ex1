from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
txt="Any person who comes  the store today eligible the discount. offert at the eand"
word_tokenize=word_tokenize(txt)
for word in word_tokenize:
    print(PorterStemmer().stem(word),"//",WordNetLemmatizer().lemmatize(word))