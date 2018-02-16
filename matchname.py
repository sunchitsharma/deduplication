def namematch(name1,name2):
    nd1=name1.split()
    nd2=name2.split()

    if(len(nd1)>len(nd2)):
        longname = nd1
        shortname = nd2
    else:
        longname = nd2
        shortname = nd1

    match = 0
    for i in shortname:
        for j in longname:
            if i==j or len(i)==1 and str(i)==j[0] or len(j)==1 and str(j)==i[0]:
                match = match+1
                longname[longname.index(j)]="XXXX"
                break
            elif j == longname[-1]:
                return False
    if match !=0:
        return True
    else:
        return False

######## TEST CODE ########
#print namematch("Vladimir Antonio Frometa Garo","Vladimir Frometa G")
