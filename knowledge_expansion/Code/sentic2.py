from nltk.corpus import opinion_lexicon
from nltk.corpus import wordnet as wn
import sys
import random

from senticnet.senticnet import Senticnet
sn = Senticnet()

#neg_word=opinion_lexicon.negative()
#pos_word=opinion_lexicon.positive()

with open("senticData.txt") as f:
	content=f.readlines()

data = [x.strip('\n') for x in content]
new_concepts_neg=[]
new_concepts_pos=[]

sys.stdout=open("new_concepts_negative.txt","w")
rem=neg_word[3007]
neg_words=[]
for w in neg_word:
	if w!=rem:
		neg_words.append(w)

for w in neg_words:
	if w not in data:
		new_concepts_neg.append(w)

for w in new_concepts_neg:
	print w

sys.stdout=open("new_concepts_positive.txt","w")

for w in pos_word:
	if w not in data:
		new_concepts_pos.append(w)

for w in new_concepts_pos:
	print w