import pandas as pd
from datetime import datetime

#loading the data from oracle sql developer
df=pd.read_csv('oracle_export.csv')

#converting the data strings to data objects
df['SALESDATE'] = pd.to_datetime(df['SALESDATE'],dayfirst=True)


df['Error_Qty']=df['QTY']<=0
df['Error_Date']=df['SALESDATE']> datetime.now()
df['Error_Price']=(df['PRODID']==101)& (df['PRICE']<10000)
# Above we are doing the error price only for PRODID=101, we can do the same for other PRODID as well


df['Audit_Comment'] = ""
df.loc[df['Error_Qty'] == True, 'Audit_Comment'] += "Negative Quantity Detected; "
df.loc[df['Error_Date'] == True, 'Audit_Comment'] += "Future Sale Date Error;"
df.loc[df['Error_Price'] == True, 'Audit_Comment'] += "Suspected Price Entry Error;"


is_suspicious =(df['Error_Qty']== True )| (df['Error_Date']==True)| (df['Error_Price']==True)
Report =df[is_suspicious]

print('AUDIT RESULTS')
print(Report)

Report.to_csv('audit_report_final.csv', index = False)

