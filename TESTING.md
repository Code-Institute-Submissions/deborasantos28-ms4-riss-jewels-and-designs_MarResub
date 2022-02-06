# Welcome to the Testing.md of Riss Jewels & Designs

## Code Validators 

* CSS
  * No errors were found when testing on the official [Jigsaw validator](https://jigsaw.w3.org/css-validator/)

* HTML

  * No errors were found when testing on the official [W3C Validator](https://validator.w3.org/)

* Python 
  * This code is Pep8 compliant but "Trailing whitespace" warning shows [Pep8 Online](http://pep8online.com/)

## Browser Compatibility 
 * This website has been tested and verified to work on various browsers such as : Chrome, Firefox and Edge.

## Responsiveness
 * This website has been tested on small, medium and large screens. 
 * When it comes to Xs screens the website has only been tested in the responsive setting on Google Developer tools. 
 * [Am I Responsive](http://ami.responsivedesign.is/)



# Testing

## Navigation / Navbar

* Test Action
    * Navigated through all the links in the navbar and clicked on them individually;
    * Created multiple accounts and signed in and out with them;
    * Logged in as an Admin to make sure the Admin functions still work as expected;
    * On google development tools, I reduced the screen size to be able to see the side nav, clicked on all the links and signed in and out of the accounts;
    * Made sure the navigation bar displays at all times and that is not hidden by any other content;
    * Tested to see if the banner at the top of the navigation bar always displays delivery information;
    * Made sure that the store name is able to be used to return back to the home page from every part of the website;

* Expected Outcome 
    * All the links to be responsive and lead to their respective pages;
    * All the links should display when not logged in, logged in a current user and logged in as an Admin;
    * The navbar sticks to the top and is always visible;
    * The delivery information banner always displays the correct information;
    * The store name logo *Riss Jewels & Designs* always leads back to the home page.

* Test Outcome: **Pass**

# Navigation / Search Bar

* Test Action
    * Searched for specific key values with the database and checked if it retrieved the values searched
    * Searched for key values that didn't exist.
    * Looked if the search bar is visible and operational for all users, either as a guest or logged in user.
    * Made sure that the search bar is centrally aligned, that it does not shift it's position or any of the elements and that   the placeholder is visible.
    * Hovered over the search button (icon) to check that the hover class works.
    * Clicked the search button to see if it does the following:
        1. Loads the products page and shows products that match the search.
        2. If when trying to submit an empty search, it returns the correct error message, or no results found.

* Expected Outcome 
    * When searching for a product it should return the correct value.
    * When trying to to submit an empty search, should return an error message
    * The search bar stays aligned
    * Any user can see the search bar
    * The icon should change color when hovered


* Test Outcome: **Pass**

# Navigation / Icons

* Test Action
    * Clicked on all three links on the My profile section:
        * Product Management (When on admin)
        * My Profile
        * Login / Logout 
    * Clicked on the basket icon to make sure it works properly and it leads to the respective page
    * Made sure that all icons appear to the right of the navigation bar.
    * Checked that they perform as expected for either:
        1. Unregistered users.
        2. Registered users.
        3. Admin.
    * Clicked on all icons to make sure all the hover classes work.
    * Checked that if there are any items in the basket, that the number of items will show on the basket icon.

* Expected Outcome
    * All links should lead to their designated pages;
    * All icons should show as expected and be linked correctly to their pages
    * All icons should show a different color when hovered over
    * The basket icon should display a quantity if there is any items within it


* Test Outcome: **Pass**

# Navigation / Links and Display

* Test Action 
    * Clicked on all the links to ensure that they all do their respective functionality.
    * Clicked on the Home link to make sure it always takes me back to it, from any other part on the page.
    * Made sure all the links to the categories are displayed correctly and that their dropdown menu links work accordingly.
    * Tested that all the menu items work and are displayed on most screen sizes and according to their media queries. 
    * Made sure when dropping to a smaller screen size, that the Burger icon is correctly displayed and functional.
    * Clicked on burger icon button on and off several times to be able to check it displays and hides the menu without any issues.
    * Checked that in smaller screens only the search icon should be visible for the search bar and only displayed when clicked on.
    * Checked that the search icon is now aligned in the right next to the the Profile icon and the Basket icon. 
    * Checked that the free delivery banner is sized accordingly to the size screen that is displayed on.
    * Made sure that the Basket items information is still displayed correctly in all screen sizes.

* Expected Outcome
    * All links lead to their expected directories
    * Home link (logo) will always redirect the user to the Home page, from anywhere on the page
    * All Category links work correctly and lead to their expected pages.
    * The dropdown menus display and behave as they should.
    * Menu items and dropdown menu are displayed correctly on most size screens, including small
    * Burger Icon displays and functions correctly on the mobile navigation
    * Only the search icon should appear when seeing the page in small devices
    * Free delivery banner resizes accordingly to the screen size
    * All items in the basket and price are displayed correctly on the smaller screens


* Test Outcome: **Pass**


# Home

* Test Action
    * Made sure that the background image is displayed and centered and per expected.
    * Made sure that the *Shop Now* button and text is displayed correctly over the background image.
    * Made sure that the *Shop Now* button and text stays aligned to the left.
    * Checked that the white overlay is applied when navigating to the Products pages, and the background image displays when back to the home page.
    * Hovered over the buttons to make sure that the hover effect applies.
    * Tested all buttons on most screen sizes and made sure they are displayed correctly.


* Expected Outcome
    * The Background image should stay clear and centered.
    * Shop Now button and text should display over the background image
    * Shop Now button should be aligned to the left.
    * A white overlay should apply when transitioning to the Products display page.
    * All buttons should display the hover effect when hovered over
    * All buttons should display in the different screen sizes


* Test Outcome: **Pass**


# Products Page

* Test Action
    * Checked that all pages are correctly categorized with the correct Categories and subcategories. Such as:
        1. All Products:
            * By Price 
            * By Rating
            * By Category
            * All Products
        2. Jewelry
            * Earrings
            * Necklaces
            * Bracelets
            * All Jewelry
        3. Homeware
            * Resin Ornaments
            * Dream Catchers
            * All Homeware
        4. Special Offers
            * New Items
            * Sale
            * Clearance
            * All Specials
    * Checked that all products load as expected.
    * Checked that the white overlay has been applied successfully
    * Checked that the searching the on the search bar for a product, displays the correct product on the correct page
    * Checked that when on the *Jewelry* and *Homeware* products page, small buttons display the subcategories should appear underneath the Products header.
    * Clicked on all the links to make sure they display the correct products only on each category 
    * Checked that the *sort by* search is working and displaying accordingly when selecting any of the options
    * Checked that the *sort by* menu is positioned correctly and fixed on the right side of the screen
    * Checked that the *sort by* menu is now central on the page when displaying in small screens
    * Checked that all the products are displayed correctly and centralized accordingly with the various breakingpoints in the screen sizes.

* Expected Outcome:
    * All Categories and subcategories are displayed correctly on the page and the corresponding dropdown menus
    * Each Category when clicked takes the user to the respective products page
    * All Products should load clearly and as expected.
    * The white overlay should apply over the background image when display the products on the page
    * When searching on the search bar the correct products should display on the page
    * The subcategories buttons should display under the Products header and when clicked should display only the products related to that specific category
    * The *sort by* search should display the dropdown menu when clicked
    * The user should be able to filter through the products using the *sort by* search which can display the products by:
        1. Price (low to high) and (high to low)
        2. Rating (low to high) and (high to low)
        3. Name (A-Z) and (Z-A)
        4. Category (A-Z) and (Z-A)
    * All products should display correctly and adjusted accordingly to each screen size.
    * The *sort by* menu should display in the center of the page when displayed in smaller screens.

* Test Outcome: **Pass**

# Individual Product Detail

* Test Action
    * Checked that the correct product is displayed when clicking on the image of the product
    * Made sure that the images adjust to the correct screen size they are displayed on
    * Made sure that each image correctly links to their *product details* page.
    * Checked that the add to basket button and quantity selector work accordingly, by adding the product to the basket
    and incrementing or decrementing the quantity of items by the users choice.
    * Check that the products name, size, rating and description is displayed correctly on the individual product details page
    * Checked that on smaller screens the product image now is displayed in the center, and the products name, size, rating and description, along with the quantity selector and the add to basket and keep shopping buttons, now being displayed underneath the image.
    * Checked that the correct buttons depending on the user appear as expect.
    * The Keep Shopping button is displayed for all users, taking the user back to the all products page.
    * Checked that the Update button updates the quantity of the item when pressed
    * Checked that the edit and delete buttons appear for admin only.
    * Checked the edit product button opens the edit product form and also only is available for admin
    * Checked the delete product button triggers the *deleted successfully* toast, and that this is available for admin only.
    * Checked that all hover classes work.

* Expected Outcome
    * The correct product should be displayed when clicking on the product image
    * Images should adjust to the correct sizing when displayed on the different screen sizes
    * Each image should correctly link to their product details page
    * All the quantity selector buttons and add to basket button should work appropriately and accordingly
    * The name, size, rating, and description should display correctly on each individual product page.
    * The name, size, rating and description fields should display centrally on the page when viewing in smaller sized screens
    * All buttons work as expected
    * Edit and Delete buttons should only be displayed for Admin only.
    * Edit and Delete Buttons should execute their funcionality accordingly


* Test Outcome: **Pass**


# Basket

* Test Action
    * Checked that when the basket is empty it displays the *Shopping Basket* header and displays a message underneath telling the user that their basket is empty. 
    * Checked that when the basket is empty a correct *Keep Shopping* button is displayed under the basket empty message. Also clicked on the button and it takes the user back to the main products page. 
    * Checked that at the top of the page a banner informing the user how much more they need to spend to qualify for free delivery is shown.
    * Checked that if items in the basket are equivalent to or over £20 then the user is informed that they qualified for free delivery
    
    * Checked that if items do exist in the cart then each individual item line has its own row with the following details:
        1. Product Image (only displayed for big and medium screens, on smaller it's hidden)
        2. Checked this links back to individual product page.
        3. Product info and Sku number should always be on display
        4. Quantity update buttons, edit and delete (if Admin)
        5. Checked that the correct quantity is shown in the box.
        6. Tested that the + and – buttons increase or decrease this number.
        7. Checked that + stops and is unable to increment further than 99.
        8. Checked that - gets disabled at 1.

* Checked update button:
    1. Seen that the quantity in the basket has been altered to new selected amount.
    2. Seen the toast message confirming this change.
    3. Checked the rows subtotal has adjusted accordingly.
    4. Checked the overall totals below adjust.
    5. Checked the free next day delivery banner adjusts accordingly

* Pressed the remove link:
    1. Checked that the item is removed from the cart and is no longer displayed.
    2. Seen that the toast message appears confirming the removal.
    3. Checked the rest of the cart reacts accordingly.
    4. Checked that the subtotal is always displayed.
    5. Tested that each row is responsive to screen width and the most important information is always displayed.
    6. Checked the totals are shown underneath the last row and are done so in a clear and obvious manner.

* Pressed the checkout button at the bottom, this takes me to the checkout page.
