from bs4 import BeautifulSoup
import requests
from itertools import zip_longest
import csv
import pandas as pd

def scrapping():
    company_names=list()
    skills=list()
    published_dates=list()
    page=0
    more_infos=list()
    while True:
     html_text=requests.get(f'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=python&pDate=I&sequence=2&startPage={page}')
     soup=BeautifulSoup(html_text.text,'lxml') #don t forget .text it makes html code a string
     page_limit=int(soup.text.find("strong"))
     jobs=soup.find_all('li',{'class':'clearfix job-bx wht-shd-bx'}) # list of jobs
     for job in jobs :
        company_name=job.find('h3',class_='joblist-comp-name').text.replace('\n','')
        skill=job.find('span',class_='srp-skills').text.replace('\n','')
        published_date=job.find('span',class_='sim-posted').text.replace('\n','')
        company_names.append(company_name)
        skills.append(skill)
        published_dates.append(published_date)
        print(f'company_name: {company_name}\n')
        print(f'required_skills{skill}\n')
        more_info=job.header.h2.a['href'] # copy link
        more_infos.append(more_info)
        print(f'the link :{more_info}')
        page+=1
        if page ==page_limit//25:
            
             break
    return  company_names,skills,published_dates,more_infos


file_list=scrapping()
exported=zip_longest(*file_list)
with open("project1.1_scrapping.csv","w") as myfile:
  wr=csv.writer(myfile)
  wr.writerow(['company name','skills','published_dates','more_infos'])
  wr.writerows(exported)









