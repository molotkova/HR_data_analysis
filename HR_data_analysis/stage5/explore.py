import ast

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

df_full['left'] = df_full['left'].astype(int)

df_first_pivot = df_full.pivot_table(index='Department', columns=['left', 'salary'], values='average_monthly_hours', aggfunc='median')
df_first_res = df_first_pivot[(df_first_pivot[0.0]['high'] < df_first_pivot[0.0]['medium']) | (df_first_pivot[1.0]['high'] > df_first_pivot[1.0]['low'])]

print(df_first_res.to_dict())

df_second_pivot = df_full.pivot_table(index='time_spend_company',
                                      columns='promotion_last_5years',
                                      values=['satisfaction_level', 'last_evaluation'],
                                      aggfunc = ['min', 'max', 'mean'] ).round(2)
df_second_res = df_second_pivot[df_second_pivot['mean']['last_evaluation'][0] >
                                df_second_pivot['mean']['last_evaluation'][1]]
print(df_second_res.to_dict())