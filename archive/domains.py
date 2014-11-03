""" Running this file with all functions uncommented will result in several
files of fixed length. The files contain words which can easily be copied
and pasted into GoDaddy's bulk domain name checker. This code is deprecated
and for funny sidelong looks only. These aren't the droids you're looking for.

Although, I did use this silly little script to register about 5 really sweet
.NYC domains. Thus the inspiration to build out an application was born.

GD's 500 word bulk limit is a lie, it will timeout. 230 worked...
"""

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

class Chunk:
    offset = 0
    contents = []
    pass

def getWords(offset):
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

def chunkIt():
    counter = 0
    while numChunks > counter:
        chunk = Chunk()
        chunk.offset = counter
        chunk.contents = getWords(counter)
        chunks.append(chunk.contents)
        counter+=1
    
def makeFiles():
    counter = 0
    while numChunks > counter:
        with open('chunked'+str(counter)+'.txt', 'w') as the_file:
            for word in chunks[counter]:
                the_file.write(str(word)+'\n')
        counter+=1

def printStats():
    print "\nTotal Dictionary Length: " + str(listLen)
    print "Number of words: " + str(words)
    print "Number of Chunks: " + str(numChunks)

chunkIt()
#makeFiles()
printStats()

#I know this is ugly, I just wanted a list of the words 
#one per line in 300-word lists