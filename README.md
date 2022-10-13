# Midterm_project

## About Us

We are L'avant Garde with the following Group members:
- Azzuhri Nauli Pasaribu - 2006489634
- Dhiwa Arya Kusumah - 2106657115
- Muhammad Fiqo Anugrah - 2106657286
- Linnea Alija Khan - 2206022405
- Julian Justin Orvino - 2106720903

## Deployment Link

https://midterm-project-pbp.herokuapp.com

## Description

In this application we want to bring up the topic that is discussed in the current
G20 summit that took place in Bali. The first thing that we will cover is a general overview about what digitalization and innovation is also their importance. Also followed by the example of digitalization and what sectors are more important to digitalize. Additionally, we will provide news/information about what are the digitalization and innovation issues that are talked about in G20 and what is the possible outcome that can affect our future. 

The main point of this application is to educate and inform people as well as facilitate discussions about the current events in the world most specifically that are related to the G20's countries in a way that can be learned easily and widely accepted. This application also creates a community to help boost digitalization and build non-governmental innovation.


## List of modules

- Authentication (Login, Logout, Make an Account)
- Article (Next Production Revolution, AI-related, manymore)
- Forum(Comment)
- Quiz (True and False in form of cards)
- Navbar (Home,Forum,Quiz, About Us)
- About us (Contact Us,etc)



## How to Build, Run and Deploy

How to Build, Run, and Deploy our app:
The building, running and deployment of this app is automated by using A CI/CD script implemented through Github actions. As such, to do it yourself, do the following:

1. Fork this github repository

2. Add Github secrets  HEROKU_API_KEY and HEROKU_APP_NAME with values of your  heroku api key and heroku app name respectively.

3. Run the Deploy workflow

After doing these steps, the application will be deployed to the heroku app specified in github Secrets.

## User Roles
- Azzuhri Nauli Pasaribu = Authentication
- Dhiwa Arya Kusumah = Article
- Muhammad Fiqo Anugrah = Quiz
- Julian Justin = Forum
- Linnea Alija Khan= Navbar, About us
