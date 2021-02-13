<h1 align="center">Patterns For Fashion</h1>

![Mock-up](static/assets/images/readme/mock-up.png)

# Table of contents
1. [User Experience](#user-experience)
    1. [User Stories](#user-stories)
        1. [Buyer Users](#buyer-users)
        1. [Seller Users](#seller-users)
    1. [Design](#design)
        1. [Overall Design](#overall-design)
        1. [Color Palette](#color-pallette)
        1. [Typography](#typography)
        1. [Imagery](#imagery)
    1. [Wireframes](#wireframes)
    1. [Second Chance Web Collections in MongoDB](#second-chance-collections-in-mongodb)
1. [Features](#features)
    1. [Features Left to Implement](#features-left-to-implement)
1. [Technologies Used](#technologies-used)
    1. [Languages Used](#anguages-used)
    1. [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)
1. [Testing](#testing)
    1. [Functionality](#unctionality)
        1. [Navigation bar](#navigation-bar)
        1. [Ads](#ads)
        1. [Search bar](#search-bar)
        1. [Redirect pages](#redirect-pages)
        1. [Flash messages](#flash-messages)
        1. [Contact Form](#contact-form)
        1. [Cancel Buttons](#cancel-buttons)
        1. [Footer section](#footer-section)
    1. [Testing User Stories from User Experience (UX) Section](#testing-user-stories-from-user-experience-(UX)-Section)
        1. [Testing Buyer User Stories](#testing-buyer-user-stories)
        1. [Testing Seller User Stories](#testing-seller-user-stories)
    1. [Validation](#validation)
    1. [Further Testing](#further-testing)
    1. [Fixed Bugs](#fixed-bugs)
    1. [Known Bugs](#known-bugs)
1. [Deployment](#deployment)
1. [Forking the GitHub Repository](#forking-the-gitHub-repository)
1. [Making a Local Clone](#making-a-local-clone)
1. [Credits](#credits)
    1. [Images](#images)
    1. [Code](#code)
    1. [Tutor Support](#tutor-support)
    1. [Mentor](#mentor)
    1. [Slack Comunity](#slack-comunity)
    1. [My Family](#my-family)

# User Experience
## User Stories
## Design
### **Overall design**
### **Color Palette**
### **Typography**
### **Imagery**
All images used for the ads posted in the website were taken by the developer and are subject for demonstration only.
## Wireframes
-   ![home](static/assets/images/wireframes/home.png)
-   ![register](static/assets/images/wireframes/register.png)
-   ![login](static/assets/images/wireframes/login.png)
-   ![post](static/assets/images/wireframes/post.png)
-   ![contact](static/assets/images/wireframes/contact.png)
-   ![mobile](static/assets/images/wireframes/mobile.png)
# Features
1. Responsiveness on different device sizes.
1. Mobile collapse button.
1. Search bar where the user can find products filtered by title, category name and description.
1. Reset button which brings the user back to the home page.
1. Interactive cards displaying succint information of the advertised products both on card content and card reveal.
    Card reveal gets triggered when clicked on the photo or on the title of the card content.
1. Registration form fields: Username, Password and Password confirmation.
1. Delete account option with dialog modal pops up to ask the user to confirm the deletion.
1. Log in form fields: Username and Password.
1. Log out.
1. Post advertising form fields: Category, Url for photos, Title, Description, Price,
    Condition, Area, Telephone, Email. Option buttons for edit and cancel which brings the user to the homepage.
1. Options for Edit and Delete the post available only for the user who posted. The delete button triggers a dialog modal asking for deletion confirmation.
1. Confirmation messages following commands as registration, logging in, logging out, post ad, edit and delete post, etc.
1. Contact form with 3 fields for filing in: username, email and message.
1. 404 page implemented.
1. Favicon.
1. Defensive programming. The Delete Account button in the profile page triggers a dialog modal which gives the user the
    possibility to choose from deleting the account or not. Same works for Delete button for the ads users can post.
## Features left to implement
1. Side Filter with index options for area, condition, category.
1. Add to User's Profile the contact details and password.
1. The User's option to edit the profile.
1. The User's option to post an advertising with the registered profile details.
1. The contact form to being automatically filled in with the username and emailaddress of the user currently logged in.
# Technologies Used
## Languages Used
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://nl.wikipedia.org/wiki/JavaScript)
-   [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))
## Frameworks, Libraries & Programs Used
1. [Django:](https://www.djangoproject.com/)
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used to add the social-media icons in the footer of the page and the various icons from the different sections of login, register, contact, post ad forms.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Roboto Slab' font into the style.css file which is used on all text throughout the website.
1. [jQuery:](https://jquery.com/)
    - jQuery was used for the interactive features.
1. [Randomkeygen:](https://randomkeygen.com/)
    - Randomkeygen was used for generating Fort Knox password.
1. [EmailJS:](https://www.emailjs.com/)
    - EmailJS was used to connect the contact form to the email address.
1. [Color Hex:](https://www.color-hex.com/)
    - Color hex was used to set the color palette.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub was used to store the projects code after being pushed from Git.
1. [Heroku:](https://heroku.com/)
    - Heroku was used for deploying the app.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.
1. [PicResize:](https://picresize.com/)
    - PicResize was used to resize the pictures used in the README file and for the ads links.
1. [Easycaptures:](https://easycaptures.com/)
    - EasyCaptures was used to host the images from the ads.
1. [Flaticon](https://www.flaticon.com/authors/freepik)
    - Flaticon was used to import the icon for the website favicon.
1. [Techsini](https://techsini.com/)
    - Techsini was used to capture the mock-ups.
# Testing
## Functionality
### Navigation bar
-   Fixed navigation bar. It stays on top while scrolling down the page.
-   Top left brand (logo) section. When click it links to the home page and brings the user from any other webpage to the home page.
-   Top right the internal links to the main webpages when the user is not logged in: Home, Log in, Register, Contact Us. The user
    can visit the home page where the ads are displayed, log in/register or submit a contact form.
-   When the user is logged in, the navbar displays Home, My Account, Post Ad, Log Out and Contact Us pages.
-   On mobile devices the navbar displays an active burger-menu icon. If clicked, the icon displays the list of all functional page links.
### Ads
-   Are displayed all on the home page.
-   The card reveal opens up by clicking on the photo or title of the card-content. It closes back by ckicking on the x symbol.
### Search bar
-   The user can search ads by typing inside the search bar words selected from the title, description and category name sections of the cards.
-   The reset button brings the user back to the home page to all ads.
### Redirect pages
-   If the user tries to register with a username which already exists in the database, the message "Username already exists"
    flashes and the user gets redirected to log in page.
-   If the user tries to log in with a username which doesn't exist in the database, the message "Username doesn't exists"
    flashes and the user gets redirected to register page.
### Toast Messages
### Contact Form
-   The submitted message arrives in the connected email, but the flash message doesn't display as expected as explained in the known
    bugs section. For this reason, in the javascript code was added "this.reset()" so that at least the form gets refreshed after being submitted.
### Footer section
-   The footer section is fixed on the bottom of all the web pages.
-   The external social media links from the footer sections open in an external window.
## Testing User Stories from User Experience (UX) Section

## Validation
-   [W3C Markup Validator](https://validator.w3.org/) 
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) 
-   [JavaScript Validator](https://jshint.com/) 
-   [Python Validator](http://pep8online.com/) 
## Further Testing
-   The website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   Friends and family members were asked to review the website to point out any bugs and/or user experience issues.
## Fixed Bugs
## Known Bugs
-   After submitting the message in the contact form the flash message doesn't display as expected and the form doesn't redirects to home page
    because it interracts with the javascript sendEmail.js file.
# Database Models

# Deployment
# Forking the GitHub Repository

By forking the GitHub Repository you make a copy of the original repository on you GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [Second-Choice GitHub Repository](https://github.com/mihaelasandrea/second-choice)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.

    ![Fork Button](static/assets/images/readme/fork.png)
3. You should now have a copy of the original repository in your GitHub account.

# Making a Local Clone

1. Log in to GitHub and locate the [Second-Choice GitHub Repository](https://github.com/mihaelasandrea/second-choice)
2. Under the repository name, click "Clone or download".

    ![Clone Button](static/assets/images/readme/clone.png)
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/second-choice
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/second-choice
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)
    to retrieve pictures for some of the buttons and more detailed explanations of the above process.

# Credits
## Images
## Code
-   [Dropdown select images](https://www.w3schools.com/howto/howto_js_dropdown.asp)
-   [JavaScript for update year in the footer copyright section.](https://stackoverflow.com/questions/4562587/shortest-way-to-print-current-year-in-a-website)
-   [Summary tag in the info card on index.html](https://www.w3schools.com/tags/tag_summary.asp)
-   [Read More functionality from info card on index.html](https://www.w3schools.com/howto/howto_js_read_more.asp)
-   [Bootstrap Address Example](https://www.w3resource.com/twitter-bootstrap/examples/twitter-bootstrap-address-example.php)
-   [Blog tutorial](https://djangocentral.com/building-a-blog-application-with-django/)
-   [Creating comments-system with django for the blog](https://djangocentral.com/creating-comments-system-with-django/)
-   [Blog Post Page Pagination](https://djangocentral.com/adding-pagination-with-django/)
## Tutor Support
Stephen for helping me rendering the fields in the measurements template
## Mentor
## Slack Comunity
https://github.com/AsunaMasuda/FloweryDays from peer-review code found an inspirational article where I learned about database modelling
## My Family