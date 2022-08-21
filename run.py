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

print("*" * 70 + "\n\n" + "Welcome to a program for analysis of The Rolling Stones top 500 albums list.\nThe list was published in 2003 with a slight update 2012.",
      "\nIt is based on weighted votes from selected musicians, critics, and industry figures, and compiled into a list by the music magazine 'The Rolling Stone'.\n\n" + "*" * 70 + "\n")

"""
def validate_menu_choice(menu_choice_1):
    try:
        if menu_choice_1 != 1 or menu_choice_1 != 2:
            raise ValueError(
                f"Choice can only be 1 or 2, you provided {menu_choice_1}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again\n")
        return False
    return True
"""


def start_menu():
    while True:
        menu_choice_1 = input(
            "Type in 1 to see the whole list, 2 to see analysis options: ")
        if menu_choice_1 == "1":
            print(tabulate(albumlist, headers=[
                  "Number", "Year", "Album", "Artist", "Genre"]))
            break
        elif menu_choice_1 == "2":
            print("Analysis options")
            break
        print("Invalid input, try again.")

def analysis_options():
    
start_menu()
