from bs4 import BeautifulSoup


with open("blank\index.html", encoding="utf-8") as site:
    site_html = site.read()
# print(site_html)

site_soup = BeautifulSoup(site_html, "lxml")

# title = site_soup.title
# print(title.text)

user_birth_date = site_soup.find('div', class_="user__birth__date")
print(user_birth_date.text.strip())
