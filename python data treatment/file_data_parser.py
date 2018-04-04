def splitLineInFiles(input, separator = None) :
    """
    split file each file line into a different file
    """
    with open(input, encoding="utf-8") as inputF :
        i = 0
        for line in inputF :
            if separator : output = line.split(separator)[0]+".txt"
            else : output = input+str(i)+".txt"
            with open(output,'w',encoding="utf-8") as outputF :
                outputF.write(line)

splitLineInFiles("finalData.txt", ",")