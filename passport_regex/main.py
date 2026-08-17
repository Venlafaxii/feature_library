import json
import pandas as pd
from datetime import datetime
df= pd.read_csv('passport_regex/country_code_web.csv')
country_codes= dict(zip(df['Code'], df['Country']))

def convert_year(year):
    current_year = int(str(datetime.now().year)[-2:])

    year = 2000 + year if year <= current_year else 1900 + year #can be updated to be dynamic
    return year
    
line1= "P<VNMGUEVARA<<CHE<<<<<<<<<<<<<<<<<<<<<<<<<<<"
line2= "3916999930GBR0012016M4006011<<<<<<<<<<<<<<02"

raw_nationality= ''.join(filter(str.isalnum, line1[2:5]))
nationality= country_codes[raw_nationality]

IC_number= ''.join(filter(str.isalnum, line2[0:9]))
sex= line2[20]

raw_name = ''.join(filter(lambda c: c.isalpha() or c == '<', line1[5:-1])).replace('<', ' ').strip()
name = " ".join(raw_name.split())

############################# DOB ST
raw_dob= line2[13:19]
raw_year = raw_dob[0:2]
dob_full_year = convert_year(int(raw_year))

dob_month = raw_dob[2:4]
dob_day = raw_dob[4:6]
############################# DOB END
###################################### Expiry ST
raw_expiry= line2[21:27]
raw_year = raw_expiry[0:2]
e_full_year = 2000 + int(raw_year)

e_month = raw_expiry[2:4]
e_day = raw_expiry[4:6]
###################################### Expiry END

print("Name:", name)
print("ID no.", IC_number)
print("Nationaliy:", nationality)
print("Date of Birth:", dob_day, dob_month, dob_full_year)
print("Gender:", sex)
print("Date of Expiry:", e_day, e_month, e_full_year)
# print(raw_dob)
# print(raw_expiry)

data = {
    "Name": name,
    "ID_no": IC_number,
    "Nationality": nationality,
    "Date_of_Birth": f"{dob_day}-{dob_month}-{dob_full_year}",
    "Gender": sex,
    "Date_of_Expiry": f"{e_day}-{e_month}-{e_full_year}"
}

print(json.dumps(data, indent=2))
json_output = json.dumps(data, indent=2)