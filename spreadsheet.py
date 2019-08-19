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


id = 0


def add_new_note(note):
    new_row = [id, note]
    sheet.append_row(new_row)


def get_all_notes():
    all_notes = sheet.col_values(2)
    pp.pprint(all_notes)
