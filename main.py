import requests
from bs4 import BeautifulSoup

url = input("Enter a URL:\n")
payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
soupedtext = BeautifulSoup(response.text, 'html.parser') # ------- makes the html text able to be souped/run functions on ---------
if "www.history.com" in str(url): # ------ runs this for HISTORY.COM articles... -----
    newsoupedtext = soupedtext.find_all("dd", attrs={"data-sentry-source-file": "box.tsx"}) #scans the entire html and grabs only the citation box
    nst0 = newsoupedtext
    nst1 = [ ]
    for element in nst0: # -------- repeatedly goes through all the citations and pulls out only the text, formatts it as a list -----------
        text = element.get_text() 
        nst1.append(text)
    # -------- these commands all define certain portions of the list as different data -----
    ArticleName = nst1[0]
    AuthorsName = nst1[1]
    WebsiteName = nst1[2]
    URL = nst1[3]
    DateAccessed = nst1[4]
    Publisher = nst1[5]
    DateLastUpdate = nst1[6]
    Heresthecitation = "Here's the citation: \n"
    # ------- the final print ----------
    print(f'{Heresthecitation}{AuthorsName}. \"{ArticleName}.\" {WebsiteName}. {Publisher}, {DateLastUpdate}. Web. Accessed {DateAccessed}.\n<{URL}>')
elif "www.britannica.com" in str(url): # ------ runs this for BRITANNICA.COM articles... -----
    nst2 = soupedtext.find_all("div", attrs={"class": "citation font-serif border rounded p-15 mt-20"})
    nst3 = []
    for element in nst2:
        text = element.get_text()
        nst3.append(text)
    















