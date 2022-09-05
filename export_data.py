
import pygsheets
import pandas as pd
#authorization
from main.index import df3

print(1111111)
#print(final_df)
sheet_output ='Output'
gc = pygsheets.authorize(service_file='../secrets/cred.json')
sh = gc.open_by_key('1-GGTWLdEw8Ucj2uXmQSEqmMJHLcRSV6DTdJZEh80va0')
try:
    sh.add_worksheet(sheet_output)
except:
    pass
wks_write = sh.worksheet_by_title(sheet_output)
wks_write.clear('A1', None, '*')
wks_write.set_dataframe(df3, (1, 1), encoding='utf-8', fit=True)

#wks_write.frozen_rows = 1




