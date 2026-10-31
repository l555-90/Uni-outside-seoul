import requests
from bs4 import BeautifulSoup

url = "https://www.timeshighereducation.com/student/best-universities/best-universities-south-korea"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]  # skip header row

for row in rows:
    cols = row.find_all("td")
    if cols:
        university_name = cols[2].get_text(strip=True)
        print(university_name)