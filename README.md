<h1 align="center">Patterns For Fashion</h1>

![Mock-up](static/assets/images/readme/mock-up.png)

# Table of contents
1. [User Experience](#user-experience)
    1. [User Stories](#user-stories)
        1. 
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
### Viewing and Navigation
1. As a buyer I want to be able to view a list of products.
1. As a buyer I want to be able to view individual product details.
1. As a buyer I want to be able to view the total of my purchases.
### Registration and User Accounts
1. As a buyer I want to be able to register for an account.
1. As a buyer I want to be able to login or logout.
1. As a buyer I want to be able to recover my password if I forget it.
1. As a buyer I want to be able to receive an email confirmation after registering.
1. As a buyer I want to be able to have a personalized user profile.
### Sorting and Searching
1. As a buyer I want to be able to search for a product by name or description.
1. As a buyer I want to be able to see the searched products and the amount of results.
1. As a buyer I want to be able to sort the products by categories, price and reviews.
### Purchasing and Checkout
1. As a buyer I want to be able to select a specific size and the quantity for the product when I purchase it.
1. As a buyer I want to be able to select one product or more in order to purchase them.
1. As a buyer I want to be able to view the items in my bag to be purchased.
1. As a buyer I want to be able to adjust the quantity of individual items in my bag.
1. As a buyer I want to be able to enter my payment information.
1. As a buyer I want to be able to view an order confirmation after checkout and receive and email confirmation.
1. As a buyer I want that my personal details and payment information is safe and secure.
### Admin and Store Management
1. As the owner of the site I want to have the choice to add a product to the website directly from the site and not through admin.
1. As the owner of the site I want to be able to edit/update a product.
1. As the owner of the site I want to be able to delete a product.
### Blog 
1. As a site visitor I want to be able to view the list of the latest news the site has to offer.
1. As a site visitor I want to be able to read individual posts on the blog page.
1. As a site visitor I want to be able to add comments to the blog posts.
## Design
### **Color Palette**
![Color Palette](static/color-palette.png)
### **Typography**
Main font-family used throughout the website is [DM Serif Display](https://fonts.google.com/specimen/DM+Serif+Display?query=DM+Serif+Display&preview.layout=row&preview.text_type=custom).
### **Imagery**
All images used for the ads posted in the website were taken by the developer and are subject for demonstration only.
## Wireframes
-   ![home](static/wireframes/homepage.jpg)
-   ![register](static/wireframes/register.jpg)
-   ![login](static/wireframes/login.jpg)
-   ![product details](static/wireframes/productdetails.jpg)
-   ![products](static/wireframes/products.jpg)
-   ![profile](static/wireframes/profile.jpg)
-   ![mobile](static/wireframes/mobile.jpg)
# Features
## Existing Features
Patterns 4 Fashion website is designed to give users easy access to information, simple navigation paths, clear feedback for all meaningful actions
and safe and secured personal data storage. The site contains 6 applications: bag, blog, checkout, home, products and profiles.
## Navbar
1. Responsiveness on different device sizes.
1. Mobile collapse button.
1. Toast messages: Pop-up window for confirmation messages following commands as registration, logging in, logging out, add product to bag,
remove product from the bag, etc. It can be dismmissed by click on x symbol.
1. Logo image on the left top corner present on all pages redirects to home page.
1. Search bar where the user can find products filtered by category and description.
1. Apps' templates links : Home, Blog, Profiles, Shpping Bag
-   ![navbar](static/navbar/navbar.jpg)
1. Profiles app dropdown list when the user is not authenticated contains the links to login/register pages.
-   ![profile collapsed](static/navbar/profile-collapsed.jpg)
1. Profiles app dropdown list when the user is authenticated as the super user. Contains the link to
the Product Management page where the superuser can add products to the site.
-   ![superuser profile](static/navbar/superuser-profile.jpg)
1. Page footer available on all pages.
    -   Contains 3 sections:
        -   Adress and Telephone.
        -   Email address and Social Media links
        -    
-   ![footer](static/navbar/footer.jpg)
## Home app
## Profiles app
1. Registration form fields: Email, Email Confirmation, Username, Password and Password confirmation.
1. Log in form fields: Username and Password.
1. Log out.
## Blog app
1. 
## Bag app


## Features left to implement
# Technologies Used
## Languages Used
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://nl.wikipedia.org/wiki/JavaScript)
-   [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))
## Frameworks, Libraries & Programs Used
1. [Django:](https://www.djangoproject.com/)
    - Django Python fullstack framework used for the rapid development of the site.
1. 
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used to add the social-media icons in the footer of the page and the various icons from the different sections of login, register, contact, post ad forms.
1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Roboto Slab' font into the style.css file which is used on all text throughout the website.
1. [jQuery:](https://jquery.com/)
    - jQuery was used for the interactive features.
1. [Randomkeygen:](https://randomkeygen.com/)
    - Randomkeygen was used for generating Fort Knox password.
1. [Color Hex:](https://www.color-hex.com/)
    - Color hex was used to set the color palette.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub was used to store the projects code after being pushed from Git.
1. [Heroku:](https://heroku.com/)
    - Heroku was used for deploying the app.
1. [AWS:](https://aws.amazon.com/?nc2=h_lg)
    - AWS is a secure cloud services platform used to store static and media files for this site.
1. [Stripe Api](https://stripe.com/en-nl)
    - Stripe is a third-party payment processor used to process card payments for this site.
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
### Search bar
-   The user can search ads by typing inside the search bar words selected from the title, description and category name sections of the cards.
-   The reset button brings the user back to the home page to all ads.
### Redirect pages
-   If the user tries to register with a username which already exists in the database, the message "Username already exists"
    flashes and the user gets redirected to log in page.
-   If the user tries to log in with a username which doesn't exist in the database, the message "Username doesn't exists"
    flashes and the user gets redirected to register page.
### Toast Messages
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
# Database Models

# Deployment
# Forking the GitHub Repository

# Making a Local Clone


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
## Mentor
## Slack Comunity
## My Family