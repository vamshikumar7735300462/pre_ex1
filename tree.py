from nltk.tokenize import word_tokenize
from nltk import pos_tag,ne_chunk
import re
txt="This is the best chance to change your self and your life .this time you leave nevar win"
lk=txt.lower()
r=re.sub("THIS","woke",lk)

t=word_tokenize(r)
print
