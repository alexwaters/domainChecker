with open ("domainDict", "r") as theFile:
    wordList=theFile.read().replace('\n', '')

godaddyBulkLim = 500
wordSize = 3
numChunks = (len(wordList) / godaddyBulkLim) + 1
chunks = []

class Chunk:
    contents = []
    length = len(contents)
    pass

def chunkIt(offset):
    tempList = []
    a = 0
    b = 0
    offset = offset*godaddyBulkLim
    
    while a < len(wordList) and b < godaddyBulkLim:
        start,fin = (a+offset),(a+offset+wordSize)
        word = wordList[start:fin]
        if len(word) == wordSize:
            tempList.append(word)
        a+=3
        b+=1
    print "asdas: " + str(tempList)
    return tempList

z=0
while numChunks > z:
    chunk = Chunk()
    chunk.contents = chunkIt(z)
    chunks.append(chunk.contents)
    z+=1

print "Total Length: " + str(len(wordList))
print "numChunks: " + str(numChunks)
print "Chunks Length: " + str(len(chunks))
print str(chunks)