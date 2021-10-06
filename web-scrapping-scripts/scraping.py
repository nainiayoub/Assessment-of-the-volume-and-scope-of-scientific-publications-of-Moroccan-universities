import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

profNames=[]
specialty=[]
university=[]
nbrOfCitation1=[]

result=requests.get("https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&before_author=t8bD_6cQAAAJ&astart=0")

src=result.content

soup=BeautifulSoup(result.content,"html.parser")

profName=soup.findAll("h3",{"class":"gs_ai_name"})
specialties=soup.findAll("a",{"class":"gs_ai_one_int"})
universities=soup.findAll("div",{"class":"gs_ai_aff"})
nbrOfCitations=soup.findAll("div",{"class":"gs_ai_cby"})

for i in range(len(profName)):
    profNames.append(profName[i].text)
    university.append(universities[i].text)
    nbrOfCitation1.append(nbrOfCitations[i].text)

#print(university)
for j in range(len(specialties)):
    specialty.append(specialties[j].text)


print(specialty)

file_list=[profNames,university,nbrOfCitation1]
exported=zip_longest(*file_list)

with open("C:\\Users\\blank\\Desktop\\bureau\\jobstestH.csv", "w") as mycsvfile:
    wr=csv.writer(mycsvfile)
    wr.writerow(["profName","university","nbr citation","specialty"])
    wr.writerows(exported)