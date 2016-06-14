from nltk.corpus import opinion_lexicon
from nltk.corpus import wordnet as wn
import sys
import random

from senticnet.senticnet import Senticnet
sn = Senticnet()
word=opinion_lexicon.words()
#sys.stdout=open("disagree_2_a_1.txt","w")

def display_concept(w):
	sentics=sn.sentics(w)
	flag=0
	sys.stdout.write(w)
	sys.stdout.write("=[")
	if sn.polarity(w) > 0:
		sen=['#joyful','#interesting','#surprising','#admirable']
		if (sentics['pleasantness']>0):
			sys.stdout.write("#joyful,")
			flag=flag+1
			sen.remove('#joyful')
		if (sentics['attention']>0):
			sys.stdout.write("#interesting,")
			flag=flag+1
			sen.remove('#interesting')
		if (sentics['attention']<0):
			if flag<2:
				sys.stdout.write("#surprising,")
				flag=flag+1
				sen.remove('#surprising')
		if (sentics['aptitude']>0):
			if flag<2:
				sys.stdout.write("#admirable,")
				flag=flag+1
				sen.remove('#admirable')

		while flag<2:
			val=random.sample(sen,1)
			for v in val:
				sys.stdout.write(v)
				sys.stdout.write(",")
				sen.remove(v)
			flag=flag+1

	if sn.polarity(w) < 0:
		sen=['#sad','#scared','#angry','#disgusting']
		if (sentics['pleasantness']<0):
			sys.stdout.write("#sad,")
			flag=flag+1
			sen.remove('#sad')
		if (sentics['sensitivity']<0):
			sys.stdout.write("#scared,")
			flag=flag+1
			sen.remove('#scared')
		if (sentics['sensitivity']>0):
			if flag<2:
				sys.stdout.write("#angry,")
				flag=flag+1
				sen.remove('#angry')
		if (sentics['aptitude']<0):
			if flag<2:
				sys.stdout.write("#disgusting,")
				flag=flag+1
				sen.remove('#disgusting')
		while flag<2:
			val=random.sample(sen,1)
			for v in val:
				sys.stdout.write(v)
				sys.stdout.write(",")
				sen.remove(v)
			flag=flag+1

	for sem in sn.semantics(w):
		if sem !='semantics':
			sys.stdout.write(sem)
			sys.stdout.write(",")
	sys.stdout.write("]")
		


#with open("senticData.txt") as f:
#	content=f.readlines()

#data = [x.strip('\n') for x in content]

for w in word[0:6788]:
	check=1
	w_pol=sn.polarity(w)
	pol=1
	if w_pol<0:
		pol=-1

	sem=sn.semantics(w)
	for s in sem:
		if s!='semantics':
			if sn.polarity(s)<0:
				s_pol=-1
			else:
				s_pol=1
			if pol!=s_pol:
				check=0

	if check==0:
		display_concept(w)
		print "\n"


