import pandas as pd


df_A = pd.read_xml('../Data/A_office_data.xml')
df_B = pd.read_xml('../Data/B_office_data.xml')
df_hr = pd.read_xml('../Data/hr_data.xml')
df_A.index = ['A' + str(i) for i in df_A['employee_office_id'].values]
df_B.index = ['B' + str(i) for i in df_B['employee_office_id'].values]
df_hr = df_hr.set_index(df_hr['employee_id'])
df_offices = pd.concat([df_A, df_B])
df_full = df_offices.merge(df_hr, how='left', left_index=True, right_index=True, indicator=True)
df_full = df_full[df_full['_merge'] == 'both']
df_full = df_full.drop(['employee_office_id', 'employee_id', '_merge'], axis=1)
df_full = df_full.sort_index()

def count_bigger_5(series):
    counter = 0
    for j in series.values:
        if j > 5:
            counter += 1
    return counter

df_full['left'] = df_full['left'].astype(int)

print(df_full.groupby('left').agg({'number_project' : ['median', count_bigger_5],
                             'time_spend_company': ['mean', 'median'],
                             'Work_accident':['mean'],
                             'last_evaluation': ['mean', 'std']}).round(2).to_dict())
