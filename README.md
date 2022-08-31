# Top 500 albums analysis program

The top 500 albums analysis program (henceforth referred to as T5-AAP) is a terminal based program that lets the user gleen insights from the Rolling Stone top 500 albums list. It provides the user with static analysis of trends in the list, a search function, and also allows for adding new lists that the user can add any albums they please to.
![r500](/workspace/top_500_albums/assets/images/rolling_stone.jpg)

## Features 

In this section, you should go over the different parts of your project, and describe each in a sentence or so. You will need to explain what value each of the features provides for the user, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

### Existing Features

- __Welcome text__

  - The user is greeted by a welcome text explaining what the top 500 albums list is and how to go forward in the program.

- __Main menu__

  ![Main Menu](/workspace/top_500_albums/assets/images/main_menu.png)

  - The main menu, which can be reached from all sub-menus, lets the user go forward in the program. It has the options View list, Analysis options, Make your own list, Add album(s) to list and quit, which shuts the program down.

  - __View lists__

    ![View Lists](/workspace/top_500_albums/assets/images/view_lists.png)

    - The view lists menu gives the user two options: to view the original Rolling Stone top 500 albums list or view a list which displays the user created worksheets. The data is presented in the terminal in a graphic table.
  
  - __Analysis options__

    ![Analysis Options](/workspace/top_500_albums/assets/images/analysis_options.png)

    - The analysis options menu lets the user either search the original list by artist, or go into the Get top 10 lists menu.

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

The planning started with finding an interesting piece of data to analyze. I looked through numbers of surveys on [Data.world](https://data.world/) and on [Kaggle](https://www.kaggle.com/). Being a music lover and a musician i chose the "Rolling Stone top 500 greatest albums of all time".
Next i made a flowchart on [Lucidchart](https://lucid.app/).



## Testing 

The program was continuosly tested essentially every new few lines of code, to catch errors as soon as possible. 
I let my mentor, friends and family test the program to give input regarding understadability and presentation.
Before deployment i went through every menu and every input statement to make sure the validation caught every kind of erroneus or empty input. Alot of experimenting with while-loops was done to get the optimal flow of input validation in both presentation and readability of code.
For example, i only in the end realized that there was an APIError when trying to add a new worksheet (list) with and existing name.

### Validator Testing 

The code was put through [The pep8online validator](http://pep8online.com/) and only generated the errors "Line too long", which I've learned from others does not affect the functionality of the code.

### Unfixed Bugs

When running the program in the browser terminal interface through Heroku, the number of lines in the tabulated presentation of the top original top 500 list exceeds the number of scrollable lines in the browser terminal. This means that the user won't be able to see placements 1-43. However, this was not anticipated in the inception of this project and when i realized this, at the very end of the project, it was simply too late to go back. Since all testing up to the point of deployment was done in the GitPod terminal and it worked there, this is by no means a flaw of this program, but rather of the browser terminal used to present the project, of which i have no control.
The lesson i learned by this is to in the future start by deploying first and do the testing in the end environment.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to Heroku. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


## Credits 
https://www.kaggle.com/datasets/notgibs/500-greatest-albums-of-all-time-rolling-stone
In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 

You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site


Congratulations on completing your Readme, you have made another big stride in the direction of being a developer! 

## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process! 