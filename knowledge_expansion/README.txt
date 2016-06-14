1. KNOWLEDGE EXPANSION
Enriching SenticNet with new concepts.

Possible ways to do this are:
a) write some code (preferably in python) to import concepts from other sentiment lexicons
b) crowdsourcing, e.g., through surveys, quizzes or games
c) an ensemble of the above


___________________________________________________________________________________________________



Code Directory
   |
   ----> input_data
               |
               ----> senticData.txt   : concepts extracted from senticnet data
               ----> new_concepts_negative.txt : from opinion_lexicon
               ----> new_concepts_positive.txt : from opinion_lexicon
                     (Both generated using Code/sentic2.py)

    |
    ----> sentic2.py : generate input files
    |
    ----> sentic3_1.py : generate output data(sentic_out3_1.txt) contains negative concepts  
    |						make use of conceptnet5.4 db entries, wordnet, opinion_lexicon
    |
    ----> sentic3_2.py : generate output data(sentic_out3_2.txt) contains positive concepts
    						make use of conceptnet5.4 db entries, wordnet, opinion_lexicon


   output_data Directory
         |
         ----> sentic_out3_1.py
         |
         ----> sentic_out3_2.py

