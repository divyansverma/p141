import requests
import pandas as pd
from bs4 import BeautifulSoup

stars_url="https://en.wikipedia.org/wiki/List_of_brightest_stars"
page=requests.get(stars_url)
#print(page)
soup =BeautifulSoup(page.text,"html.parser")
star_table=soup.find('table')
tem_list=[]
table_row=star_table.find_all('tr')
for row in table_row:
    td=row.find_all('td')
    r=[i.text.rstrip()for i in td]
    tem_list.append(r)

names=[]
distance=[]
mass=[]
radius=[]
for i in range(1,len(tem_list)):
    names.append(tem_list[i][2])
    distance.append(tem_list[i][4])
    mass.append(tem_list[i][1])
    

df=pd.DataFrame(list(zip(names,distance,mass)),columns=["starnames","distance","masses"])
print(df)
df.to_csv("stars.csv")  




















