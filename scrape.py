import pandas
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandasql as ps
from gspread_dataframe import set_with_dataframe

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

#TODO: use techlab email credentials. ALSO make sure you share the google document with your service account email.
credentials = ServiceAccountCredentials.from_json_keyfile_name('auth.json', scope)

gc = gspread.authorize(credentials)


#TODO: enter URLS
# ENROLLMENT & CHARGE SHEETS URL
sheet1_url = ""

# SCHEDULE SHEET URL
sheet2_url = ""

# Integrated view sheet URL - URL for your output sheet
int_sheet_url = ""


sheet = gc.open_by_url(sheet1_url)
schedule_sheet = gc.open_by_url(sheet2_url)
int_sheet = gc.open_by_url(int_sheet_url)


summer = sheet.worksheet("summer_enrollment")
charge = sheet.worksheet("charge")
schedule = schedule_sheet.worksheet("schedule")

#write
integrated_view_sheet = int_sheet.worksheet("integrated-view")

enrollment_df = pandas.DataFrame(summer.get_all_records())
charge_df = pandas.DataFrame(charge.get_all_records())
schedule_df = pandas.DataFrame(schedule.get_all_records())



#print(schedule_df)

subquery = "SELECT enrollment_df.name, schedule_df.course, schedule_df.start, schedule_df.end, enrollment_df.charge FROM enrollment_df INNER JOIN schedule_df ON enrollment_df.session = schedule_df.uid"
query = "SELECT sub.name, sub.course, sub.start, sub.end, charge_df.name AS parent_name, charge_df.amount, charge_df.email FROM (" + subquery + ") sub INNER JOIN charge_df ON sub.charge = charge_df.charge"

query_df = ps.sqldf(query, locals())
print(query_df)
set_with_dataframe(integrated_view_sheet, query_df)
print("WROTE TO SHEET")

