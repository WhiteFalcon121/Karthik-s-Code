from urllib.request import urlopen
import re
'''
#url = "http://olympus.realpython.org/profiles/aphrodite"
url = "https://www.bbc.co.uk"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('utf-8')
#html = "<title  > ad</title>"
#print(html)

#pattern = r"<title.*?>.*?</title.*?>"  # use '.*?' for any text (so blank space here) up to '>'
pattern = r"<span aria-hidden.*?>.*?</span.*?>"
matches = (re.search(pattern, html, re.IGNORECASE)).group() # .group() returns the string
#print(matches)
matches = re.sub("<.*?>", "", matches) # '?' = non-greedy match
print(matches)
'''
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://www.bbc.co.uk"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode('utf-8')

full_html = BeautifulSoup(html, "html.parser") # parse the html varaible using Python's inbuilt html.parser
#print(full_html.get_text())
matches = str(full_html.find_all('span', {"aria-hidden":"false"}, text=True)) # find text in the span tag where "aria-hidden='false'"
matches = matches[1:-1] # remove square brackets
#print(matches)
matches = re.sub("<.*?>", "___", matches) # remove anything in tags
#print(matches)
full_matches = matches
#print(matches)
matches = re.search("___.*?___",matches, re.IGNORECASE) # 1st match

headlines = []

for i in range(0,6):
    if i == 0:
        matches_section = full_matches
    #print(matches)
    start = (matches.start())
    end = (matches.end())
    #print(start, end)
    headline = matches_section[start:end]
    if "&amp;" in headline:
        #print("substituting '&' character")
        headline = re.sub("&amp;", "&", headline) # sub in & when html is used
    headlines.append(headline)
    matches_section = matches_section[end:]
    #matches = re.sub("&amp;", "&", matches_section)
    matches = re.search("___.*?___",matches_section, re.IGNORECASE)
    #print(matches)
    #print(matches.group())
headlines = headlines[::-1]
for i in headlines:
    index = headlines.index(i)
    #print(i)
    headlines[index] = re.sub("___", "", i) # get rid of all the underscores
print(headlines)
#####add links to articles
#print(str(full_html.find_all('a href', {"class":"css-1rqiz8d-PromoLink ett16tt7"})))

links = str(full_html.find_all('a', {"class":"css-1rqiz8d-PromoLink ett16tt7"}))
links = links[1:-1] # remove square brackets
#print(links)
full_links = links

links_matches = re.search("href.*?>", links, re.IGNORECASE) # 1st match
#print(links_matches.group())
links_list = []

for i in range(0,3):
    if i == 0:
        links_section = full_links
    start = links_matches.start()
    end = links_matches.end()
    link = links_section[start:end]
    #print(link)
    #print("\n")
    links_list.append(link)
    links_section = links_section[end:]
    #print(links_section)
    links_matches = re.search("href.*?>", links_section, re.IGNORECASE)
links_list = links_list[::-1]
print(links_list)
