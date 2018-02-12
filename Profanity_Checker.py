from urllib.request import urlopen
def read_text():
    text = open("C:/Users/aditya/Desktop/text.txt")
    contents = text.read()
    print(contents)
    check_profanity(contents)
    text.close()
    
def check_profanity(text_to_check):
    with urlopen('http://www.wdylike.appspot.com/?q='+text_to_check) as response:
       html = response.read()
       print(html)
       response.close()
    
read_text()
