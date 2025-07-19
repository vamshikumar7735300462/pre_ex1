from nltk.tokenize import word_tokenize
from nltk import pos_tag,ne_chunk
txt="break the sysetem dowan is the procees .the include "
t=ne_chunk(pos_tag(word_tokenize(txt)))
print(t)
# import nltk
# nltk.download('maxent_ne_chunker_tab')