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
      "\nIt is based on weighted votes from selected musicians, critics, and industry figures, and compiled into a list by the music magazine 'The Rolling Stone'.\n" + "*" * 70 + "\n")


def main_menu():
    while True:
        menu_choice = input(
            "\n----  MAIN MENU ----\n\n1. See the whole list\n2. Analysis options\n3. Make your own list\n4. Add album(s) to existing list\n5. Quit\n")
        if menu_choice == "1":
            print(tabulate(albumlist, headers=[
                  "Number", "Year", "Album", "Artist", "Genre"]))
            main_menu()
        elif menu_choice == "2":
            analysis_options()
            break
        elif menu_choice == "3":
            new_list()
            break
        elif menu_choice == "4":
            add_to_list()
            break
        elif menu_choice == "5":
            break
        print("\nInvalid option, please try again.")

def analysis_options():
    while True:
        print("\n ---- ANALYSIS OPTIONS ---- \n1. Search for artist\n2. Get top 10 list\n3.",
              "Get most occuring genre per decade\n4. Main menu")
        menu_choice = input()
        if menu_choice == "1":
            search_artist()
        elif menu_choice == "2":
            get_top_10()
        elif menu_choice == "3":
            print("Decade  -  Artist")
            #most_occurring_per_decade()
        elif menu_choice == "4":
            main_menu()
        
        print("\nInvalid option, please try again.")

def search_artist():
    
    q = input("Enter an artist or a band: ").lower()
    a = [row for row in albumlist if row[3].lower() == q]
    print(tabulate(a, headers=["Placement", "Year", "Album", "Artist", "Genre"]))
    analysis_options()

def get_pct(int):
    """
    Takes a value and turns it in to a percentage of the 500 placements
    """
    pct = int / 500 * 100
    return pct

def get_int(tuple):
    """
    Takes a list of tuples and gets the second value of the first tuple
    """
    tup = tuple[0]
    i = tup[1]
    return i

def top_10_artist():
    """
    Counts the number of values in the 4th(artist) column and prints the 10 most common artists in a table
    and a line presenting the most popular artist and the percentage of their placements
    """
    artist_count = Counter(worksheet.col_values(4)).most_common(10)
    top_1_artist = artist_count[0]
    print(tabulate(artist_count, headers=["Artist", "No. of placements"]))
    print(
        f"\nThe most popular artist was {top_1_artist[0]} with {get_pct(get_int(artist_count))}% of placements")
    get_top_10()

def top_10_year():
    """
    Counts the number of values in the 2nd(year) column and prints the 10 most common years in a table
    and a line presenting the most popular year and the percentage of its placements
    """
    year_count = Counter(worksheet.col_values(2)).most_common(10)
    top_1_year = year_count[0]
    top_1_year_int = top_1_year[1]
    print(tabulate(year_count, headers=["Year", "No. of placements"]))
    print(
        f"\nThe most popular year was {top_1_year[0]} with {get_pct(top_1_year_int)}% of placements")
    get_top_10()

def top_10_decade():

    """ 
    Converts the years into ints, extracts the decades and puts them into a list
    and prints a top list of the decades represented
    """

    years = worksheet.col_values(2)
    ints = [eval(i) for i in years]
    decades = []
    for each in ints:
        decade = int(np.floor(each / 10) * 10)
        decades.append(decade)
    d_counter = Counter(decades)
    d_most_common = d_counter.most_common(7)
    top_decade = d_most_common[0]
    top_decade_int = top_decade[1]
    print(type(top_decade_int))
    print("\nSince there are only 7 decades represented in the list, this is a top 7 list:\n")
    print(tabulate(d_most_common, headers=["Decade", "No. of placements"]))
    print(
        f"\nThe most popular decade was {top_decade[0]} with {get_pct(top_decade_int)}% of placements")
    get_top_10()

def top_10_genre():
    """ 
    Counts the number of values in the 5th(year) column and prints the 10 most common genres in a table
    and a line presenting the most popular genre and the percentage of its placements
    """
    genre_count = Counter(worksheet.col_values(5)).most_common(10)
    print(type(genre_count))
    top_1_genre = genre_count[0]
    top_1_genre_int = top_1_genre[1]
    print(tabulate(genre_count, headers=["Genre", "No. of placements"]))
    print(
        f"\nThe most popular genre was {top_1_genre[0]} with {get_pct(top_1_genre_int)}% of placements")
    get_top_10()

def get_top_10():
    """
    The menu for "Get top 10 lists"
    """
    while True:
        print("\n---- TOP 10 LISTS ----\n1. Artist\n2. Year\n3. Decade\n4. Genre\n5. Back\n6. Main menu")
        menu_choice = input()
        if menu_choice == "1":
            top_10_artist()
        elif menu_choice == "2":
            top_10_year()
        elif menu_choice == "3":
            top_10_decade()
        elif menu_choice == "4":
            top_10_genre()
        elif menu_choice == "5":
            analysis_options()
        elif menu_choice == "6":
            start_menu()
        print("\nInvalid option, please try again.")

def add_to_list():
    print("Select a worksheet to add an album to:\n")
    sheet_list = []
    for spreadsheet in SHEET.worksheets():
        sheet_list.append(spreadsheet.title)
    num = 0
    for sheet in sheet_list:
        num += 1
        print(f"{num}. {sheet}")
    choice = input()
    choice = int(choice)
    selected_ws = ""
    for i in sheet_list:
        if choice == i:
            selected_ws = sheet_list[choice]
    print(selected_ws)
    
        

def new_list():
    list_name = input("Enter a name for your list:")
    new_ws = SHEET.add_worksheet(title=list_name, rows=500, cols=5)
    add_album(new_ws)

def add_album(ws):
    new_ws = ws
    while True:
        new_row = []
        while True:
            try:
                placement = int(input("Enter a placement (a number between 1 and 500): "))
            except ValueError:
                print("Invalid input, try again.")
                continue
            if placement > 500 or placement < 1:
                print("Placement must be a number between 1 and 500.")
                continue
            else:
                break
        new_row.append(placement)
        while True:
            try:
                year = int(input("Year: "))
            except ValueError:
                print("Invalid input, try again.")
                continue
            if year > 9999 or year < 1000:
                print("Must be a 4 digit year.")
                continue
            else:
                break
        new_row.append(year)
        while True:
            try:
                name = input("Album name: ")
            except ValueError:
                print("Invalid input, try again.")
                continue
            else:
                break
        new_row.append(name)
        while True:
            try:
                artist = input("Artist/band: ")
            except ValueError:
                print("Invalid input, try again.")
                continue
            else:
                break
        new_row.append(artist)
        while True:
            try:
                genre = input("Genre:")
            except ValueError:
                print("Invalid input, try again.")
                continue
            else:
                break
        new_row.append(genre)
        new_ws.append_row(new_row)
        print(f"\nNew album added to worksheet {new_ws.title}")


start_menu()
