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


def main_menu():
    """
    Function that starts the program, and shows the menu choices to go forward in the program.
    """
    while True:
        menu_choice = input(
            "\n----  MAIN MENU ----\n\n1. See the whole list\n2. Analysis options\n3. Make your own list\n4. Add album(s) to existing list\n0. Quit\n")
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
        elif menu_choice == "0":
            break
        print("\nInvalid option, please try again.")


def analysis_options():
    """
    Menu for the two analysis options: Search artist and Get top 10 lists.
    """

    print("\n ---- ANALYSIS OPTIONS ---- \n1. Search for artist\n2. Get top 10 lists\n0. Main menu")
    while True:
        menu_choice = input("Enter menu choice: \n")
        if menu_choice == "1":
            search_artist()
        elif menu_choice == "2":
            get_top_10()
        elif menu_choice == "0":
            main_menu()
        print("\nInvalid option, please try again.")


def search_artist():
    """
    Lets the user search the top 500 album list for an artist/band, and then shows a tabulated list of 
    all the instances of placements on the top 500 list of that artist/band.
    Converts input and strings it reads to lower case to make it more versatile.
    """
    print("\nHere you can search for an artist or band and see a list of the album(s) they have on the list.\nInput can be lower case.\n")
    while True:    
        while True:
            q = input("Enter an artist or a band: \n").lower()
            if len(q) == 0:
                print("Input cannot be empty, please try again.")
                continue
            else:
                break
        a = [row for row in albumlist if row[3].lower() == q]
        if not a:
            print("No such artist/band, please try again.")
            continue
        else:
            print(tabulate(a, headers=["Placement",
            "Year", "Album", "Artist", "Genre"]))
            while True:
                choice = input("1. Search again\n2. Back to analysis options\n0. Main menu\n")
                if choice == "1":
                    break
                elif choice == "2":
                    analysis_options()
                elif choice == "0":
                    main_menu()


def get_pct(int):
    """
    Takes a value and returns its percentage out of the 500 placements.
    """
    pct = int / 500 * 100
    return pct


def top_10_artist():
    """
    Counts the number of values in the 4th(artist) column and prints the 10 most common artists in a table
    and a line presenting the most popular artist and the percentage of their placements
    """
    artist_count = Counter(worksheet.col_values(4)).most_common(10)
    shared_first_place = []
    # Loop through top 10 artists to find if there are shared first places
    for x, y in artist_count:
        if y in artist_count[0]:
            shared_first_place.append(x)
    artist, no_placements = artist_count[0]
    print(tabulate(artist_count, headers=["Artist", "No. of placements"]))
    print(
        f"\nThe most popular artists were {', '.join(shared_first_place)} with {get_pct(no_placements)}% of placements each")


def top_10_year():
    """
    Counts the number of values in the 2nd(year) column and prints the 10 most common years in a table
    and a line presenting the most popular year and the percentage of its placements
    """
    year_count = Counter(worksheet.col_values(2)).most_common(10)
    top_1_year = year_count[0]
    year, no_placements = top_1_year
    print(tabulate(year_count, headers=["Year", "No. of placements"]))
    print(
        f"\nThe most popular year was {top_1_year[0]} with {get_pct(no_placements)}% of placements")


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
    decade, no_placements = top_decade
    print("\nSince there are only 7 decades represented in the list, this is a top 7 list:\n")
    print(tabulate(d_most_common, headers=["Decade", "No. of placements"]))
    print(
        f"\nThe most popular decade was {decade} with {get_pct(no_placements)}% of placements")


def top_10_genre():
    """
    Counts the number of values in the 5th(year) column and prints the 10 most common genres in a table
    and a line presenting the most popular genre and the percentage of its placements
    """
    genre_count = Counter(worksheet.col_values(5)).most_common(10)
    print(type(genre_count))
    top_1_genre = genre_count[0]
    genre, no_placements = top_1_genre
    print(tabulate(genre_count, headers=["Genre", "No. of placements"]))
    print(
        f"\nThe most popular genre was {genre} with {get_pct(no_placements)}% of placements")


def get_top_10():
    """
    The menu for "Get top 10 lists"
    """
    while True:
        print("\n---- TOP 10 LISTS ----\n1. Artist\n2. Year\n3. Decade\n4. Genre\n5. Back\n0. Main menu")
        menu_choice = input("Enter menu choice: \n")
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
        elif menu_choice == "0":
            main_menu()
        else:
            print("\nInvalid option, please try again.")


def add_to_list():
    print("\nSelect a worksheet to add an album to:\n")
    worksheets = SHEET.worksheets()
    for num, ws in enumerate(worksheets[1:]):
        print(f"{num+1}. {ws.title}")
    choice = int(input("Enter the number of the list you'd like to add to: \n"))
    selected_ws = worksheets[choice]
    print(f"Selected {selected_ws.title}")
    add_album(selected_ws)


def new_list():
    list_name = input("Enter a name for your list: \n")
    new_ws = SHEET.add_worksheet(title=list_name, rows=500, cols=5)
    add_album(new_ws)


def add_album(ws):
    new_ws = ws

    new_row = []
    while True:
        try:
            placement = int(
                input("Enter a placement (a number between 1 and 500): \n"))
        except ValueError:
            print("Invalid input, try again.")
            continue
        if placement > 500 or placement < 1:
            print("Placement must be a number between 1 and 500.")
            continue
        elif str(placement) in new_ws.col_values(1):
            print("Placement already taken, try again.")
            continue
        else:
            break
    new_row.append(placement)
    while True:
        try:
            year = int(input("Year: \n"))
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
        name = input("Album name: \n")
        if len(name) == 0:
            print("Album name cannot be empty, try again.")
            continue
        else:
            break
    new_row.append(name)
    while True:
        artist = input("Artist/band: \n")
        if len(artist) == 0:
            print("Artist/band name cannot be empty, try again.")
            continue
        else:
            break
    new_row.append(artist)
    while True:
        genre = input("Genre: \n")
        if len(genre) == 0:
            print("Genre cannot be empty, try again.")
            continue
        else:
            break
    new_row.append(genre)
    new_ws.append_row(new_row)
    print(f"\nNew album added to worksheet {new_ws.title}\n")
    print("1. Add another album\n2. Main menu")
    choice = input("Enter menu choice: \n")
    while True:
        if choice == "1":
            add_album(ws)
        elif choice == "2":
            main_menu()
            break
        else:
            print("Invalid input, try again.")


if __name__ == "__main__":
    main_menu()
