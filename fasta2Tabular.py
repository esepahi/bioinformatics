def FastaToTabular (SourceFile, ResultFile):
    fr=open(SourceFile, "r").read().split() #splits a line to some lines, the other code is readlines() without .split()
    fw = open(ResultFile, "w")
    mylist=[]

    for item in fr:
        item=str(item)
        item=item.rstrip()
        mylist.append(item)
    for i in mylist:
        if i[0]==">":
            fw.write("\n"+i+"\t")
        elif i [0].isupper() and ")" not in i:
        #elif i [0]!=" " or i [0]!= ">":
        #elif i[0]=="A"or i[0]=="A"or i[0]=="G"or i[0]=="T"or i[0]=="C":
            fw.write(i)
        else: continue
FastaToTabular("Galaxy207-[getorf_on_data_191].fasta", "Galaxy207-[getorf_on_data_191].txt")