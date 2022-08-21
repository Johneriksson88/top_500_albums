import gspread
from tabulate import tabulate
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('albumlist')

worksheet = SHEET.worksheet('albumlist')
albumlist = worksheet.get_all_values()

print("*" * 70 + "\n\n" + "Welcome to a program for analysis of The Rolling Stones top 500 albums list.\nThe list was published in 2003 with a slight update 2012.", \
    "\nIt is based on weighted votes from selected musicians, critics, and industry figures, and compiled into a list by the music magazine 'The Rolling Stone'.\n\n" + "*" * 70 + "\n")

def start_menu():
    choice_1 = int(input("Type in 1 to see the whole list, 2 to see analysis options: "))
    try:
        if choice_1 == 1:
            print(tabulate(albumlist, headers=["Number","Year", "Album", "Artist", "Genre"]))
        elif choice_1 == 2:
            print("Analysis options")