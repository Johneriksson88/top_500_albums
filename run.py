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

print("*" * 70 + "\n\n" + "Welcome to a program for analysis of \
The Rolling Stones top 500 albums list.\nThe list was published \
in 2003 with a slight update 2012. \
\nIt is based on weighted votes from selected musicians, critics, \
and industry\nfigures, and compiled into a list by the music magazine \
'The Rolling Stone'.\n\n" + "*" * 70)

print("\nIn the menu below you can explore the options of this program.\n")


def main_menu():
    """
    Starts the program and shows the menu choices to go forward in the program.
    """

    print("\n----  MAIN MENU ----\n")
    print("1. View lists")
    print("2. Analysis options")
    print("3. Make your own list")
    print("4. Add album(s) to existing list")
    print("0. Quit\n")
    while True:
        menu_choice = input("Enter menu choice: \n")
        if menu_choice == "1":
            view_lists()
            break
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
    print("\n**** ANALYSIS OPTIONS ****\n")
    print("1. Search by artist\n2. Get top 10 lists\n0. Main menu")
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
    Lets the user search the top 500 album list for an artist/band, and then
    shows a tabulated list of all the instances of placements on the top 500
    list of that artist/band.
    Converts input and strings it reads to lower case to
    make it more versatile.
    """
    print("\n**** SEARCH BY ARTIST ****\n")
    print("Here you can search for an artist or band and see a list of"
          "the album(s) they have on the list.\nInput can be lower case.\n")
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
                choice = input(
                    "1. Search again\n2. Back to analysis options\n"
                    "0. Main menu\n")
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


def get_top_10():
    """
    The menu for "Get top 10 lists"
    """
    print("\nBelow you can find top 10 lists of the most popular",
          "artists/bands, years, decades and genres on the list.\n")
    print("\n---- TOP 10 LISTS ----\n")
    print("1. Artist\n2. Year\n3. Decade\n4. Genre\n5. Back\n0. Main menu")
    while True:
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


def top_10_artist():
    """
    Counts the number of values in the 4th(artist) column and prints the
    10 most common artists in a table
    and prints a line presenting the most popular artist and the percentage of
    their placements.
    """
    artist_count = Counter(worksheet.col_values(4)).most_common(10)
    shared_first_place = []
    # Loop through top 10 artists to find out if there are shared first places,
    # and add the artist sharing first place into list shared_first_place.
    for x, y in artist_count:
        if y in artist_count[0]:
            shared_first_place.append(x)
    artist, no_placements = artist_count[0]
    print(tabulate(artist_count, headers=["Artist", "Spots on the list"]))
    print(
        f"\nThe most popular artists were {', '.join(shared_first_place)}",
        f"with {get_pct(no_placements)}% each of spots on the list.")
    print("1. View another top 10 list\n0. Main menu\n")
    choice = input("Enter menu choice:\n")
    while True:
        if choice == "1":
            get_top_10()
        elif choice == "0":
            main_menu()
        else:
            print("Invalid input, please try again.")
            continue


def top_10_year():
    """
    Counts the number of values in the 2nd(year) column and prints the 10 most
    common years in a table and prints a line presenting the most popular year
    and the percentage of its placements.
    """
    year_count = Counter(worksheet.col_values(2)).most_common(10)
    top_1_year = year_count[0]
    year, no_placements = top_1_year
    print(tabulate(year_count, headers=["Year", "Spots on the list"]))
    print(
        f"\nThe most popular year was {top_1_year[0]} with",
        f"{get_pct(no_placements)}% of spots on the list.")
    print("1. View another top 10 list\n0. Main menu\n")
    choice = input("Enter menu choice:\n")
    while True:
        if choice == "1":
            get_top_10()
        elif choice == "0":
            main_menu()
        else:
            print("Invalid input, please try again.")
            continue


def top_10_decade():
    """
    Converts the years into ints, extracts the decades and puts them into a
    list and prints a list of the decades represented.
    At the end prints a line presenting the most popular decade and the
    percentage of its placements.
    """

    years = worksheet.col_values(2)
    ints = [eval(i) for i in years]
    decades = []
    # Loop thorugh the years, divide the year with 10 and round it down
    # (e.g. 1972 / 10 = 197.2 rounded down = 197),
    # multiplies it by 10 (197 * 10 = 1970) and puts it into
    # the list "decades".
    for each in ints:
        decade = int(np.floor(each / 10) * 10)
        decades.append(decade)
    d_counter = Counter(decades)
    d_most_common = d_counter.most_common(7)
    top_decade = d_most_common[0]
    decade, no_placements = top_decade
    print("\nSince there are only 7 decades represented in the list,",
          "this is a not a top 10 list:\n")
    print(tabulate(d_most_common, headers=["Decade", "Spots on the list"]))
    print(
        f"\nThe most popular decade was the {decade}s with",
        f"{get_pct(no_placements)}% of spots on the list.")
    print("1. View another top 10 list\n0. Main menu\n")
    choice = input("Enter menu choice:\n")
    while True:
        if choice == "1":
            get_top_10()
        elif choice == "0":
            main_menu()
        else:
            print("Invalid input, please try again.")
            continue


def top_10_genre():
    """
    Counts the number of values in the 5th(year) column and prints
    the 10 most common genres in a table and a prints
    a line presenting the most popular genre and
    the percentage of its placements.
    """
    genre_count = Counter(worksheet.col_values(5)).most_common(10)
    print(type(genre_count))
    top_1_genre = genre_count[0]
    genre, no_placements = top_1_genre
    print(tabulate(genre_count, headers=["Genre", "Spots on the list"]))
    print(
        f"\nThe most popular genre was {genre} with"
        f" {get_pct(no_placements)}% of spots on the list.")
    print("1. View another top 10 list\n0. Main menu\n")
    choice = input("Enter menu choice:\n")
    while True:
        if choice == "1":
            get_top_10()
        elif choice == "0":
            main_menu()
        else:
            print("Invalid input, please try again.")
            continue


def view_lists():
    """
    Shows a menu with the options to view the original Rolling Stone list
    or a user created list.
    """
    print("\n**** VIEW LISTS ****\n")
    print("1. View the Rolling Stone greatest 500 albums list")
    print("2. View a user created list")
    print("0. Main menu")
    while True:
        choice = input("Enter menu choice:\n")
        if choice == "1":
            print(tabulate(albumlist, headers=[
                  "Number", "Year", "Album", "Artist", "Genre"]))
            break
        elif choice == "2":
            print("\n**** SELECT LIST ****\n")
            worksheets = SHEET.worksheets()
            for num, ws in enumerate(worksheets[1:]):
                print(f"{num+1}. {ws.title}")
            while True:
                try:
                    choice = int(
                        input("Enter number for desired list:\n"))
                    selected_ws = worksheets[choice]
                except ValueError:
                    print("Invalid input, please try again.")
                    continue
                except IndexError:
                    print("Worksheet does not exist, please try again.")
                    continue
                else:
                    break
            print(tabulate(selected_ws.get_all_values(), headers=[
                  "Placement", "Year", "Album", "Artist", "Genre"]))
            break
        elif choice == "0":
            main_menu()
        else:
            print("Invalid input, please try again.")
            continue
    print("1. View another list\n0. Main menu\n")
    choice = input("Enter menu choice:\n")
    while True:
        if choice == "1":
            view_lists()
        elif choice == "0":
            main_menu()
        else:
            print("Invalid input, please try again.")
            continue


def add_to_list():
    """
    Lets the user add an album to an existing list.
    """
    print("\n**** ADD ALBUM TO EXISTING LIST ****\n")
    print("Select a worksheet to add an album to:\n")
    worksheets = SHEET.worksheets()
    # Loop thorugh the worksheets, skipping the original top 500 album list
    # (at index 0) since we don't want to add an album to the original list.
    for num, ws in enumerate(worksheets[1:]):
        print(f"{num+1}. {ws.title}")
    while True:
        try:
            choice = int(
                input("Enter number for desired list:\n"))
            selected_ws = worksheets[choice]
        except ValueError:
            print("Invalid input, try again.")
            continue
        except IndexError:
            print("Selected worksheet does not exist, try again.")
            continue
        else:
            break
    print(f"Selected {selected_ws.title}.")
    add_album(selected_ws)


def new_list():
    """
    Lets the user create a new list, and gives them the option to add an album
    to that list.
    """
    print("\n**** CREATE NEW LIST ****\n")
    while True:
        list_name = input("Enter a name for your list: \n")
        if len(list_name) == 0:
            print("List must have a name, please try again.")
            continue
        else:
            break

    try:
        new_ws = SHEET.add_worksheet(title=list_name, rows=500, cols=5)
        print(f"Created new list: {new_ws.title}\n")
    except gspread.exceptions.APIError:
        print(
            f"A sheet with the name {list_name} already exists. Please enter",
            "another name.")
        new_list()

    choice = input(f"1. Add an album to {new_ws.title}\n2. Main menu\n")
    if choice == "1":
        add_album(new_ws)
    elif choice == "2":
        main_menu()
    else:
        print("Invalid input, try again.")


def add_album(ws):
    """
    Is called either from the new_list function if the user chooses to add an
    album to the new list directly,
    or from the add_to_list function.
    Lets the user create a new row in chosen list, with 5 column values:
    placement, year, album name, artist/band and genre.
    """
    print("\n**** ADD ALBUM ****\n")
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
    print(f"\nAlbum {name} added to worksheet {new_ws.title}\n")
    print("1. Add another album\n0. Main menu")
    choice = input("Enter menu choice: \n")
    while True:
        if choice == "1":
            add_album(ws)
        elif choice == "0":
            main_menu()
            break
        else:
            print("Invalid input, try again.")


if __name__ == "__main__":
    main_menu()
