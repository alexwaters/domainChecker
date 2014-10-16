with open ("domainDict", "r") as theFile:
    wordList=theFile.read().replace('\n', '')

listLen = len(wordList)
gdBulkLim = 230
wordSize = 3
words = listLen / wordSize
numChunks = (words / gdBulkLim) + 1
chunks = []
#domExt = ".nyc"
domExt = ""
counter = 0

class Chunk:
    offset = 0
    contents = []
    pass

def chunkIt(offset):
    tempList = []
    a,b = 0,0
    off = offset*gdBulkLim*wordSize
    
    while a < len(wordList) and b < gdBulkLim:
        start,fin = (a+off),(a+off+wordSize)
        
        word = wordList[start:fin]
        if len(word) == wordSize:
            tempList.append(str(word) + domExt)
        a+=wordSize
        b+=1
    print ("Chunk " + str(offset + 1) + " (Len:" + str(len(tempList)) + "): "
    + str(tempList))
    return tempList

while numChunks > counter:
    chunk = Chunk()
    chunk.offset = counter
    chunk.contents = chunkIt(counter)
    chunks.append(chunk.contents)
    counter+=1
counter = 0

print "\nTotal Dictionary Length: " + str(listLen)
print "Number of words: " + str(words)
print "Number of Chunks: " + str(numChunks)

while numChunks > counter:
    with open('chunked'+str(counter)+'.txt', 'w') as the_file:
        for word in chunks[counter]:
            the_file.write(str(word)+'\n')
    counter+=1
counter = 0