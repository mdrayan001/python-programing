#Requirements
#Extract the following fields for each job posting:
    #Job title
    #Company name
    #Location
    #Job detail page URL


#import packages needed
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/' #Fake Job postings website
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

job_data = [] #empty dataframe to store scraped data later
results = soup.find_all('div',class_='column is-half')

for result in results:
    job = result.find('h2',class_ = 'title is-5').text.strip().title()
    company = result.find('h3',class_='subtitle is-6 company').text.strip().title()
    location = result.find('p',class_='location').text.strip().title()
    job_url = result.find('a', class_='card-footer-item', string = 'Apply', href=True)['href'].strip()

    job_data.append({
        'Job_Title':job,
        'Company':company,
        'Location':location,
        'URL':job_url
    })

df = pd.DataFrame(job_data)
print(df)
df.to_csv(r'C:\Users\jonat\Documents\2026 Coding Projects\CSV Output\job_listings.csv',index=False)
