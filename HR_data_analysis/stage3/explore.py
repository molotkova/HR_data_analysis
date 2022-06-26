import pandas as pd


df_A = pd.read_xml('A_office_data.xml')
df_B = pd.read_xml('B_office_data.xml')
df_hr = pd.read_xml('hr_data.xml')
df_A.index = ['A' + str(i) for i in df_A['employee_office_id'].values]
df_B.index = ['B' + str(i) for i in df_B['employee_office_id'].values]
df_hr = df_hr.set_index(df_hr['employee_id'])
df_offices = pd.concat([df_A, df_B])
df_full = df_offices.merge(df_hr, how='left', left_index=True, right_index=True, indicator=True)
df_full = df_full[df_full['_merge'] == 'both']
df_full = df_full.drop(['employee_office_id', 'employee_id', '_merge'], axis=1)
df_full = df_full.sort_index()
print(list(df_full.sort_values('average_monthly_hours', ascending=False)['Department'].values[:10]))
print(df_full[(df_full['Department'] == 'IT') & (df_full['salary'] == 'low')]['number_project'].sum())
print(df_full.loc[['A4', 'B7064', 'A3033'], ['last_evaluation', 'satisfaction_level']].values.tolist())
