print("This program takes in a CFG, then creates the CYK table for test strings")
print("one at a time and returns whether they can be made by the given CFG or not.\n")

productions = {}

print("Please enter the production rules for your CFG here.")
print("Ensure all terminals are only one character long, and that all rules are in CNF.\n")
inputChoice = int(input("Enter 1 to get productions from a file, or 2 to manually enter: "))
while((inputChoice != 1) and (inputChoice != 2)):
    inputChoice = int(input("Invalid input: Please enter either 1 or 2: "))

if(inputChoice == 1):
    fileName = input("Please enter the name of the file: ")
    inFile = open(fileName, 'r')
    startLine = 0
    for line in inFile:
        if(startLine == 0):
            startVar = line.strip(" ").strip("\n")
            startLine = 1
        else:
            parts = line.split("->")
            var = parts[0].strip(" ")
            results = parts[1].split("|")
            for i in range(len(results)):
                results[i]=results[i].strip(" ").strip()
            for i in results:
                if(i in productions):
                    temp = productions.get(i)
                    if(not(var in temp)):
                        temp.add(var)
                        productions[i]=temp
                else:
                    productions[i]=set(var)
else:
    startVar = input("Please enter the letter for the start variable: ")
    userIn = input("Enter a production rule in the form A -> B|C|d or \"done\": ")
    while(userIn != "done"):
        parts = userIn.split("->")
        var = parts[0].strip(" ")
        results = parts[1].split("|")
        for i in range(len(results)):
            results[i]=results[i].strip(" ").strip("\n")
        for i in results:
            if(i in productions):
                temp = productions.get(i)
                if(not(var in temp)):
                    temp.add(var)
                    productions[i]=temp
            else:
                productions[i]=set(var)
        userIn = input("Enter a production rule in the form A -> B|C|d or \"done\": ")

for key in productions:
    productions[key] = frozenset(productions[key])

print("\nEnter a .csv file name to write the CYK results to.")
outFileName = input("WARNING: If the file already exists, it will be overwritten: ")
outFile = open(outFileName,'w')

testString = input("Enter the string to test or \"done\" : ")
while(testString != "done"):
    a = [[set() for x in range(len(testString)-y)] for y in range(len(testString))]
    for i in range(0,len(testString)):
        for j in range(len(testString)-i):
            if(i == 0):
                a[i][j] = productions.get(testString[j])
            else:
                colX = j
                colY = i-1
                checkX = j+i
                checkY = 0
                while colY >= 0:
                    for k in a[colY][colX]:
                        for l in a[checkY][checkX]:
                            if(((k+l) in productions) and (productions[k+l] not in a[i][j])):
                                for m in productions[k+l]:
                                    a[i][j].add(m)
                    colY-=1
                    checkX-=1
                    checkY+=1

    for i in range(len(testString)-1,-1,-1):
        for j in range(len(testString)-i):
            outFile.write("\"")
            index = 0
            if(len(a[i][j]) == 0):
                outFile.write("N/A")
                outFile.write("\",")
            else:
                for k in a[i][j]:
                    if(index == 0):
                        outFile.write(k)
                    else:
                        outFile.write(","+k)
                    index += 1
                outFile.write("\",")
        outFile.write("\n")
    for i in range(len(testString)):
        if (i == 0):
            outFile.write(testString[i])
        else:
            outFile.write(","+testString[i])
    outFile.write("\n\n")

    if(startVar in a[len(testString)-1][0]):
        print(testString+" is accepted by the given CFG.")
    else:
        print(testString+" is not accepted by the given CFG.")
    
    testString = input("Enter another string to test or \"done\" : ")
outFile.close()
