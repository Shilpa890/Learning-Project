# Write a function to print agents count in agents.txt file and find the ids of all the active agents 
# Implement with pandas and without pandas
# Dump output in a file named analysis.txt


# Find the team with maximum salary [1,2,3,4,5] they are paying to their active agents.
# Fetch data from google sheet.
# Implement with and without pandas.
# Without Pandas


# print('Happy Learning 1')
# file = open("c:/Work/Learning/data/agents.txt")
# print(file)
# content=file.readlines()
# content=[t.replace('\n','') for t in content]
# header=content[:1]
# rows=content[1:]
# print(header)
# headerArr = header[0].split(",")
# #print(rows)
# #print(len(rows))
# print(len(headerArr))
# j=0
# k=0
# for i in range(len(headerArr)):
#     if (headerArr[i]).lower()=="agentid":
#         print(i)
#         j=i
#     if (headerArr[i]).lower()=="status":
#         print(i)
#         k=i    

# c=0
# s=0
# f= open("c:/Work/Learning/data/analysis1.txt","w+")
# for r in rows:

#     rArray = r.split(',')
#     #print(rArray)
#     if rArray[j] is not '':
#         c=c+1
#     if rArray[k].lower()=='active': 
#         f.write("AgentId %d\r" %int(rArray[j]))
#         print("AgentId",rArray[j])
#         s=s+1
# print("Active Agent Count",s)
# print ("AgentId Count",c)        
# f.close()

# With Pandas fg
# import numpy as np

# agents_df=pd.read_table("c:/Work/Learning/data/agents.txt",sep=",")
# print(agents_df)
# print(agents_df.count())
# print_custom('shilpa')
# df_filtered = agents_df[agents_df.Status=='Active'].AgentId
# print(df_filtered)
# df_filtered.to_csv('new_file.csv')

# def print_sheet(input):
#     print('Custom output: {}'.format(input))

from main.GoogleSheets_API import main
import pandas as pd

from main.export_Sheet_wpd import mainnew

my_values = main()
# print(my_values)
# print('Agent data df')
# print(my_values['AgentData'])
print(my_values.keys())
Agent_data = my_values['AgentData']
Team_data = my_values['TeamData']
Salary_Data = my_values['SalaryData']
# print(Agent_data)
# print(Agent_data)
# header=my_values[:1]
# rrows=my_values[1:]
# for row in my_values:
#         print('%s, %s %s' % (row[0], row[1], row[2]))
# Find the team with maximum salary [1,2,3,4,5] they are paying to their active
df1 = pd.merge(left=Agent_data, right=Team_data, how="inner", on='AgentId')
df2 = pd.merge(left=Salary_Data, right=df1[df1.Status == 'Active'], how="inner", on='AgentId')
df2['Salary'] = df2['Salary'].astype('float')
final_df = df2.groupby('TeamId').Salary.sum()
df3 = pd.DataFrame(final_df, dtype=int)
print(df3)
# Dump output in a file named analysis.txt

# without pandas

my_tables = mainnew()
Agentd = my_tables[0]
Teamd = my_tables[1]
Salaryd = my_tables[2]
active_agents = []
print('xxxxx')
print(Agentd)
for rows in Agentd:
    if rows[2] == 'Active':
        active_agents.append(rows[0])
print(active_agents)

active_agentid_to_salary = {}

for agentid in active_agents:
    for row in Salaryd:
        if row[0] == agentid:
            active_agentid_to_salary[agentid] = float(row[1])

print(active_agentid_to_salary)
print(Teamd)
teamid_to_salary = {}

for team in Teamd:
    if team[0] in active_agents:
        print('Key: {}'.format(team[1]))
        teamid_to_salary[team[1]] = teamid_to_salary.get(team[1], 0) + active_agentid_to_salary[team[0]]
        print(teamid_to_salary)
