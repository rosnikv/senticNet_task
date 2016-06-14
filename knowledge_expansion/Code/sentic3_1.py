import re
from nltk.corpus import wordnet as wn
import sys
import random
from itertools import product
import heapq
#from senticnet.senticnet import Senticnet
#sn = Senticnet()
sys.stdout=open("sentic_out3_1.txt","w")

def get_emotion(word):
	list1=[]
	list2=["sad","scared","angry","disgusting"]
	list1.append(word)
	allsyns1 = set(ss for word in list1 for ss in wn.synsets(word))
	allsyns2 = set(ss for word in list2 for ss in wn.synsets(word))
	best = heapq.nlargest(2,((wn.wup_similarity(s1, s2) or 0, s1, s2) for s1, s2 in product(allsyns1, allsyns2)))

	scared_syn=["frighten","daunt","scar","frightened"]
	sad_syn=["sad","deplorable"]
	angry_syn=["angry"]
	disgust_syn=["disgust","disgusting"]
	mood=[]

	if len(best)==2:
		if  best[0][2].name().split(".")[0] in scared_syn:
			if "#scared" not in mood:
				mood.append("#scared,")
		elif best[0][2].name().split(".")[0] in sad_syn:
			if "#sad" not in mood:
				mood.append("#sad,")
		elif best[0][2].name().split(".")[0] in angry_syn:
			if "#angry" not in mood:
				mood.append("#angry,")
		else:
			if "#disgusting" not in mood:
				mood.append("#disgusting,")

		if  best[1][2].name().split(".")[0] in scared_syn:
			if "#scared" not in mood:
				mood.append("#scared,")
		elif best[1][2].name().split(".")[0] in sad_syn:
			if "#sad" not in mood:
				mood.append("#sad,")
		elif best[1][2].name().split(".")[0] in angry_syn:
			if "#angry" not in mood:
				mood.append("#angry,")
		else:
			if "#disgusting" not in mood:
				mood.append("#disgusting,")

		mood=list(set(mood))
		while len(mood)<2 :
			temp=["#sad,","#scared,","#angry,","#disgusting,"]
			for v in mood:
				temp.remove(v)
			val=random.sample(temp,1)
			for v in val:
				mood.append(v)
	
		for i in mood:
			sys.stdout.write(i)
	
		del mood[:]
		return 1
	
	else:
		return 0


from urllib2 import Request, urlopen, URLError
url="http://conceptnet5.media.mit.edu/data/5.4/c/en/"

with open("new_concepts_negative.txt","r") as f:
	content=f.readlines()

#word="allegation"
for word in content:
	check=url+word
	op=Request(check)
	op2=urlopen(op)
	l=op2.read()
	data=re.findall(r'\"end\": \"/c/en/[a-z].+[/_].+[a-z].+\"',l)
	concepts=[]
	for i in data:
		sem1=i.split("/")
		if sem1[3]!=word and sem1[3] not in concepts:
			concepts.append(sem1[3])
		else:
			if len(sem1)>=5:
				if sem1[5] not in concepts:
					concepts.append(sem1[5])

	
	if len(concepts)>=2:
		count=len(concepts)
		for w in concepts:
			if count>=6:
				break
			if "_" not in w and w!=word:
				for syn in wn.synsets(w):
					for l in syn.lemmas():
  						if l.name()!=w:
  						#	print l.name()
  							concepts.append(l.name())
  				count=len(concepts)
 # 	print "**START**"
 #	concepts=list(set(concepts))
 	seen = set()
 	seen.add(word.strip())
	result = []
	for item in concepts:
		if item not in seen:
			seen.add(item)
			result.append(item)


	if len(result)>=5:
		sys.stdout.write(word.strip())
  		sys.stdout.write("=[")
  		flag=get_emotion(word.strip())
  		if flag:
	  		sc=1
			for i in result:
				if i!=word:
					sys.stdout.write(i)
					sys.stdout.write(",")
					sc=sc+1
				if sc>5:
					break

			print "]\n"	
#	print "**END**"

		del concepts[:]
		del result[:]
