import pandas as pd
import requests
import os

# write your code here


if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

    df_A = pd.read_xml('../Data/A_office_data.xml')
    df_B = pd.read_xml('../Data/B_office_data.xml')
    df_hr = pd.read_xml('../Data/hr_data.xml')
    df_A.index = ['A' + str(i) for i in df_A['employee_office_id'].values]
    df_B.index = ['B' + str(i) for i in df_B['employee_office_id'].values]
    df_hr = df_hr.set_index(df_hr['employee_id'])
    print(list(df_A.index))
    print(list(df_B.index))
    print(list(df_hr.index))





