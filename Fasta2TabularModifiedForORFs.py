def FastaToTabular (SourceFile, ResultFile):
    fr=open(SourceFile, "r").read().split()
    fw = open(ResultFile, "w")
    mylist=[]

    for item in fr:
        item=str(item)
        item=item.rstrip()
        mylist.append(item)
    for i in mylist:
        if i[0]==">":
            if i[-2]=="_":
                fw.write("\n"+i[0:-2]+"\t")
            if i[-3]=="_":
                fw.write("\n"+i[0:-3]+"\t")
        elif i [0].isupper() and ")" not in i:
        #elif i [0]!=" " or i [0]!= ">" or i [0]!= "[" or i [0]!= "(" or i [0]!= "l":
        #elif i[0]=="A"or i[0]=="A"or i[0]=="G"or i[0]=="T"or i[0]=="C":
            fw.write(i)
        else: continue
FastaToTabular("Galaxy207-[getorf_on_data_191].fasta", "Galaxy207-[getorf_on_data_191].txt")