inFile1 = open(r'data\factbook.csv','r')
inFile2 = open(r'data\factbook-2.csv','r')

outFile = open(r'temp\temp.csv','w')

listLines = []

for line in inFile1:

    if line in listLines:
        continue

    else:
        outFile.write(line)
        listLines.append(line)

for line in inFile2:

    if line in listLines:
        continue

    else:
        outFile.write(line)
        listLines.append(line)

outFile.close()

inFile2.close()
inFile1.close()