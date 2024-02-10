import random

namesFile = 'Names.txt'
pairsFile = 'Pairs.txt'

#Read Names.txt and create array of Names separated by lines
def readNamesIntoArray():
    data = []
    with open(namesFile, 'r') as file:
        for line in file:
            data.append(line.strip())
        return data

#Read existing pairs to reference when creating new ones
def readPairsIntoArray():
    data = []
    with open(pairsFile, 'r') as file:
        for line in file:
            #read the pairs splitting the names by using commas
            innerList = [elt.strip() for elt in line.split(',')]
            #append pair into array
            data.append(innerList)
        return data
    #GigaPog
    #I contributed a lot to this
def createPairs(nameList, pairList):
    #clone nameList into dummy so not to do destrutive edits to original list
    dummy = nameList[:]
    if len(dummy) % 2 == 1:
        dummy.append("O")
    newPairs = []
    count = 0
    #run through dummy list making pairs and removing the names that have been paired
    while len(dummy) > 1:
        count += 1
        for i in range(len(dummy)):
            for j in range(i+1,len(dummy)):
                pair = [dummy[i],dummy[j]]
                #check pair if it has existed before or not
                if pair not in pairList and pair[::-1] not in pairList:
                    newPairs.append(pair)
                    if(len(dummy) > 2):
                        dummy.remove(dummy[j])
                        dummy.remove(dummy[i])
                        count = 0
                    else:
                        return newPairs
                    break
                #if the list of names goes down to 3 or less and that group of people have been matched before it will return -1
                elif len(dummy) <= 3 or count > 10:
                    return -1

    return newPairs

def writePairs(pairs):
    with open(pairsFile, 'a') as file:
        for i in pairs:
            file.write(i[0] + " , " + i[1] + "\n")
        file.close()
    return


def main():
    # Print names from .txt
    nameArray = readNamesIntoArray()
    #create previous pairs as array, hashmap would be better but whatever you run this once a month
    namePairs = readPairsIntoArray()
    pairs = createPairs(nameArray,namePairs)
    #if -1 is returned shuffle the names and try again
    #if it infinitly repeats then you are approaching (number of names) Choose 2, high probablity that doesn't happen
    while pairs == -1:
        random.shuffle(nameArray)
        pairs = createPairs(nameArray, namePairs)
    writePairs(pairs)
    for i in pairs:
        print(i[0] + ' , ' + i[1])

if __name__ == "__main__":
    main()
