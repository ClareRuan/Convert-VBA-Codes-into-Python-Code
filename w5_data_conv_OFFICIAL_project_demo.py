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
host = 'ftp.jobready123.com'
user='dq121@testingmoo.com'
pwd='K#Xwx3Sp.gmL'
ftp=FTP(host)
ftp.login(user=user,passwd=pwd)

file_name_on_ftp = 'Customer_Info.xlsx'
file_directory_on_ftp='2210'
file_name_local='cust.xlsx'

log_name_on_ftp = 'log.txt'
log_name_local='log.txt'

# step 1 - download file

def download_ftp(host, user, pwd, file_directory_on_ftp, file_name_on_ftp,file_name_local):
    ftp=FTP(host)
    ftp.login(user=user,passwd=pwd)
    
    ftp.cwd(file_directory_on_ftp)

    with open('../2210/data/mock/{file_name_local}','wb') as f:
        ftp.retrbinary(f'RETR {file_name_on_ftp}', f.write)

    ftp.quit()
    
def upload_ftp(host, user, pwd, file_directory_on_ftp, file_name_on_ftp,file_name_local):
    ftp=FTP(host)
    ftp.log(user=user,passwd=pwd)
    
    ftp.cwd(file_directory_on_ftp)
    
    with open('../2210/data/{file_name_local}','rb') as f:  # rb: read
        ftp.storelines(f'STOR {file_name_on_ftp}', f.write)

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
            #print(f"{row['Name']} | Age: missing value")
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
            print(f"{row['Name'] }| Score > 100")
            score=100 * age / 75
        elif score<1:
            print(f"{row['Name']} | Score < 1")
            score = 1
        df.loc[index,'Score'] = score


# step 3.1 - persist to db
# connect to destination database
# validate backend data in destination db

def persiste_todo(df):
    connection = pymysql.connect(
                                 user='root',
                                 password = '',
                                 database = 'test_abc',
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection:
            with connection.cursor() as cursor:
                #Create a new record
                for index, row in df.iterrows():
                    name = row['Name']
                    score = row['Score']
                    age = row['Age']
                    sql = f"INSERT INTO 'Customers' ('Name', 'Age', 'Score') VALUES ('{name}','{age}','{score}')"
                    cursor.execute(sql)

# connection is not autocommit by default, so you must commit to save your changes
            connection.commit()
            with connection.cursor() as cursor:
                # read a single record
                sql = "SELCT * from name_t"
                cursor.execute(sql)
                result = cursor.fetchall()
                print(result)



# step 3.2 - log
def create_log(log_name_local,lo):
    with open(log_name_local, 'w') as f:
        f.write(lo['msg'])


# step 4 - upload the log file

    if __name__=='__main__':
            
        logObj={}
            
        download_ftp(host, user, pwd, file_directory_on_ftp, file_name_on_ftp, file_name_local)
        df = loading_file(file_name_local)
        data_conversion(df,logObj)
        create_log(log_name_local, logObj)
        upload_ftp(host, user, pwd, file_directory_on_ftp, log__name_on_ftp, log_name_local)
        print(df)
    
        print(logObj)
        
# task scheduler
    
    
    