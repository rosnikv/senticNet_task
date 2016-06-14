from nltk.corpus import opinion_lexicon
from nltk.corpus import wordnet as wn
import sys
import random

from senticnet.senticnet import Senticnet
sn = Senticnet()

#sys.stdout=open("disagree_2_a_1.txt","w")

def display_concept(w,new_sem):
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

	
	count=0
	while count <5:
		if w!=new_sem[count]:
			sys.stdout.write(new_sem[count])
			sys.stdout.write(",")
			count=count+1
	sys.stdout.write("]")
		


with open("semdata.txt") as f:
	content=f.readlines()

data = [x.strip('\n') for x in content]

d=[]
for x in data:
	if x!='':
		d.append(x)


	
synonyms = []
for w in d:
	new_semantics=[]
	for syn in wn.synsets(w):
		for l in syn.lemmas():
  			if l.name()!=w:
	       			synonyms.append(l.name())

	synonyms=list(set(synonyms))

	if sn.polarity(w)>0:			
		for s in synonyms:
			if sn.polarity(s)>=0:
				new_semantics.append(s)
	else:
		for s in synonyms:
			if sn.polarity(s)<=0:
				new_semantics.append(s)

	for sem in sn.semantics(w):
		if sem!='semantics':
			if sn.polarity(w)>0:
				if sn.polarity(sem)>0:
					new_semantics.append(sem)
			else:
				if sn.polarity(sem)<0:
					new_semantics.append(sem)

	if len(new_semantics)>4:
		display_concept(w,new_semantics)
		print "\n"
		
	del new_semantics[:]
	del synonyms[:]