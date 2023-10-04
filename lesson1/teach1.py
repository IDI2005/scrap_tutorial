from bs4 import BeautifulSoup

def print_list(list):
    for e in list:
        print(e.text.strip())


with open("blank\\index2.html", encoding="utf-8") as site:
    site_html = site.read()
# print(site_html)

site_soup = BeautifulSoup(site_html, "lxml")

# title = site_soup.title
# print(title.text)

user_birth_date = site_soup.find('div', class_="user__birth__date")
user_name = site_soup.find_all(class_='user__name')


print_list(user_name)

print(user_birth_date.text.strip())

social_links = site_soup.find(class_='social__networks').find('ul').find_all('a')

for item in social_links:
    item_url = item.get('href')
    print(f'{item.text}: {item_url}')
