import gspread
from tabulate import tabulate
from google.oauth2.service_account import Credentials
from collections import Counter
import numpy as np

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


def start_menu():
    while True:
        menu_choice_1 = input(
            "Type in 1 to see the whole list, 2 to see analysis options: ")
        if menu_choice_1 == "1":
            print(tabulate(albumlist, headers=[
                  "Number", "Year", "Album", "Artist", "Genre"]))
            break
        elif menu_choice_1 == "2":
            analysis_options()
            break
        print("Input must be 1 or 2, try again.")

def analysis_options():
    while True:
        print("\nMake one of the following choices:\n1. Search for artist\n2. Get top 10 list of a given parameter\n3.",
        "Get most occuring genre per decade\n4. Add your own album(s) to the list")
        get_top_10()
        break
"""
def search_artist():
    artists = worksheet.col_values(4)
    
    requested_artist = input(("Enter an artist or band: "))
    matches = []
    for match in artists:
        if requested_artist in match:
            matches.append(match)
    print(matches)
"""

def get_top_10():
    print("\nChoose a variable to see a top 10 list of:\n1. Artist\n2. Year\n3. Decade\n4. Genre")
    menu_choice_2 = input()
    
    if menu_choice_2 == "1":
        artist_count = Counter(worksheet.col_values(4))
        top_10_artist = artist_count.most_common(10)
        print(tabulate(top_10_artist, headers=["Artist", "No. of placements"]))

    elif menu_choice_2 == "2":
        year_count = Counter(worksheet.col_values(2))
        top_10_years = year_count.most_common(10)
        print(tabulate(top_10_years, headers=["Year", "No. of placements"]))

    elif menu_choice_2 == "3":
        years = worksheet.col_values(2)
        ints = [eval(i) for i in years]
        decades = []
        for each in ints:
            decade = int(np.floor(each / 10) * 10)
            decades.append(decade)
        dec_counter = Counter(decades)
        print(dec_counter)
        


start_menu()
