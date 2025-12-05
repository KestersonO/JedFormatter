import requests
from bs4 import BeautifulSoup


url = input("Enter a URL:\n")
response = requests.get(url) #gets the html of the url
soupedtext = BeautifulSoup(response.text, 'html.parser') #makes the html text able to be souped/run functions on

newsoupedtext = soupedtext.find_all("dd", attrs={"data-sentry-source-file": "box.tsx"}) #scans the entire html and grabs only the citation box
nst0 = newsoupedtext
nst1 = [ ]
for element in nst0: #repeatedly goes through all the citations and pulls out only the text
    text = element.get_text() 
    nst1.append(text)
ArticleName = nst1[0]
AuthorsName = nst1[1]
WebsiteName = nst1[2]
URL = nst1[3]
DateAccessed = nst1[4]
Publisher = nst1[5]
DateLastUpdate = nst1[6]
Heresthecitation = "Here's the citation: \n"
print(f'{Heresthecitation}{AuthorsName}. \"{ArticleName}.\" {WebsiteName}. {Publisher}, {DateLastUpdate}. Web. Accessed {DateAccessed}.\n<{URL}>')














