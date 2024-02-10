import sys
import os

namesFile = 'Names.txt'
pairsFile = 'Pairs.txt'

def deleteNamePair(name):
    with open(pairsFile, "r") as input:
        with open("temp.txt", "w") as output:
            # iterate all lines from file
            for line in input:
                #split line based on ','
                innerList = [elt.strip() for elt in line.split(',')]
                # if text matches then don't write it
                if innerList[0] != name and innerList[1] != name:
                    print("Name Found")
                    output.write(line)

    # replace file with original name
    os.replace('temp.txt', pairsFile)

    with open(namesFile, "r") as input:
        with open("remp.txt", "w") as output:
            # iterate all lines from file
            for line in input:
                #split line based on ','
                if line.strip("\n") != name:
                    print("Name Found")
                    output.write(line)

    # replace file with original name
    os.replace('remp.txt', namesFile)


def main():

    name = sys.argv[1]
    deleteNamePair(name)


if __name__ == "__main__":
    main()