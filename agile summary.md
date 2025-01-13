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


### User Stories

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