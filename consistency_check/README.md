2. CONSISTENCY CHECK
Finding errors in SenticNet, e.g., in terms of polarity or semantics.

a) Polarity check
1) find all concepts on which SenticNet and other lexicons disagree (i.e., for which they have different polarity)
2) shortlist only the ones for which SenticNet is wrong

b) Semantics check
1) find SenticNet concepts that present problematic semantics, e.g., semantics that are not related to the entry concept or semantics that have different polarities
2) propose new semantics for that entry

___________________________________________________________________________________________________________


Code Directory
|
--> polarity_check.py   : make use of opinion lexicon, list out the concepts having different polarities in 	                          senticnet and opinion_lexicon


output_Data Directory
|
--> polarity_check.txt  : Output data in sentic vector format


Code Directory
|
--> semantics_check.py  : make use of senticData.txt (concepts extracted from senticnet)



output_Data Directory
|
--> semantics_check.txt  : Output data in sentic vector format, concepts having semantics with
                           different polarity.


Code Directory
|
--> new_semantics.py  : make use of senticdata.txt (concepts extracted from problematic semantics data)



output_Data Directory
|
--> new_semantics.txt  : Output data in sentic vector format, concepts having new semantics from
                          wordnet (if available) with same polarity.
