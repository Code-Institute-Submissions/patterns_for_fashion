# Contents Testing
1. [Manual Testing](#manual-testing)
    1. [Functionality](#functionality)
    1. [User Experience Stories](#user-experience-stories)
1. [Validation](#validation)
1. [Further Testing](#further-testing)
1. [Fixed Bugs](#fixed-bugs)
1. [Known Bugs](#known-bugs)

# Manual Testing
## Functionality
### Index.html
**Test Case** | **Description** | **Expected Results** | **Actual Results** | **Pass/Fail** | **Comments**
--- | --- | --- | --- | --- | ---
TC001 | Test Website responsiveness on all screen sizes on chrome browser | Website is responsive, all elements contained and no imgages distorted | Website is responsive, all elements contained and no imgages distorted | Pass |
TC002 | Test Website responsiveness on all screen sizes on firefox browser | Website is responsive, all elements contained and no imgages distorted | Website is responsive, all elements contained and no imgages distorted | Pass |
TC002 | Test Website responsiveness on all screen sizes on microsoft edge browser | Website is responsive, all elements contained and no imgages distorted | Website is responsive, all elements contained and no imgages distorted | Pass |

## User Experience Stories
### Viewing and Navigation
1. As a buyer I want to be able to view a list of products.
    -   When the user clicks on the All garments link in the main navigation bar, the products page display all garments.
1. As a buyer I want to be able to view individual product details.
    -   When the user clicks on an individual product, the product detail page displays the selected product with all the its properties.
1. As a buyer I want to be able to view the total of my purchases.
    -   When a user adds a product to the shopping bag, there's a pop-up alert window displaying a list of the added products.
1. As a buyer I want to able to view the history of my orders.
    -   At the bottom of the profile page there's a card containing the past user's orders.
### Registration and User Accounts
1. As a buyer I want to be able to register for an account.
    -   The user can safely register in order to create an account when purchasing an item.
    -   The user can safely register when clicking on the register link from the dropdown navigation item at the top navigation bar
1. As a buyer I want to be able to login or logout.
    -   The user can enter the already registered credentials and stays logged in unless the user log out.
1. As a buyer I want to be able to recover my password if I forget it.
    -   If the user forgets the password there is a link at the bottom of the log in form which redirects the user to password reset page
    -   The user can enter the email address used for creating the account and press on the reset password button
    -   The user gets redirected to the reset password form.
    -   ![Testing Password](static/testing/testing-password.png)
1. As a buyer I want to be able to receive an email confirmation after registering.
    -   After registering the user receives an verification email
    -   ![Registration Confirmation](static/testing/registration.png)
1. As a buyer I want to be able to have a personalized user profile.
    -   The user profile page displays a form where the user can enter personal information
    -   At the bottom of the form there is an order history card where the user can view the past orders if any.
### Sorting and Searching
1. As a buyer I want to be able to search for a product by name or description.
    -   When the user enters a word in the search bar which is to be found in the product(s) description or name, than the page renders the specific product(s)
    -   When the searched word doesn't exist in the name or description of any product, there is a message displaying letting the user know that there are 0 results.
    -   ![Search](static/testing/search.png)
    -   As a known bug, if the user enters more than a word then, the search results are 0.
1. As a buyer I want to be able to see the searched products and the amount of results.
    -   When the user enters a valid search word, the products page displays the specific product(s) and their amount. 
1. As a buyer I want to be able to sort the products by categories, price and reviews.
    -   On the main navigation bar there is the filter link where the user can sort the products by categories alphabetically,
    by price from the lowest to the highest or by reviews from the highest to the lowest. 
### Purchasing and Checkout
1. As a buyer I want to be able to select a specific size and the quantity for the product when I purchase it.
    -   There is a dropdown select field with the options fo the xs, s, m, l, xl sizes
    -   After selecting the size, the user can add extra items from the same size to the bag or add different sizes of the same product.
1. As a buyer I want to be able to select one product or more in order to purchase them.
    -   After adding the selected product to the bag, the user can continue shopping by clicking on the keep shopping button and selecting
    another product to purchase from the all products page.
1. As a buyer I want to be able to view the items in my bag to be purchased.
    -   After addindg the desired products to the shopping bag, the user can view the contents of the shopping bag by clicking the alert
    windows which notifies the user that the product was added or by simply ckicking on the bag icon top right of the top navigation bar.
1. As a buyer I want to be able to adjust the quantity of individual items in my bag.
1. As a buyer I want to be able to enter my payment information.
1. As a buyer I want to be able to view an order confirmation after checkout and receive and email confirmation.
1. As a buyer I want that my personal details and payment information is safe and secure.
### Admin and Store Management
1. As the owner of the site I want to have the choice to add a product to the website directly from the site and not through admin.
    -   This feature is available only for the superuser.
    -   If the logged in user is not authenticated as superuser, when trying to add a new product there's a toast message pop up "Sorry, only owners can do that."
    ![Authentification alert message](static/testing/superuser.png)
1. As the owner of the site I want to be able to edit/update/ or delete a product.
    -   Every product both on the all products page and product detail page has the edit/delete links available only when the superuser is authenticated.
### Blog 
1. As a site visitor I want to be able to view the list of the latest news the site has to offer.
    -   The blog page renders 3 posts per page, the rest of the posts can be viewed by clicking on the NEXT/PREV button.
1. As a site visitor I want to be able to read individual posts on the blog page.
    -   Every individual post details: image, title, date of post, content, can be viewed by clicking on the desired post.
1. As a site visitor I want to be able to add comments to the blog posts.
    -   Each post detail page has a functional form for adding comments.
    -   Any user can add a comment without being authenticated.
    -   The comments are being moderated by the superuser from the admin panel.
    -   ![Comment Moderation](static/testing/comment.png)

# Validation
-   [W3C Markup Validator](https://validator.w3.org/) 
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) 
-   [JavaScript Validator](https://jshint.com/) 
-   [Python Validator](http://pep8online.com/) 
# Further Testing
-   The website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   Friends and family members were asked to review the website to point out any bugs and/or user experience issues.
# Fixed Bugs
# Known Bugs