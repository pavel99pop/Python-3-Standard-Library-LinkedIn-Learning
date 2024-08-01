# HTML Parser Module
from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start tag: ', tag)
        for attr in attrs:
            print('attr: ', attr)

    def handle_endtag(self, tag):
        print('End tag: ', tag)

    def handle_comment(self, data):
        print('Comment: ', data)
    
    def handle_data(self, data):
        print('Data: ', data)

myParser = HTMLParser()
myParser.feed('<html><head><title>Title goes here</title></head><body><h1><!--Comment goes here-->Header goes here</h1></body></html>')
print()

userIn = input('Type html...\n')
myParser.feed(userIn)
print()

with open('sampleHTML.html', 'r') as myFile:
    # myParser.feed(str(myFile.readlines()))
    line = myFile.readline()
    myParser.feed(line)