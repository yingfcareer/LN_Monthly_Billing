# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 13:07:31 2023

@author: yfang
"""
import cx_Oracle
import pandas as pd
import datetime

db=cx_Oracle.connect('analytics/password@prodlz-v.ds.aus.netspend.net:1521/prodlz_adhoc',encoding = "UTF-8",nencoding = "UTF-8")
cur = db.cursor()

cur.callproc("REFRESH_LN_BILLING_COUNT")


ora_conn = cx_Oracle.connect('analytics/password@prodlz-v.ds.aus.netspend.net:1521/prodlz_adhoc',encoding = "UTF-8",nencoding = "UTF-8") 
df=pd.read_sql("SELECT SUM(CT_ORDERED) FROM TEMP_LN_BILLING_COUNT_4 ORDER BY 1", ora_conn)

current_date = datetime.datetime.now().strftime("%m%d%Y")
df.to_csv(str('S:/NetSpend Online/Analytics/LN Billable Count/response' + current_date + '.csv'),header =False,index=False)
df.to_csv(str('S:/NetSpend Online/Analytics/Vendor/Lexis Nexis/response' + current_date + '.csv'),header =False,index=False)
