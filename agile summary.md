# AGILE

For this project, I am using Agile methodology as a means of planning and tracking progress. This project would be run in Sprints of 6, with each sprint combining similar and related user stories, development and todo tasks. I will be using GitHub issues to create user stories and other tasks, using labels to designate which is which. I will be using GitHub milestones to create Sprints. Below is the summary of all sprints at the start of the project.

## Sprint Summary

### Sprint 1

This sprint will be all about planning the project. This will include the creation of user stories, ERD diagram for the database, setup for the Django project and linking the database to the project, and UI design. This sprint has been set to be completed on the same day.

### Sprint 2

This sprint will be all about populating the database with preliminary data. I will be using a MySQL database with various neccesary tables following the ERD created from Sprint 1. This sprint has been set to be completed on the day after Sprint 1.

### Sprint 3

This sprint will be all about designing the bulk of the frontend HTML and CSS code, and any required JavaScript code required for basic frontend performance. The design will follow the planned frontend design done in Sprint 1, and will run concurrently with Sprint 2, aimed to be completed on the day after Sprint 2.

### Sprint 4

This sprint will be all about the designing of the backend. This will also run concurrently with Sprints 2 and 3, due to the overlapping nature of some of it. This is meant to be completed 2 days after Sprint 3

### Sprint 5

This sprint will be all about testing and fixing any errors in the code, as well as updating the README markdown. This is meant to be completed on the day after Sprint 4.

### Sprint 6

This sprint will be all about deployment to Heroku, meant to be completed on the day after Sprint 5.


## Sprint Runs

### Sprint 1
The tasks in this sprint are:
- Scope planning
- Developing user stories
- ERD design
- UI design
- SQL database setup
- Django project setup.


#### Scope

MUST HAVE:
- Login and logout function
- Signup function
- Home page, welcome for all visitors
- About page, for contact information
- FAQ page, for commonly asked questions
- Our Gym page, to see the equipment and services given at the gym
- Profile page, to see your details (this will be restricted to logged in users only)
- Profile page to contain links to other pages such as "My Sessions" (for tracking workout sessions), "My PRs" (where user can record their PRs on certain exercises)
- Visitors are able to see the Home, About, FAQ and Our Gym pages, but cannot view Profile page if not logged in
- A button to simulate paying the first joining fee

SHOULD HAVE:
- "Plan My Workout" page in Profile page, where user can plan out their sessions and check into the session when they arrive at the gym
- "Book Personal Trainer" page in the Profile page, where user can select from a list of PTs and book one for a specific time
- Email confirmation for signup, check in and out to a workout session and booking of PT
- Cancel membership (de facto deletion of account)

COULD HAVE:
- Recommended workout song of the day


#### User Stories

As a user, I should:
- be able to create an account so I can become a member of the gym
- be able to view the homepage of the gym website so that I can get an idea of what is going on
- be able to view the FAQ page so that I can gain understanding of the commonly asked questions
- be able to see the about page, so I can get more information about the monthly price of the gym
- be able to see the about page, so I know the address of the gym
- be able to see the about page, so I know how to contact the gym either by phone, email or social media
- be able to click the payment simulation button so that I can officially join the gym

As a logged in user, I should:
- be able to log into my account using my username and password so I can access my profile details
- be able to change my password so that I can practice basic security
- be able to delete my account so that I can cancel my membership
- be able to access the "My Sessions" page so I can view and review my past workout sessions
- be able to access the "My Sessions" page so I can start and stop a new workout session with the things I'm training in that session
- be able to access the "My PRs" page so I can view my past PRs on various exercises
- be able to access the "My PRs" page so I can add a new PR to a specific exercise
- be able to access the "Plan My Workout" page so that I can plan my next workout
- be able to access the "Book Personal Trainer" page so that I can book an appointment with a PT

As an admin, I should:
- be able to view all registered users so I know who is a member of the gym
- be able to edit things in the database so that I can control what is displayed on the frontend


#### ERD Design

After coming up with the scope and the user stories, I created an entity relationship diagram, which would describe the various tables in 
the database and their relationships with each other. Some of these tables are standalone (i.e. not having any relationship with any other 
table) and some of these tables are in relationship with others. The relationships between the tables are one-to-many, with the use of foreign 
keys to link certain tables to the other. The full ERD can be found in the [README](./README.md) document.


#### UI Design

After creating the ERD, I began making a design for the user interface. This started with me coming up with a colour theme, and then a logo for 
the gym. I drew inspiration for the colour theme from the [JD Gyms](https://www.jdgyms.co.uk/) website (the gym that I go to), which generally 
uses a theme of green and grey. Using Figma, I designed the interface of some sample webpages of the gym.

However I soon ran into a bit of creator's block. I generally struggle with planning and I'm more proactive in the "coding" side of things, 
making things as I go along. This did cause me to spend a considerable amount of time thinking of and coming up with designs for the webpages, 
which ended up in me running over the time intended for Sprint 1 and getting into the time meant for Sprint 2. Eventually, I decided to begin 
working with what I had managed to get done eventually, and to work on other tasks concurrently with the design. This ended up in me moving 
the remainder of the tasks in Sprint 1 into Sprint 2.

The Figma sketch can be found [here](https://www.figma.com/design/GP25XAQJHQZZ4yP2yYRqTl/GainzCenter) and also in the [README](./README.md) document.




### Sprint 2
The tasks in this sprint are:
- UI design (brought over from Sprint 1)
- SQL database setup (brought over from Sprint 1)
- Django project setup (brought over from Sprint 1)
- SQL database population


#### UI Design

Due to reasons outlined above, this would run concurrently with other tasks as ideas came along to me. This was to enable me to work on other 
tasks without wasting any more time trying to come up with further designs for the UI. Hence upon the starting of this sprint I went straight 
to the SQL database setup.


#### SQL Database Setup

During the development of the website, I will be using a localhost instance on my PC as a server for the database, which would be deployed to the live 
hosting site along with the rest of the project. I am using MySQL Workbench as a tool to manage the database and its tables, making use of SQL 
commands to create the database and populating the preliminary data.

While creating the database, I ran into a bit of a hitch whilst creating the table for the personal trainers, as I was unsure that my ERD design was 
accurate in reflecting how availability and bookings would be stored. After doing some further brainstorming, I decided to have an extra table that would 
explicitly show the sessions with their availability and bookings, rather than in one table and then using the application to determine what slot 
is available and what isn't (as per the original plan). With this in mind, I updated the ERD to reflect this change.

I began with the tables that didn't have any foreign keys, so as to avoid any complications early on. I soon found out that I had forgotten to 
define some relationships amongst some tables in my ERD, so I made this correction to the diagram, hence further updating it. This proved 
helpful when I began to create the tables that had foreign keys, as some tables had up to 3 foreign keys and their relationship to other tables 
needed to be defined in the ERD.

I also realized that I should've defined a relationship between the MyPRs table and the Exercises table, since one would update their PR on a 
specific exercise (e.g. a new PR on bench press or deadlifts). I subsequently updated the ERD to reflect this.

All SQL commands used in creating and populating the table have been laid out in the SQL file [gainz-center-sql-commands](./gainz-center-sql-commands.sql).


#### Django Project Setup

After having set up the database, I then created the Django project. Running the relevant commands in my terminal, I setup the project and called it `gainz_center_project`. Within this project I created the app `gainz_center_app`, which is where the website will be located. I then created a user account within the MySQL instance with which the project will access the database to perform the required operations.


#### SQL Database Setup

After creating the Django project, I then started populating the database with preliminary data. I focused on populating the `FAQs`, `Equipment`, `Exercises`, `ExerciseTypes` and `PersonalTrainers` tables, as these are the prelimary tables that can stand alone without needing data from other aspects of the application. The other tables will be populated alongside the project, as this will require there to be at least 1 record of a user account.




### Sprint 3
The tasks in this sprint are:
- Creating the `static` and `template` directories
- Creating HTML, CSS and JavaScript for basic frontend functions
- Creating the Home, About, FAQ and Our-Gym pages


#### Creating Directories

This was a fairly easy task as I created the folders `static` and `templates`. These would hold the styles and JS files, and the HTML files respectively, which would be served by the Django backend. I created another folder `temporal-image-folder` within the `static` directory where i kept my images, as I was having issues with PostImg, whereby my computer was blocking access to the 
site because it believed that it was a potential source of malware and inappropriate content. I put my images there temporarily, with the aim of replacing the image elements with the hosted images once I resolved the issue with PostImg.


#### Designing Frontend

This was basically a combination of the last 2 tasks in this sprint. Following the initial designs created in Sprint 1, I proceeded 
to write HTML and CSS code to design the frontend of the Home, About, FAQ and Our-Gym pages. I also ensured to include responsive 
design, testing out the results with various sizes of my browser window, ensuring that it would still be readable to users with 
smaller screens. At the suggestion of a friend, I slightly adjusted the design whilst coding, ensuring that only headers had the `Irish Grover` font (the font used for the design) whilst all other text had a basic typeface font.

I also had to do a bit of backend coding in Django, as the FAQs would be pulled from the database, as well as the equipment 
to be displayed in the Our-Gym page. I defined models in [`models.py`](./gainz_center_app/models.py) that would be used to retrieve information from their respective databases, passed them through [`views.py`](./gainz_center_app/views.py) and brought them into their respective HTML pages.




### Sprint 4
The tasks in this sprint are: