
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd


urls=['https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&before_author=t8bD_6cQAAAJ&astart=0',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=uGv7AObu__8J&astart=10',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=uAnZAB_3__8J&astart=20',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=4536AAH5__8J&astart=30',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=RTT9AIb6__8J&astart=40',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=VB79ANT7__8J&astart=50',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=GI33AGT8__8J&astart=60',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=qHgYAMP8__8J&astart=70',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=edgQAEH9__8J&astart=80',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=OFABAYz9__8J&astart=90',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=UWX6APf9__8J&astart=100',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=yjU8AEv-__8J&astart=110',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=iNs4AHX-__8J&astart=120',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=KJP4AKL-__8J&astart=130',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=PTgTAMr-__8J&astart=140',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=1HK2AOT-__8J&astart=150',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=8JSPACL___8J&astart=160',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=9bL4AD7___8J&astart=170',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=E9d9AFv___8J&astart=180',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=LEt9AHT___8J&astart=190',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=6ZbCAIv___8J&astart=200',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=VQH7AJn___8J&astart=210',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=Yi36AK____8J&astart=220',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=gZv3ALv___8J&astart=230',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=wfy1AMX___8J&astart=240',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=Y2gYANL___8J&astart=250',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=pRriANv___8J&astart=260',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=ZyjqAOP___8J&astart=270',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=k3WyAOj___8J&astart=280',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=6LUeAe3___8J&astart=290',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=Kf_xAPH___8J&astart=300',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=5MABAfT___8J&astart=310',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=TaL4APb___8J&astart=320',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=cOnnAPn___8J&astart=330',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=TQ35APr___8J&astart=340',
      'https://scholar.google.com/citations?view_op=search_authors&hl=en&mauthors=um5&after_author=ZYH4APz___8J&astart=350'




]

npo_jobs= {}
job_no = 0

for url in urls :
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    frames = page_soup.findAll("div",{"class" : "gsc_1usr"})

    

    for frame in frames :
        
        
        fav_prof = frame.findAll("h3",{"class" : "gs_ai_name"})
        prof = fav_prof[0].text.strip()

        fav_univ = frame.findAll("div",{"class" : "gs_ai_aff"})
        univ = fav_univ[0].text.strip()

        fav_cited = frame.findAll("div",{"class" : "gs_ai_cby"})
        cited = fav_cited[0].text.strip()
        
        numbers = [int(word) for word in cited.split() if word.isdigit()]
        Nb_cited =numbers[0]

        job_no+=1
        npo_jobs[job_no] = [prof , univ , Nb_cited]



npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient = 'index' , columns = ['prof ','university' , 'cited by'])
npo_jobs_df.to_csv('um5.csv')