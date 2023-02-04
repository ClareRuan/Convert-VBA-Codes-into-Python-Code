# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 13:08:10 2022

@author: cr_ru
"""

# =============================================================================
# 
# =============================================================================
import pandas as pd

from ftplib import FTP
host = 'ftp.xxx.com'
user='xxx.com'
pwd='XXX'
ftp=FTP(host)
ftp.login(user=user,passwd=pwd)

file_name_on_ftp = 'Customer_Info.xlsx'
file_directory_on_ftp='2210'
file_name_local='cust.xlsx'

ftp.cwd(file_directory_on_ftp)

# step 1 - download file

def download_ftp(host, user, pwd, file_directory_on_ftp, file_name_on_ftp,file_name_local):
    ftp=FTP(host)
    ftp.login(user=user,passwd=pwd)

with open('../2210/data/mock/cust.xlsx','wb') as f:
    ftp.retrbinary('RETR Customer_Info.xlsx', f.write)

ftp.quit()

def loading_file(file_name):
    df =pd.read_excel(f'data/mock/{file_name}')  # df: abbr dataframe
   
    return df


# step 2 - convert
def data_conversion(df,lo):
    # cleaning
    lo['msg']=''
    for index, row in df.iterrows():
        # print(row)
        
        age = row['Age']
        score = row['Score']
        if pd.isna(age):
            lo['msg']=lo['msg'] + f"{row['Name']} | Age: missing value \n"
            age=50
        elif age >75:
            print(f"{row['Name']} | Age > 75")
            age = 75
        elif age <25:
            print(f"{row['Name']} | Age < 25")
            age = 25
        df.loc[index,'Age'] = age
        
        if pd.isna(score):
            lo['msg'] = lo['msg'] + f"{row['Name']} | Score: missing value \n"
            score=50
        elif score > 100:
            print(f"{row['Name'] | Score > 100")
            score=100 * age / 75
        else:


# step 3.1 - persist to db
# connect to destination database
# validate backend data in destination db

# step 3.2 - log



# step 4 - upload the log file


if __name__=='__main__':
    logObj={}
    download_ftp(host,user,pwd,file_directory_on_ftp,file_name_on_ftp,file_name_local)
    df = loading_file(file_name_local)

    
    
    
    print(df)
    
    print(logObj)
    
    
    
# task scheduler
    
    
    