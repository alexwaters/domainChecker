wordList = "abcdefdeddesxd"
godaddyBulkLim = 500

class Chunk:
    contents = []
    length = len(contents)
    pass

chunks = []


def chunkIt():
    tempList = []
    a = 0
    b = 0
    
    while a < len(wordList) and b < godaddyBulkLim:
        tempList.append(wordList[a:(a+3)])
        a+=3
        b+=1
    return tempList


tempList = chunkIt()



print tempList[-1]
print "List Length: " + str(len(tempList))
print "Total Length: " + str(len(wordList))