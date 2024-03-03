![readme-header](https://github.com/0davidog/Umbra-Report/assets/135815736/8de51b7b-e160-437f-843c-e9a490cc37e6)

# The Umbra Report

- The Umbra Report is a blog dedicated to strange and unusual stories.
- Users are able to contribute stories with a supporting image while interacting with the posts of others through comments and likes.
- The site offers an opportunity for community around creative writing or perhaps even true stories.

## Live Site

The live app is hosted on ther Heroku platform. More details on how the project was deployed can be found below [here](#deployment).
- [Heroku Link](https://umbra-report-f975c52ec09c.herokuapp.com/)

## Repo

The project's code and file repository is hosted by Github. More details on cloning or forking the repository can be found [here](#repo).
- [Github link](https://github.com/0davidog/Umbra-Report)

## Author
David C. O'Gara

# Table of contents

- [The Umbra Report](#the-umbra-report)
  - [Live Site](#live-site)
  - [Repo](#repo)
  - [Author](#author)
- [Table of Contents](#table-of-contents)
  - [Agile Process](#agile-process)
    - [User Stories](#user-stories)
    - [Project Backlog](#project-backlog)
    - [Iteration 01 – Due 05/03/2024](#iteration-01--due-05032024)
- [UX](#ux)
  - [Project Goal](#project-goal)
  - [Target Audience](#target-audience)
  - [Wireframes](#wireframes)
  - [Information Architecture](#information-architecture)
    - [Entity Relationship Diagram](#entity-relationship-diagram)
    - [Database Choice](#database-choice)
    - [Data Models](#data-models)
      - [Report Model](#report-model)
      - [Comment Model](#comment-model)
      - [About Model](#about-model)
      - [User Model](#user-model)
  - [Design Choices](#design-choices)
    - [Title](#title)
    - [Thematic and visual inspiration](#thematic-and-visual-inspiration)
    - [Colors](#colors)
    - [Typography](#typography)
    - [Images](#images)
    - [Design Elements](#design-elements)
      - [Icons](#icons)
    - [Animations and Transitions](#animations-and-transitions)
    - [Frameworks](#frameworks)
    - [Custom Styles](#custom-styles)
    - [Custom Javascript](#custom-javascript)
  - [Features](#features)
    - [Implemented Features](#implemented-features)
      - [Navigation](#navigation)
      - [Create Report](#create-report)
      - [Read Report List](#read-report-list)
      - [Read Full Report Detail](#read-full-report-detail)
      - [Edit Report](#edit-report)
      - [Delete Report](#delete-report)
      - [Likes](#likes)
      - [Create Comments](#create-comments)
      - [Read Comments](#read-comments)
      - [Edit Comments](#edit-comments)
      - [Delete Comments](#delete-comments)
      - [Account Register](#account-register)
      - [Account Log-in/out](#account-log-inout)
      - [About Page](#about-page)
      - [User Page](#user-page)
      - [Admin Panel](#admin-panel)
    - [Future Features](#future-features)
  - [Testing](#testing)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
  - [Deployment](#deployment)
    - [Prerequisites](#prerequisites)
      - [ElephantSQL Database:](#elephantsql-database)
      - [Create Superuser](#create-superuser)
      - [Cloudinary](#cloudinary)
    - [Fork and Clone the Repository](#fork-and-clone-the-repository)
      - [Fork](#fork)
      - [Clone](#clone)
    - [Local Deployment](#local-deployment)
    - [Production Deployment](#production-deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgments](#acknowledgments)

## Agile Process

This project is to be made using Agile develpment pricipals to plan and complete the work to a minimum viable product. This involves seperating the work in to a project back log of user stories in which an iteration of the project (MVP) must be achieved by project deadline. 

### User Stories

Following Agile development practice this project has been divided into user stories to give a clear understanding of the project needs, goals and features and to split the work in to small achievable sets of tasks.

[User Stories on Github](https://github.com/0davidog/Umbra-Report/issues)

Here is a list of user stories for this project seperated in to their relative Epics. 
Each story links to its place on Github where you can view:
- User Story
- Acceptance criteria
- MSCW prioritisation label
- Linked iteration
- Linked project board.

**Epic: User Registration and Authentication** 

- [As a Site User, I want to register an account on the blog website so that I can create and manage my own posts.](https://github.com/0davidog/Umbra-Report/issues/1)
- [As a Site User, I want to log in to the website securely using my credentials so that I can participate in the blog’s features.](https://github.com/0davidog/Umbra-Report/issues/2)
- [As a Site user, I want the option to reset my password in case I forget it, ensuring secure access to my account.](https://github.com/0davidog/Umbra-Report/issues/3)

**Epic: Blog Post CRUD Management** 

- [As a Site User, I want to create a new blog post with a title, content, and optional images, so that I can share my thoughts and experiences.](https://github.com/0davidog/Umbra-Report/issues/4)
- [As a Site User, I want the ability to update my existing blog posts to update or improve the content over time.](https://github.com/0davidog/Umbra-Report/issues/5)
- [As a Site User, I want to be able to delete my own blog posts if I decide to remove them from the website.](https://github.com/0davidog/Umbra-Report/issues/6) 
- [As a Site User or Admin, I can create draft posts so that I can finish writing the content later.](https://github.com/0davidog/Umbra-Report/issues/7)
- [As a Site Admin I can manage all blog posts through the admin panel to maintain control over the site’s content.](https://github.com/0davidog/Umbra-Report/issues/8)

 **Epic: User Interaction and Engagement** 

- [As a Site User I can view a paginated list of posts so that I can select which post I’m interested in viewing.](https://github.com/0davidog/Umbra-Report/issues/9) 
- [As a Site User, I can click on a post so that I can view the complete content.](https://github.com/0davidog/Umbra-Report/issues/10) 
- [As a Site User or Admin, I can view the comments on each individual post so that I can read the conversation.](https://github.com/0davidog/Umbra-Report/issues/11) 
- [As a Site User, I want to be able to comment on blog posts to engage with the author and other readers.](https://github.com/0davidog/Umbra-Report/issues/12) 
- [As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments.](https://github.com/0davidog/Umbra-Report/issues/13) 
- [As a Site User, I want to be able to like blog posts to engage with the author and other readers.](https://github.com/0davidog/Umbra-Report/issues/14)
- [As a Site User, I want to receive notifications when someone likes or comments on my blog posts to stay informed about the engagement with my content.](https://github.com/0davidog/Umbra-Report/issues/15) 

**Epic: Search and Navigation** 

- [As a Site User, I want to search for specific blog posts or topics to quickly find the information I'm looking for.](https://github.com/0davidog/Umbra-Report/issues/16)
- [As a Site User, I want a user-friendly navigation menu that helps me explore different sections of the blog easily.](https://github.com/0davidog/Umbra-Report/issues/17) 

**Epic: Responsive Design and Accessibility** 

- [As a Site User, I want the blog website to be responsive, ensuring a seamless experience on various devices, including desktops, tablets, and smartphones.](https://github.com/0davidog/Umbra-Report/issues/18) 
- [As a Site User with accessibility needs, I want the website to be accessible, with features like alt text for images and keyboard navigation, to ensure a positive experience for all users.](https://github.com/0davidog/Umbra-Report/issues/19) 

**Epic: Additional information** 

- [As a Site User, I can click on the About link so that I can read about the site.](https://github.com/0davidog/Umbra-Report/issues/20)
- [As a Site Admin, I can create or update the about page content so that it is available on the site.](https://github.com/0davidog/Umbra-Report/issues/21)
- [As a Site User, I can click on a username link so that I can read about the user and see their posts.](https://github.com/0davidog/Umbra-Report/issues/22)

### Project Backlog

Due to the small scope of this project, having a project backlog and seperate iterations didn't seem neccessary as their would only be one project to client hand-over. It was instead decided to keep all the user stories in the one project iteration list. A project backlog milestone was created however on github to follow agile practice. You can view it [here](https://github.com/0davidog/Umbra-Report/milestone/2). 

### Iteration 01 – Due 05/03/2024

[Iteration on Github](https://github.com/0davidog/Umbra-Report/milestone/1)

As this is an accedemic porfolio project there is only one interation in which this project will be developed and tested. That being the project start date to it's hand-in date by which all its must-have deliverables are to be achieved. 

# UX

## Project Goal

The aim of The Umbra Report is to provide a space for users to share unusual stories, whether real or imagined as well as engage with the stories of others through comments, likes and uploading of related images.

## Target Audience

The target audience for this project are enthusiasts of horror stories, urban legends, 'creepypasta', ghost hunting and crytozoology. The site aims to be suitable for a wide-audience so meterial that is deemed inappropriate, harmful or 'not safe for work' will be filtered about by the site admin.

## Wireframes

Wireframes were created to plan the basic layout of the App.

![PP4_Wireframes_01](https://github.com/0davidog/Umbra-Report/assets/135815736/01047aec-8884-4768-b21e-991df04f8d91)
![PP4_Wireframes_02](https://github.com/0davidog/Umbra-Report/assets/135815736/b7131a71-138d-44db-a649-87d15354c754)

## Information Architecture

<details><summary>VIEW SECTION</summary>

### Entity Relationship Diagram

The diagram displayed here shows the relationship between the database models used in the project.
- The Report custom model links to the User through an author field. This is the site user that has created the report (blog post).
- The Report model also relates to the User model through the likes field. This is a many-to-many field as this allows a user to like multiple reports and a report to have multiple likes.
- The User model is Django's built in user authentication model and is linked to buy the other models.
- The Comment model links to the Report model as post (the subject of the comment) and the User model as author.
- The About model links to the User model as author. 

![Umbra ERD](https://github.com/0davidog/Umbra-Report/assets/135815736/a24df8af-8664-49b0-a92c-8dd79540d9fd)

### Database Choice

The project uses the PostgreSQL database installed and managed through the ElephantSQL service and the Psycopg2 database adapter for use with Python and Django. 
This is chosen as the project requires a relational database for interactivity between models.

### Data Models

#### Report Model

![model-report](https://github.com/0davidog/Umbra-Report/assets/135815736/a4f9a684-b34f-4d55-8357-7e88c05b6e9e)

The custom Report model is the model that acts as the site's blog post.

|DB Key|Data Type|Purpose|Additional Information|
|------|---------|-------|---------------|
|id(Primary Key)|IntegerField|Unique numerical identifier.|Automatically generated.|
|title|CharField|This is the title of each blog post.|Required. Has to be unique. Max character length is 250|
|slug|AutoSlugField|Slug is a string that can only include characters, numbers, dashes, and underscores. This is auto generated by the content of the title field via the Django library Autoslug.|Slug is editable.|
|author|ForeignKey|The is the author of the report linked to and represented by the User model.|On deletetion of linked User model post will also be deleted. Realted name is 'blog_posts'.|
|category|CharField|This allows a user to select a category for their report from a dropdown list.|CATEGORY_CHOICES = [("1", "True Story"),("2", "Urban Legend"),("3", "Creative Writing"),("4", "Creepypasta"),]|
|source|URLField|This in option to include a url if the report references work from elsewhere.|blank = True|
|featured_image|CloudinaryField|This field allows the user to upload an optional image as supporting content for the report and is done so by linking to the hosting service Cloudinary.|By default this field is set to 'placeholder' (as a string).|
|image_title|CharField|Optional field to input a title for the featured_image.|blank=True|
|image_author|CharField|Optional field to input an author for the featured_image.|blank=True|
|image_source|Charfield|Optional field to include URL if image referenced from elsewhere.|blank=True|
|content|TextField|This is the reports main text content.||
|description|CharField|This field is for a description, tagline or excerpt of the main text to be seen as a preview in the blog's index page.|This can be left blank by the user, in which case the site Admin can fill with appropriate information while reviewing. Max character length is 500.|
|status|IntegerField|This field uses a binary system (1 or 0) to represent whether the report is in draft or published status.|Set to 'published' by default.|
|created_on|DateTimeField|This field states the date and time the instance of report was created.|Automatically generated once when instance is created through 'auto_now_add'.|
|updated_on|DateTimeField|This field states the date and time the instance of report was last updated on.|Automatically generated each time the instance is updated via 'auto_now'.|
|approved|BooleanField|This field is a simple checkbox to mark whether the administrator has apporoved the content for publication.|Set to False (unapproved) by default.|
|likes|ManyToManyField|This field collects a list of Users who have given the page a 'like'.|Allowed to be blank by default.|

Report model contains two model functions.
- __str__(self): Returns string of Title and Author as '{self.title} by {self.author}' for admin display purposes.
- likes_number(self): Returns an integer of number of users who have liked the report.

- [x] Create - Registered users (see User model) are able to create a new report as author via a form on the site.
- [x] Read - Users both registered and unregistered can browse and read published reports.
- [x] Update - Registered and authenticated users are able to update/edit a report providing they are the author or administrator.
- [x] Delete - Registered and authenticated users are able to delete a report providing they are the author or administrator.

#### Comment Model

![model-comment](https://github.com/0davidog/Umbra-Report/assets/135815736/0546df73-8114-447f-9a46-25edafb9a545)

The Comment model represents a comment written on a report. This is based on the Comment model used in the Code Institute "I Think, Therefore I Blog" walkthrough project.

|DB Key|Data Type|Purpose|Additional Information|
|------|---------|-------|---------------|
|post|ForeignKey|Links to the Report model to specify which report is the subject of the comment.|Upon deletion of the referenced report instance the comment will also be deleted from the database.|
|content|TextField|This is the main text content of the comment.||
|approved|BooleanField|This is a checkbox to state whether the admin has deemed to content of the comment as suitable for publication.|Set to false (unapproved) by default.|
|created_on|DateTimeField|This field states the date and time the instance of comment was created.|Automatically generated once when instance is created through 'auto_now_add'.|
|updated_on|DateTimeField|This field states the date and time the instance of comment was last updated on.|Automatically generated each time the instance is updated via 'auto_now'.|

Comment model contains one model function.
- __str__(self): Returns string of comment content and author as "Comment: {self.content} by {self.author}".

- [x] Create - Registered users (see User model) are able to create a new comment as author via a form on the site.
- [x] Read - Users both registered and unregistered can browse and read published comments.
- [x] Update - Registered and authenticated users are able to update/edit a comment providing they are the author or administrator.
- [x] Delete - Registered and authenticated users are able to delete a comment providing they are the author or administrator.

#### About Model

![model-about](https://github.com/0davidog/Umbra-Report/assets/135815736/d087fcc6-2b1d-45e2-b204-0b22a5ea7ff6)

The About model represents a paragraph of text about the site. This is largely based on the About model used in the Code Institute "I Think, Therefore I Blog" walkthrough project.

|DB Key|Data Type|Purpose|Additional Information|
|------|---------|-------|---------------|
|title|CharField|The title of the about article.|Max character length of 200.|
|updated_on|DateTimeField|This field states the date and time the instance of comment was last updated on.|Automatically generated each time the instance is updated via 'auto_now'.|
|content|TextField|The main text portion of the about article.||

About model contains one model function.
- __str__(self): Returns string of title as "Title".

#### User Model

![model-user](https://github.com/0davidog/Umbra-Report/assets/135815736/1f86a8f3-cdf5-418e-ba4d-8bd041f9d155)

The User model is Django's buit in user authentication model. More information on this model can be found in the Django documentation [here](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/). Users can register for an account on the site through forms provided by Django [Allauth](https://docs.allauth.org/en/latest/).

A few notes on relevant fields.
- is_staff is a boolean field that states whether a registered user can access the admin panel. This is needed to approve posts and comments, update the about page and have an overall control of the content.
- is_superuser is a boolean field that grants a particular user all available privelidges, including staff status. The site creator registers as superuser during production.

</details>

## Design Choices

<details><summary>VIEW SECTION</summary>

### Title

The Umbra Report title was taken from music I was listening to at the time of developing ideas for the project. This was 'The Umbra Report', an album by 'Cities Last Broadcast'. I felt the title fit the theme of 'reports from the shadows' that I was going for. [Bandcamp](https://cryochamber.bandcamp.com/album/the-umbra-report)

### Thematic and visual inspiration

The app's theme is one of stories and urban legends, inspired by sites such as readit where various threads allow users to contribute stories of varied kinds and comment on each other's posts.

This theme was also part inspired by the game Control by Remedy Entertainment. The game's theme features an organisation that collects and investigates strange phenomena, objects and reports. I felt this was a fun theme on which to work this project around.

![IMG_0146](https://github.com/0davidog/Umbra-Report/assets/135815736/33505342-6923-4945-bbbc-5f43e15279c6)

This game seemed the perfect place to take inspiration for the visual design of the app also. From the mysterious background image pictured above to the UI design bellow. The red highlights, white text and use of symbols throughout was something I wanted to try in the visual design for this site.

![IMG_0142](https://github.com/0davidog/Umbra-Report/assets/135815736/9fc87002-e9f3-452f-81a7-5026fc683c13)

### Yamishibai: Japanese Ghost Stories

For fun, a small reference to the animated series Yamishibai (闇芝居, Yami Shibai, lit. Dark Play) is included at the end of each report with the question 'oshimai?' (おしまい?, eng. The End?). This is something the narrator asks at the end of each ghost story.

### Colors

![Umbra_Report_Palette](https://github.com/0davidog/Umbra-Report/assets/135815736/e969c1b4-47f5-49fc-a7a0-d7bc0939ac29)

- #ffffff Main body text is white allowing the text to stand out in contrast to the darker shades of the background colour.
- #800000 Dark red is used to highlight headlines, hyperlinks and important information such as warnings.
- #008080 Cyan is used as both a body background colour when the background image fails and as hover colour for anchor tags. 
- #000000 Black is used as a background shade to contrast the white, red, grey and cyan used throughout.
- #808080 Grey is used as a background to some buttons.
- UPDATE - Dark red(#800000) was changed to a lighter red (#BA0000) later in production. Though this didn't show up on any lighthouse or wave audits, it was found to be a contrast issue by a low decimal number on dev tool's contrast information. 

### Typography

- Oswald via [google-fonts](https://fonts.google.com/specimen/Oswald?query=oswal)
- Courier Prime via [google-fonts](https://fonts.google.com/specimen/Courier+Prime)

![PP4_fonts](https://github.com/0davidog/Umbra-Report/assets/135815736/de643af3-015d-46c6-9890-801da9e8ff59)

Oswald and Courier Prime were chosen to provide an appealing contrast between headings in Oswald and main body text in Courier. Courier in particular was chosen as it resembles a typewriter written document and suited the blog's themes of observation and reports.

### Images

A logo for the site, featured on the About page, was created. This represents the site's themes of observation and collaboration.

![umbra-logo](https://github.com/0davidog/Umbra-Report/assets/135815736/63f9f201-93e4-4daf-bda8-b0522240f240)

A background image was created for the site's main body. This represents the site's theme of the unknown and the unusual through its abstract and distorted appearance.

![SpacialCyanBG](https://github.com/0davidog/Umbra-Report/assets/135815736/12d0feca-51eb-4efc-8769-508946dcb991)

A user-image was created. This is a textured edit of a standard blank user image used to represent an anonymous reporter.

![blank_face](https://github.com/0davidog/Umbra-Report/assets/135815736/b75e0c0f-457d-4ada-97a7-6a8ced3d20a6)

### Design Elements

#### Icons

Icons are used throughout the site and are sourced from [fontawesome](fontawesome.com/). See [credits] for a full list.

### Animations and Transitions

- A CSS transform is applied to buttons as a hover state that increases their size to 1.1 scale.

### Frameworks

- Bootstrap is used thoughout this project to allow for a quick development of a site that is responsive and stylised with a greatly reduced amount of code.

### Custom Styles

Custom CSS was added where necessary to create a more personalised look to the site on top of Boostrap's default styles. The file can be viewed [here](https://github.com/0davidog/Umbra-Report/blob/main/static/css/style.css).

### Custom Javascript

- Custom javascript was added when needed to assist with bootstrap's deletion modals.
- The modal js to delete reports can be viewed [here](https://github.com/0davidog/Umbra-Report/blob/main/static/js/delete_report.js).
- The javascript file to edit and delete comments was mostly taken from the Code Institiue Walkthhough project with only minor changes.
- This can be viewed [here](https://github.com/0davidog/Umbra-Report/blob/main/static/js/comments.js).

</details>

## Features

<details><summary>VIEW FEATURES</summary>

### Implemented Features

#### Navigation

<em>[As a Site User, I want a user-friendly navigation menu that helps me explore different sections of the blog easily.](https://github.com/0davidog/Umbra-Report/issues/17)</em>

The Navigation bar was created from Bootstrap's offcanvas navbar found [here](https://getbootstrap.com/docs/5.3/components/navbar/#offcanvas).

![Screenshot 2024-02-25 at 10-46-13 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/bf5171f6-6b0a-43de-b15b-106aa68f63e1)
![Screenshot 2024-02-25 at 10-46-27 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/5ec380d9-3d50-4454-9fc9-fcb820a7c78f)

#### Create Report

<em>[As a Site User, I want to create a new blog post with a title, content, and optional images, so that I can share my thoughts and experiences.](https://github.com/0davidog/Umbra-Report/issues/4)</em>

A button on the index page allows the user to access a form for creating a Report (blog post).

![Screenshot 2024-02-25 at 11-05-21 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/a376f63e-5354-4587-974a-83b16dc5115a)

When not logged in the button instead takes the user to the login page.

![Screenshot 2024-02-25 at 10-48-39 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/168d8f6b-331e-4191-abe0-0354351a2ae3)

The form can then be filled out and submitted.

![Screenshot 2024-02-25 at 11-00-02 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/13c619da-205b-41c0-ab50-3212cf7dbd0b)

<em>[As a Site User or Admin, I can create draft posts so that I can finish writing the content later.](https://github.com/0davidog/Umbra-Report/issues/7)</em>

Users can select whether they want to publish their report or save it as a draft to finish later. Draft reports can then be accessed via the user page.

#### Read Report List

<em>[As a Site User I can view a paginated list of posts so that I can select which post I’m interested in viewing.](https://github.com/0davidog/Umbra-Report/issues/9)</em>

The index page shows a list of reports (blog posts) and these are separated into pages if there are more than 6.

![Screenshot 2024-02-25 at 11-08-57 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/0f8f0dd6-6c63-4b76-a1f6-de6ed5905777)

#### Read Full Report Detail

<em>[As a Site User, I can click on a post so that I can view the complete content.](https://github.com/0davidog/Umbra-Report/issues/10)</em>

Clicking on a report title takes the user to a full dteail view of the post where they can read the whole content.

![Screenshot 2024-02-25 at 11-13-31 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/dae33a24-03e2-45a1-b773-8d68f1b61293)

#### Edit Report

<em>[As a Site User, I want the ability to update my existing blog posts to update or improve the content over time.](https://github.com/0davidog/Umbra-Report/issues/5)</em>

Users who want to edit a report they have writen can do so when logged in. A link to edit is on the list view in the index page and an edit button can be found on the full report detail page also.

![Screenshot 2024-02-25 at 11-17-28 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/c03c1f5a-6d7c-4c71-bcc0-2a66e5f855fb)

#### Delete Report

<em>[As a Site User, I want to be able to delete my own blog posts if I decide to remove them from the website.](https://github.com/0davidog/Umbra-Report/issues/6)</em>

Users can also choose to delete any report they have written providing they are logged in. A link to delete the report can be found on the list view in the index page and a button to delete can be found on the full report detail page also. Choosing to delete brings up a model to ask for confirmation.

![Screenshot 2024-02-25 at 11-17-28 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/c03c1f5a-6d7c-4c71-bcc0-2a66e5f855fb)

#### Likes

<em>[As a Site User, I want to be able to like blog posts to engage with the author and other readers.](https://github.com/0davidog/Umbra-Report/issues/14)</em>

Users, when logged in can like a post by accessing the full post page. A button can be found beneath the main content. Once liked a user can unlike a post with the same button.

![Screenshot 2024-02-25 at 11-18-38 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/333698c6-9821-453d-8e2b-a2f1008e061a)

#### Create Comments

<em>[As a Site User, I want to be able to comment on blog posts to engage with the author and other readers.](https://github.com/0davidog/Umbra-Report/issues/12)</em>

A form to add a comment on any post can be found at the bottom of the full report detail page. If a user is logged in the can choose to fill out this form to add a comment.

![Screenshot 2024-02-25 at 11-19-32 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/9c7c9b28-c9c1-412a-bb62-5e6a29f96455)

#### Read Comments

<em>[As a Site User or Admin, I can view the comments on each individual post so that I can read the conversation.](https://github.com/0davidog/Umbra-Report/issues/11)</em>

A list of comments can be found at the bottom of the full report detail page. User can only see approved comments unless the are the auther of a yet to be approved comment.

![Screenshot 2024-02-29 at 16-29-47 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/a5a464b4-dbcc-4308-a601-f86435005c68)

#### Edit Comments

Once a comment is created a user can choose to edit that comment using the edit button bellow the comment. A user must be logged in and the author of the comment to be able to edit. Clicking the edit button changes the original comment form to an edit comment form, populated with the comments content.

![Screenshot 2024-02-29 at 16-29-59 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/9342c4ad-db3b-4c42-94c0-98a5fe665eca)

#### Delete Comments

A user can choose to delete their comment providing the are the author and are logged in. This is done by selecting the delete button beneath the comment and confirming with the modal.

![Screenshot 2024-02-29 at 17-19-10 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/96f83669-7651-40c7-8313-5c7af3ef8f33)

#### Account Register

<em>[As a Site User, I want to register an account on the blog website so that I can create and manage my own posts.](https://github.com/0davidog/Umbra-Report/issues/1)</em>

A new user can register an account by selecting sign up and entering the required details. This is handled by django allauth.

![Screenshot 2024-02-25 at 11-20-29 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/7ef8426d-6cbf-4318-afc4-4b6e2a30a44b)

#### Account Log-in/out

<em>[As a Site User, I want to log in to the website securely using my credentials so that I can participate in the blog’s features.](https://github.com/0davidog/Umbra-Report/issues/2)</em>

A user, once registered can then log in or out by selecting the links in the navigation bar. This too is handled by django allauth.

Log out:
![Screenshot 2024-02-25 at 11-21-22 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/15df1a17-9336-46b6-8f3c-4f57fb9974ce)

Sign In:
![Screenshot 2024-02-25 at 11-20-46 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/10cbdc37-ee37-4492-9004-8a5eb9518b31)

<em>[As a Site user, I want the option to reset my password in case I forget it, ensuring secure access to my account.](https://github.com/0davidog/Umbra-Report/issues/3)</em>

Should a user forget their password, Django-allauth offers a password reset option on the login page. This requires the user have an email so email was made a requirement on signup.

#### About Page

<em>[As a Site User, I can click on the About link so that I can read about the site.](https://github.com/0davidog/Umbra-Report/issues/20)</em>

An about page was created to give users an idea of what the site's themes are and how to participate.

![Screenshot 2024-02-25 at 11-22-28 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/bad8b923-91cd-43a6-8775-08901a2673b9)

#### User Page

<em>[As a Site User, I can click on a username link so that I can read about the user and see their posts.](https://github.com/0davidog/Umbra-Report/issues/22)</em>

Users can click on their own or anothers user name to access a page that lists links to that user's written reports.

![Screenshot 2024-02-25 at 11-23-07 The Umbra Report](https://github.com/0davidog/Umbra-Report/assets/135815736/d54496a5-d3f1-4c40-97dd-55fac1fef080)

#### Admin Panel

<em>[As a Site Admin I can manage all blog posts through the admin panel to maintain control over the site’s content.](https://github.com/0davidog/Umbra-Report/issues/8)</em>

<em>[As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments.](https://github.com/0davidog/Umbra-Report/issues/13)</em>

<em>As a Site Admin, I can create or update the about page content so that it is available on the site.](https://github.com/0davidog/Umbra-Report/issues/21)</em>

In creating the Djando app I created a super user account for myself ([see detail](#create-superuser)) which allows me to access the admin panel. This means I have the ability to edit and approve all posts and/or comments as well as update the about page.

### Future Features

Being a project with limited time a couple of user stories were given the label 'won't-have' and are marked here as possible future features.

- [As a Site User, I want to receive notifications when someone likes or comments on my blog posts to stay informed about the engagement with my content.](https://github.com/0davidog/Umbra-Report/issues/15)
- [As a Site User, I want to search for specific blog posts or topics to quickly find the information I'm looking for.](https://github.com/0davidog/Umbra-Report/issues/16)

</details>

## Testing

Please refer to this seperate testing document for a full rundown of tests and audits:

[TEST-DOCUMENT](https://github.com/0davidog/Umbra-Report/blob/main/TESTING.md)
  
## Technologies Used

### Languages

- HTML
- CSS
- Javascript
- Python

### Frameworks, Libraries & Programs Used

- Django
- Bootstrap
- VScode
- GitBash
- Further requirements:

<details><summary>REQUIREMENTS LIST</summary>
  
```
asgiref==3.7.2
bleach==6.1.0
certifi==2023.11.17
cffi==1.16.0
charset-normalizer==3.3.2
cloudinary==1.36.0
crispy-bootstrap5==0.7
cryptography==41.0.7
defusedxml==0.7.1
dj-database-url==0.5.0
dj3-cloudinary-storage==0.0.6
Django==4.2.9
django-allauth==0.57.0
django-autoslug==1.9.9
django-crispy-forms==2.1
django-summernote==0.8.20.0
gunicorn==20.1.0
idna==3.6
oauthlib==3.2.2
psycopg2==2.9.9
pycparser==2.21
PyJWT==2.8.0
python3-openid==3.2.0
requests==2.31.0
requests-oauthlib==1.3.1
setuptools==69.0.3
six==1.16.0
sqlparse==0.4.4
tzdata==2023.4
urllib3==1.26.18
webencodings==0.5.1
whitenoise==5.3.0
```

</details>

## Deployment

### Prerequisites

This project requires some steps in preparation...

#### ElephantSQL Database:

ElephantSQL is the PostgreSQL database hosting service used in this project.

<details><summary>DETAILS</summary>


- Visit [ElephantSQL](https://www.elephantsql.com/) and set up a free account if you don't already have one (you can use Google or Github to create an account easily).
- Login
- Navigate to Dashboard
- To create a new database instance click the '+Create New Instance' button.
- Select a name for your instance (usually the project name).
- Select the free plan called 'Tiny Turtle'.
- (You can leave Tags empty).
- Click the 'Select Region' button.
- Select any available data centre.
- Click the review button.
- If all the details look good then click the 'Create Instance' button.
- Click on your new instance.
- Navigate to STATS menu.
- Check the version is 12 or higher.
- (any less and you may have to create another instance with a different chosen data centre).
- Navigate to DETAILS menu.
- Copy the URL
- Paste into env.py file in this format:

`os.environ.setdefault("DATABASE_URL", "<The copied instance URL>")`

- pip3 install packages needed to connect to your database:

`pip3 install dj-database-url~=0.5 psycopg2~=2.9`

- Add to reqiurements.txt:

`pip3 freeze --local > requirements.txt`

- import the packages into the setting.py file:

`import os
import dj_database_url
if os.path.isfile('env.py'):
    import env`

- Comment out the existing sqlite3 databas connection:

```
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
```

- Connect the DATABAS_URL from env.py to settings.py in this format: 

`DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}`

- Your project should now be connected to the database, to create the database tables use this command:

`python3 manage.py migrate`

</details>

#### Create Superuser

Use this command and enter details to create your superuser account:

`python3 manage.py createsuperuser`

#### Cloudinary

Cloudinary is a hosting platform used for images in this project.

<details><summary>DETAILS</summary>


- Install The necessary Cloudinary Packages:
  
`pip3 install cloudinary~=1.36.0 dj3-cloudinary-storage~=0.0.6 urllib3~=1.26.15`

- Don't forget to add to requirements file:
  
`pip3 freeze --local > requirements.txt`

- Visit [Cloudinary](https://cloudinary.com/) and set up a free account if you don't already have one (you can use Google or Github to create an account easily).
- Login
- Navigate to Programmable Media - Dashboard
- Copy the API environment variable: CLOUDINARY_URL and fit it into your env.py file in this format:
  
`os.environ.setdefault("CLOUDINARY_URL", "<The URL copied from Cloudinary Dashboard>")`

- (remove 'CLOUDINARY_URL=' from the copy-pasted string)
- Open settings.py and add cloudinary and cloudinary_storage to INSTALLED_APPS.
- (The cloudinary_storage app should by place directly under django.contrib.staticfiles)

</details>

### Fork and Clone the Repository

<details><summary>DETAILS</summary>

#### Fork

To keep the original branch unaltered you can fork a repository on github.

- Navigate to the repository you want to fork.
- Click the 'Fork' button at the top right.
- Select the 'Owner' from the dropdown menu.
- Enter an optional description.
- Choose whether or not to copy main branch only.
- Click Create fork.

Source: [Github Docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)
    
#### Clone

On Github you can clone your repository to create a local and sync between the two locations.

- Navigate to the main page of the repository.
- Click thr '<>Code' button..
- Copy the repository URL.
- Open Git Bash or a terminal in your IDE.
- Choose the directory you want to place the repository.
- Type 'git clone', and then paste in the copied repo URL.

`git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`

- Press Enter to create your local clone.

Source: [Github Docs]([https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository))

</details>

### Local Deployment

<details><summary>DETAILS</summary>


To get started with local development in GitPod or your preferred IDE, follow these steps:

- Clone the repository.
- Install required packages (if project is already worked on)

`pip3 install -r requirements.txt`

- Create an 'env.py file in the app's root directory for environment variables (if using CI template this should already exist).

- In the 'env.py file, add a secret key in this format:

```
import os

os.environ.setdefault(
    "SECRET_KEY", 
    "<your chosen key goes here>"
)
```

- Add to settings.py in this format:

```
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")
```

- Start the server by running the following command:

`python3 manage.py runserver`

- Now you can access the application by opening the provided URL in your browser (add your browser url to allowed hosts).

`ALLOWED_HOSTS = ['<browser URL>']`

</details>

### Production Deployment

<details><summary>DETAILS</summary>

        
Prepare the Django Project:

- Ensure your Django project is properly configured and runs smoothly locally.
- Make sure you have a requirements.txt file listing all Python dependencies required for your project.
- Ensure your project's settings are set up to work in a production environment (e.g., DEBUG = False, static files configuration, database settings).

Create a Procfile:
- Heroku uses a Procfile to determine how to run your application.
- Create a file named Procfile (no file extension) in your project's root directory.
- Inside the Procfile, specify the command needed to run your Django application. 

For example:

`web: gunicorn your_project_name.wsgi`

Create a runtime.txt File:

- Heroku needs to know which Python version your application requires. Create a runtime.txt file in your project's root directory.
- Inside runtime.txt, specify the Python version.

For example:

`python-3.9.5`

Install Gunicorn:

- Gunicorn is a WSGI HTTP server for Python web applications, and it's commonly used for deploying Django applications.
- Install Gunicorn and add it to your requirements.txt file:

`pip install gunicorn`
`pip freeze > requirements.txt`

Set Up Database:

See [ElephantSQL](####-ElephantSQL-Database)

Ad Heroku to allowed hosts in settins.py:

`ALLOWED_HOSTS = ['<browser URL>', '.herokuapp.com']`

Collect Static Files:

If your project uses static files, collect them using Django's collectstatic command:

`heroku run python manage.py collectstatic`

Commit your changes to Git:

`git add .
git commit -m "Initial commit"`

Create a new app on Heroku:
- Head over to heroku and log in. Choose 'create new app'.
- Choose a name for your app and your location. Hit 'create app'.
- Select the 'Settings' tab.
- In Config Vars, reveal config vars.
- Enter the config variables used in your env.py file.
- For example:
  - CLOUDINARY_URL
  - DATABASE_URL
  - EMAIL_USER - (gmail address)
  - EMAIL_PASS- (gmail password)
  - SECRET_KEY (The Django secret key is a crucial security setting used to provide cryptographic signing.)
   
    It is used for:
    - Security: The secret key is used to generate hashes for password reset tokens, user session tokens, and other cryptographic signatures. It helps protect against various security threats such as session hijacking, data tampering, and CSRF (Cross-Site Request Forgery) attacks.
    - Session Management: Django uses the secret key to sign and verify session cookies. This ensures that the session data stored in cookies cannot be tampered with by malicious users.
    - CSRF Protection: Django uses the secret key to create tokens for preventing CSRF attacks. When a form is rendered, Django includes a hidden CSRF token in the form. When the form is submitted, Django verifies that the CSRF token matches the one generated for the user's session, thus preventing CSRF attacks.
    - Cryptographic Signatures: The secret key is used to sign various pieces of data within Django, such as cookies, messages, and tokens. This allows Django to verify the integrity and authenticity of these pieces of data.
    - Given its critical role in security and various Django functionalities, it's essential to keep the secret key secret and never share it publicly or with unauthorized individuals. If the secret key is compromised, it could potentially lead to security vulnerabilities in your Django application.

- Head over to the Deploy tab.
- Select Github (you will need to authorize this).
- Choose your repository.
- Manually deploy the main branch of this GitHub repo.
- You can now view your app.

</details>

## Credits

### Content

- The Code Institute walkthrough project 'I Think, Therefore I Blog' was used to inform the setup and general structure of this project.

### Media

Icons are sourced from [fontawesome](fontawesome.com/).
- [Menu bars](https://fontawesome.com/icons/bars?f=classic&s=solid)
- [Eye](https://fontawesome.com/icons/eye?f=classic&s=solid)
- [Information Icon](https://fontawesome.com/icons/circle-info?f=classic&s=solid)
- [Github logo](https://fontawesome.com/icons/github?f=brands&s=solid)
- [LinkedIn logo](https://fontawesome.com/icons/linkedin?f=brands&s=solid)

Site logo and background created by the site author.
Majority of Report images uploaded to site are also the author's work however as the site is available for users to upload images, any copyrighted images found will have to be dealt with accordingly when identified. 

### Acknowledgments

- Thanks to my Mentor, Malia, for her advice on ensuring a solid end product.
- Thanks to those users who signed up and got involved in testing/using the site.
