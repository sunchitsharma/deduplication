# deduplication

ABOUT THE PROJECT :

The project aims at deduplication of names in a given dataset.

APPROACH : 

I have used a multilevel clustring approach where the root clusters are on basis on Gender. Inside the gender I have made clusters accroding to date of birth. Whenever I reach a cluster I check of any name in the cluster is a duplation of the current name and if yes, I do not add that name to the cluster else I do add it. 

To check if two names are same or not I have used the following approach :

A name is same as the other name if and only if it follows the following rules:

1) Either it is identical to the other name.
2) Or if the name is multi-word in nature, parts of it may be either reduced to 
	a) The first Letter
	b) A null 

eg : Ram Lal Sharma is same as Ram L Sharma or Ram Sharma.



TO RUN THE PROJECT:

Run the bashfile provided :
Eg : bash runproject.sh

	OR

run the mainfile.py direcltly
Eg : python mainfile.p


