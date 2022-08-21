import gspread
from tabulate import tabulate
import pandas as pd
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

albumlist = SHEET.worksheet('albumlist')

print("*" * 70 + "\n\n" + "Welcome to a program for analysis of The Rolling Stones top 500 albums list.\nThe list was published in 2003 with a slight update 2012.", \
    "\nIt is based on weighted votes from selected musicians, critics, and industry figures, and compiled into a list by the music magazine 'The Rolling Stone'.\n\n" + "*" * 70 + "\n")

choice_1 = input("Type in 1 to see the whole list, 2 to see analysis options: ")
print(f"Choice was {choice_1}")

