import re
def fileread(name_of_file):
    f=None
    try:
        f= open(name_of_file,"r")
    except:
        print " Sorry Enter a valid file name "
        exit(0)

    dicdata=[]
    strdata = f.readlines()
    strdata=re.split(",|\r",strdata[0])
    #print strdata
    answer=[]
    temp=[]
    for i in range(0,len(strdata)):

        if i==0:
            temp.append(strdata[i])
        elif(i%4==0):
            answer.append(temp)
            temp=[]
            temp.append(strdata[i])
        else:
            temp.append(strdata[i])

    del answer[0]

    answer.append(temp)

    return answer



######## TEST CODE ########
#fileread("dataset.csv")
