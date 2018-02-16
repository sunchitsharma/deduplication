import matchname as mn
import readfile as rf

f_name = raw_input("Enter The Dataset Name : ")
n_list = rf.fileread(f_name)

finaldict = {}

## DICT {M{DOB1:[[FN1 , SN1],[FN2 , SN2]]    DOB2:[[FN3 , SN3],[FN4 , SN4]]}

for i in n_list:
    if i[2] in finaldict.keys(): # eg : M exist <MAIN>

        if i[1] in finaldict[i[2]].keys(): # eg : in M DOB1 exists <SECOND>
            match = 0
            for j in finaldict[i[2]][i[1]]:
                if(mn.namematch(i[3],j[0]) and mn.namematch(i[0],j[1])):
                    match = 1
                    break
            if(match == 0): # M existed , DOB existed but no match
                finaldict[i[2]][i[1]].append([i[3],i[0]])
            else: # Found a match
                pass

        else : # <SECOND> if DOB DOES NOT EXIST IN LIST
            finaldict[i[2]][i[1]]=[[i[3],i[0]]]

    else: # <MAIN> if M does not exist
        finaldict[i[2]]={i[1]:[[i[3],i[0]]]}

for i in finaldict:
    for j in finaldict[i]:
        for k in finaldict[i][j]:
            print k[0]+" "+k[1]+" \t\t BORN ON : "+j+" \t GENDER : "+ i
