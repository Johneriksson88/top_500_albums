# Top 500 albums analysis program

The top 500 albums analysis program is a terminal based program that lets the user gleen insights from The Rolling Stone Greatest 500 Albums Of All Time list. It provides the user with static analysis of trends in the list, a search function, and also allows for adding new lists that the user can add any albums they please to.

![r500](https://github.com/Johneriksson88/top_500_albums/blob/main/assets/images/rolling_stone.jpg?raw=true)

## Features 

### Existing Features

- __Welcome text__

  - The user is greeted by a welcome text explaining what The Rolling Stone Greatest 500 Albums Of All Time list is and how to go forward in the program.

- __Main menu__

  - The main menu, which can be reached from all sub-menus, lets the user go forward in the program. It has the options View list, Analysis options, Make your own list, Add album(s) to list and quit, which shuts the program down.

  ![Main Menu](https://github.com/Johneriksson88/top_500_albums/blob/main/assets/images/main_menu.png?raw=true)

  - __View lists__

    ![View Lists](https://github.com/Johneriksson88/top_500_albums/blob/main/assets/images/view_lists.png?raw=true)

    - The view lists menu gives the user two options: to view the original Rolling Stone top 500 albums list or view a list which displays the user created worksheets. The data is presented in the terminal in a graphic table.

    ![View user list](https://github.com/Johneriksson88/top_500_albums/blob/main/assets/images/view_user_list.png?raw=true)

  
  - __Analysis options__

    ![Analysis Options](https://github.com/Johneriksson88/top_500_albums/blob/main/assets/images/analysis_options.png?raw=true)

    - The analysis options menu lets the user either search the original list by artist, or go into the Get top 10 lists menu.

      - __Search by artist__
      
        - Here the user can search the original Rolling Stone list by artist name, and have the all the albums of that artist/band on the list displayed in a tabulated format.

      - __Get top 10 lists__

       - Here the user can choose to see a static top 10 list over the most represented artist, years, decades and genres.
       - Note that the top list for decades only contains 7 decades since there are no more decades represented.


  - __Make your own list__

    - Lets the user create a new worksheet in order to create their own toplist of albums.
    - Gives the user the option to directly start adding albums to the new list.
  

  - __Add album(s) to existing list__

    - Lets the user add albums to a user created list.
    - Note that the user cannot add any albums to the original Rolling Stones list.


### Features Left to Implement

- Extend search function to all columns (placement, year, album name and genre) and also to all worksheets.
- More advanced static analysis, like for example most popular genre per decade

## Planning

The planning started with finding an interesting piece of data to analyze. I looked through numbers of surveys on [Data.world](https://data.world/) and on [Kaggle](https://www.kaggle.com/). Being a music lover and a musician i chose the The Rolling Stone Greatest 500 Albums Of All Time list.
Next i made a flowchart on [Lucidchart](https://lucid.app/).

![flowchart](https://github.com/Johneriksson88/top_500_albums/blob/main/assets/images/flowchart.png?raw=true)

During developing the program and testing, more ideas came to be implemented in the program and some original ideas removed so the flowchart is an original representation of the idea, but does not fully correspond to the finished project. For example the "view most occurring per decade" option was removed.

## Testing 

The program was continuosly tested essentially every new few lines of code, to catch errors as soon as possible. 
I let my mentor, friends and family test the program to give input regarding understadability and presentation.
Before deployment i went through every menu and every input statement to make sure the validation caught every kind of erroneus or empty input. Alot of experimenting with while-loops was done to get the optimal flow of input validation in both presentation and readability of code.
For example, i only in the end realized that there was an APIError when trying to add a new worksheet (list) with an existing name.

### Validator Testing 

The code was put through [The pep8online validator](http://pep8online.com/) and only generated the errors "Line too long", which I've learned from others does not affect the functionality of the code.

### Unfixed Bugs

When running the program in the browser terminal interface through Heroku, the number of lines in the tabulated presentation of the top original top 500 list exceeds the number of scrollable lines in the browser terminal. This means that the user won't be able to see placements 1-43. However, this was not anticipated in the inception of this project and when i realized this, at the very end of the project, it was simply too late to go back. Since all testing up to the point of deployment was done in the GitPod terminal and it worked there, this is by no means a flaw of this program, but rather of the browser terminal used to present the project, of which i have no control.
The lesson i learned by this is to in the future start by deploying first and do the testing in the end environment.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to Heroku. The steps to deploy are as follows: 
  - In the Heroku dashboard, click create app and name the app accordingly. 

  - While in the project page, go to Settings tab.
    - Click Reveal config vars and add two config vars:
      | Key | Value |
      --- | ---
      PORT | 8000
      CREDS | contents of the creds.json-file

    - Go to the Buildpacks section and click add buildpack.
      - Add python and node.js.
      - It's important that the buildpacks show up in this order: python on top and nodejs below. If not, drag python on top using the hamburger icon on the left of the buildpack.

  - Go to the Deploy tab.
    - Select GitHub as deployment method
    - In the Connect to GitHub section, search for your repository name and click connect.
    - Scroll down to the deploy sections. If desired click Enable Automatic Deploys (this will automatically deploy every time you push a new change to GitHub)
    - I chose to manually deploy, which is below Automatic Deploys. This will deploy the project.

The live link can be found here - https://top-500-albums.herokuapp.com/ 


## Credits 

### Content 

- The original Rolling Stone Greatest 500 Albums list was created by:
Jonathan Bernstein, Pat Blashill, Jon Blistein, Nathan Brackett, David Browne, Anthony DeCurtis, Matt Diehl, Jon Dolan, Chuck Eddy, Ben Edmonds, Gavin Edwards, Jenny Eliscu, Brenna Ehrlrich, Suzy Exposito, David Fricke, Elisa Gardner, Holly George-Warren, Andy Greene, Kory Grow, Will Hermes, Brian Hiatt, Christian Hoard, Charles Holmes, Mark Kemp, Greg Kot, Elias Leight, Joe Levy, Angie Martoccio, David McGee, Chris Molanphy, Tom Moon, Jason Newman, Rob O’Connor, Park Puterbaugh, Jody Rosen, Austin Scaggs, Karen Schoemer, Bud Scoppa, Claire Shaffer, Rob Sheffield, Hank Shteamer, Brittany Spanos, Rob Tannenbaum, David Thigpen, Simon Vozick-Levinson, Barry Walters, Jonah Weiner

- The [CSV-file](https://www.kaggle.com/datasets/notgibs/500-greatest-albums-of-all-time-rolling-stone) was downloaded from [kaggle.com](https://www.kaggle.com) and created by user [gibs](https://www.kaggle.com/notgibs).
