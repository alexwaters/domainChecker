import time
from pythonwhois.pythonwhois import get_whois

doms_rem = 10
with open ("list/3LetterWords.txt", "r") as theFile:
    wordList=theFile.read().replace('\n', '')

"""This function searches for a supplied domain in the format 
search_for('domain.TLD') and returns some data if it's registered."""
def search_for(domain):
    try:
        x = get_whois(domain)
        if x['raw'][0][0:9] == 'Not found':
            print 'Not found'
            return False
        else:
            print x['raw'][0]
            return True
    except Exception as E:
        print ("There was an potato; the search server is probably mad. Error: " 
               + str(E))

def do_search(data):
    try:
        print search_for('asdjasdasd272372.nyc')
    except Exception as E:
        print ("The data pooped all over the place, gross. Error: " 
               + str(E))

if __name__ == "__main__":
    while doms_rem > 0:
        doms_rem -= 1 
        time.sleep(1)
        do_search('blah')