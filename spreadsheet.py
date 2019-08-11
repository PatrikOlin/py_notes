import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

creds = ServiceAccountCredentials.from_json_keyfile_name(
    'notes_secret.json', scope)

client = gspread.authorize(creds)

sheet = client.open('pynotes_notes').sheet1

pp = pprint.PrettyPrinter()

new_row = ['6', 'Testar att addera rad']
sheet.append_row(new_row)

all_notes = sheet.col_values(2)
pp.pprint(all_notes)
