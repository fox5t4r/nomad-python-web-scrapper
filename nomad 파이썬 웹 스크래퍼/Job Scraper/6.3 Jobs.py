import requests
from bs4 import BeautifulSoup

url = 'https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings'

response = requests.get(url)

soup = BeautifulSoup(
    response.content,
    "html.parser",
)

jobs = soup.find("section", class_='jobs').find_all('li')[0:-1] # 리스트로 저장됨

for job in jobs:
    title = job.find("h3", class_="new-listing__header__title")
    company = job.find("p", class_="new-listing__company-name")
    headquarters = job.find("p", class_="new-listing__company-headquarters")

    title = title.text.strip() if title else "N/A"
    company = company.text.strip() if company else "N/A"
    headquarters = headquarters.text.strip() if headquarters else "N/A"

    print(f'{title} | {company} | {headquarters}')

