import json
import requests
from bs4 import BeautifulSoup
import time

def main():
    url = "http://www.generalasp.com/D201/onlineapp/jobpostings/Output.asp?Category=High+School+Teaching&all=cat&"
    r = requests.get(url)
    while True:
        soup = BeautifulSoup(r.content, 'html.parser')
        tables = soup.find_all('table')
        data = {}
        for table in tables:
            print("\n")
            pull_row = table.find_all('td')
            title_clean = (pull_row[0].text)
            job_id = pull_row[1].text[8:]
            if len(job_id) > 4:
                job_id = job_id[:4]
                print(job_id)
            else:
                print(job_id)

            data[title_clean] = job_id
        print(data)
        url2 = 'https://api.jsonbin.io/v3/b'
        headers = {
            'Content-Type': 'application/json',
            'X-Master-Key': '$2b$10$8ZLGc53IHdU2svwoocfXF.qh1P7GfegPE5F7oGskVjAg.ji1qTNXa'
        }
    
        req = requests.post(url2, json=data, headers=headers)
        print(req.text)
        time.sleep(86,400)

if __name__ == "__main__":
    main()