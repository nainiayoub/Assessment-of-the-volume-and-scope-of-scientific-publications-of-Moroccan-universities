import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest



job_title=[]
specialty=[]
university=[]
nbrOfCitation1=[]

result=requests.get("https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=universite+hassan+2&after_author=VGuMAP3___8J&astart=420")
src=result.content


soup=BeautifulSoup(src,"html.parser")
job_titles=soup.findAll("h3",{"class":"gs_ai_name"})
specialties=soup.findAll("a",{"class":"gs_ai_one_int"})
universities=soup.findAll("div",{"class":"gs_ai_aff"})
nbrOfCitations=soup.findAll("div",{"class":"gs_ai_cby"})

for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    university.append(universities[i].text)
    nbrOfCitation1.append(nbrOfCitations[i].text)
#print(university)
for j in range(len(specialties)):
    specialty.append(specialties[j].text)
print(specialty)


file_list=[job_title,university,nbrOfCitation1]
exported=zip_longest(*file_list)
with open("C:\\Users\\blank\\Desktop\\bureau\\jobstestH2.csv","a") as f:
    wr=csv.writer(f)
    wr.writerows(exported)