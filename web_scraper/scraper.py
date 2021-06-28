import requests

from bs4 import BeautifulSoup

URL= "https://en.wikipedia.org/wiki/History_of_Mexico"

def  get_citations_needed_count():

    page= requests.get(URL)

    soup=BeautifulSoup(page.content,'html.parser')

    results=soup.find(class_='mw-parser-output')

    citation_results=results.findAll('a',title='Wikipedia:Citation needed')
    print(citation_results)

    return (len(citation_results))


def get_citations_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(class_="mw-parser-output")

    p_tags = []
   

if __name__=='__main__':

    get_citations_needed_count()
    

   
   
#all_jobs = all_results.find_all('li', class_='has-pointer-d')
# print(len(all_jobs))
