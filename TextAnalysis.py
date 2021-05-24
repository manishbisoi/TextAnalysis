import pandas as pd
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import LineTokenizer
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
import matplotlib.pyplot as plt

lt = LineTokenizer()
ps = PorterStemmer()
lem = WordNetLemmatizer()

stop_words = set(stopwords.words("english"))
#Remove commas, brackets in stemmed_words
unwanted_char = ['1','2','3','4','5','6','7','8','9','0',',','.','?','(',')',':','\'','\"']

f = open("content.txt","r", encoding="utf8")
w = []
for each_line in lt.tokenize(f.read()):
	for line in sent_tokenize(each_line):
		for word in word_tokenize(line):
			if word not in unwanted_char:
				w.append(word.lower())

# w is the list of words in Content.txt
#fdist = FreqDist(w)
#print(fdist.most_common(10))	#prints top 10 most common words
filtered_word = []
for each_wrd in w:
	if each_wrd not in stop_words and each_wrd not in unwanted_char:
		filtered_word.append(lem.lemmatize(each_wrd))


f_dist = FreqDist(filtered_word)
f_dist.plot(10,cumulative=False)
plt.show()
print(f_dist)
