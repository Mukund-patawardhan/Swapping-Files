def swapFiles (input1,input2):
    read1 = open(input1,"r")
    read2 = open(input2,"r")
    data1 = read1.read()
    data2 = read2.read()
    write1 = open(input1,"w")
    write2 = open(input2,"w")

    write1.write(data2)
    write2.write(data1)
    
swapFiles("sample1.txt","sample2.txt")