from nltk.tokenize import word_tokenize as wt
from nltk.tokenize import sent_tokenize as st
from nltk.corpus import stopwords as sw
text=" Any person who comes in the store today is eligible for the discount. offert at the eand"
tok=wt(text)
sot=st(text)
print("work tokenize",tok)
print("sent tokenize",sot)
s=sw.words("english")
print("stop words",s)
lst=[]
for i in tok:
    if i not in s:
        lst.append(i)
print("after removing stop words",lst)
print("stops words are deleted ",set(tok)-set(lst))