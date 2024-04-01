# JUNK TRADER: A Post-Apocalyptic eCommerce Trading Game

![responsiveness](/media/readme_images/responsive.png)
![responsiveness](/media/readme_images/mobile_bp.png)
![responsiveness](/media/readme_images/mobileview.png)

**Visit Junk Trader at [Junk Trader](https://junktrader-d1896583f35f.herokuapp.com/)**


Junk Trader is an engaging web-based game that simulates the experience of trading collectables in a virtual marketplace. In this game, players are immersed in a dynamic world where they can buy and sell various items to build their wealth and climb the ranks of collectors. With a limited amount of funds and a diverse range of collectables available, players must strategically navigate the market to make profitable investments and maximize their profits.

The game challenges players to keep a close watch on market trends and fluctuations in item prices, allowing them to make informed decisions about when to buy and sell. As players accumulate wealth, they can expand their collection, take calculated risks, and ultimately emerge victorious by amassing the most wealth before the game ends. With each passing day, new challenges and opportunities arise, adding an element of excitement and urgency to the gameplay experience.


## Table of Contents
1. [User Stories](#user-stories)
2. [Design and Color Scheme](#design-and-color-scheme)
3. [Features](#features)
4. [Wireframe](#wireframe)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Database Configuration](#database-configuration)
8. [Deployment](#deployment)
9. [Credits](#credits)


## JUNK TRADER User Stories


### User Story 1
As a player in Junk Trader, I want to experience the excitement of trading items, buying and selling to make profits, and upgrading my inventory capacity using real-world payments through Stripe integration.

**Acceptance Criteria:**
1. The game should provide a seamless interface for players to browse, purchase, and sell items using Stripe payments, ensuring secure transactions and convenience.
2. Players should be able to engage in trading activities such as buying low and selling high to accumulate wealth and progress in the game, mirroring the gameplay mechanics of traditional trading games like DopeWars.
3. The inventory system should allow players to upgrade their backpack capacity by spending real currency, providing a sense of progression and enabling them to carry more items for trading.
4. The game's theme and visual elements should evoke a traditional video game atmosphere, incorporating interactive 3D GLB images for all available items to enhance immersion and engagement.

### User Story 2
As a player in Junk Trader, I want to experience the challenge of managing limited inventory space and navigating through dynamic market conditions, including fluctuating item prices and random events.

**Acceptance Criteria:**
1. Players should face the challenge of managing a limited backpack capacity, which can be upgraded by purchasing capacity upgrades using in-game currency earned through successful trades.
2. Item prices should fluctuate dynamically as players travel to different locations within the game world, reflecting supply and demand factors, and presenting opportunities for strategic trading decisions.
3. Players should be able to choose the difficulty level at the beginning of the game, which determines the starting amount of player funds and the intensity of market fluctuations and random events, catering to different player preferences and skill levels.

### User Story 3
As a player in Junk Trader, I want to track my progress, compare my performance with others, and aim for high scores by completing the game objectives within the 30-day time limit.

**Acceptance Criteria:**
1. The game should display the player's progress and current score, indicating the total funds accumulated through successful trades and transactions throughout the game duration.
2. Players should have the option to view leaderboards and compare their scores with those of other players, fostering competition and motivation to achieve higher rankings.
3. The game should conclude after 30 in-game days or a set number of location visits, prompting players to compare their final scores with others and celebrate their achievements.
4. Players should have the ability to review all items in their backpack, including their prices, to make informed decisions about selling or keeping items for future trades, enhancing strategic planning and gameplay depth.


## Design and Color Scheme

Junk Trader immerses players in a post-apocalyptic world where they traverse between various run-down locations, depicting an industrial and handcrafted aesthetic characterized by rusty metal and decaying city backgrounds. The game's design aims to evoke a sense of gritty realism while incorporating elements of futuristic technology and innovation.

![logo](/media/logo.png)

### Colour Scheme
- The primary color palette revolves around a blend of red and black, symbolizing danger, urgency, and the harsh realities of the game's environment.
- Red is prominently featured throughout the interface, serving as a focal point for important elements such as buttons, alerts, and borders.
- To provide visual contrast and prevent color fatigue, mild respite colors are strategically employed in profile sections and upgrade screens, offering relief from the intensity of the red-dominated environment.
- Laser-like red borders and shading add a touch of futuristic flair, enhancing the overall aesthetic and reinforcing the game's theme of technological advancement amidst decay.

![Design](/media/readme_images/index.png)

### Font and Typography
- The font choice reflects the rugged and worn-down nature of the post-apocalyptic setting, featuring a distressed and weathered appearance that complements the industrial theme.
- Text is rendered in a stylized manner, resembling handwritten markings on scrap metal or makeshift signage commonly found in dystopian landscapes.
- The typography enhances immersion by reinforcing the narrative of survival and resourcefulness, conveying a sense of urgency and determination as players navigate the treacherous world of Junk Trader.

In essence, the design and color scheme of Junk Trader aim to transport players into a harsh yet captivating world, where every transaction and decision carries weight amidst the remnants of civilization's collapse. Through a blend of industrial aesthetics, futuristic accents, and thematic typography, the game creates an immersive experience that challenges players to thrive in the face of adversity.

### Base Template

- The base template defines the overall structure and layout of the web pages. It includes common elements like the header, navigation, and footer.
- It imports various CSS and JavaScript libraries, such as Bootstrap, Font Awesome, and jQuery, to style and enhance the functionality of the interface.
- The header section contains a navigation bar with dropdown menus for user options like profile management, authentication, and logout.
- Additionally, it displays dynamic information such as the player's funds, backpack capacity, days played, and various action links related to trading and upgrades.
- The template also includes JavaScript functions for dropdown menu functionality, GLB viewer lighting, updating player funds dynamically, and displaying toast messages.

### Landing Page

- The index template represents the home page of the application.
- It extends the base template and overrides specific blocks to insert content unique to the home page.
- The content section includes a welcome message and options for the user to choose the game difficulty.
- It also provides a modal dialog explaining how to play the game, outlining steps such as starting with funds, exploring markets, buying and selling collectibles, managing the backpack, and achieving victory.
- JavaScript code is included to validate the form submission when selecting the game difficulty, ensuring that a difficulty level is chosen before proceeding.
- A user must login to begin the game.


## Features

Junk Trader offers a diverse range of features designed to immerse players in a post-apocalyptic world, including interactive 3D models, dynamic market exploration, strategic buying and selling mechanics, and real-time market trend monitoring, all aimed at providing an engaging and immersive gaming experience.

### Main Game Console

The main game console serves as the central hub for players to interact with the game. Here's what players can do from this console:

![Console](/media/readme_images/interface.png)

- **View Available Funds:** Players can see their available funds displayed dynamically on the interface, allowing them to track their financial status within the game.

- **View Backpack Capacity:** Players can view how many items in their backpack and how close to capacity it is

- **Navigate to Upgrades:** By clicking on the "Upgrades" option, players can access the upgrades section where they can enhance their gameplay experience by acquiring various upgrades.

- **Check Remaining Days:** The console displays the number of days left in the game, providing players with a sense of urgency and helping them plan their strategies accordingly.

- **Navigate to Trading Window:** Players can access the trading window from the console, where they can view a variety of tradable items available in virtual markets. This feature enables players to engage in buying and selling activities to advance in the game.

### Custom Apps

### **home**:
- Displays the homepage for initiating the game
- Prompts players to login
- Once logged in a player must choose a difficulty level which will determine the starting player funds for game play.

### **collectables**:
- Allows browsing, buying, and selling of collectible items.
- Interactive 3D files
- Manages inventory and item pricing.
- Prices fluctuate each new loaction and game day played.

![Collectables](/media/readme_images/items.png)

### **backpack**:
- Manages user inventory and storage capacity.
- Enables adding, removing, and organizing items though buying and selling them for profit or loss.

![Backpack](/media/readme_images/backpack.png)

### **places and side panel**:
- Represents different game locations or markets.
- Offers unique prices and trading dynamics.
- Enables navigation between locations.

![Collectables](/media/readme_images/sidepanel.png)

### **upgrades**:
- Enhances gameplay with upgrades or improvements.
- Offers increased backpack capacity.
- Implements systems for unlocking and purchasing upgrades through stripe payments.

![Collectables](/media/readme_images/upgrades.png)

![Stripe](/media/readme_images/stripe.png)

### **profiles**:
- Manages user accounts, registration, and authentication.
- Allows users to create and manage profiles.
- Handles authentication and access control.

![Profile](/media/readme_images/profile.png)

### **end_of_game**:
- Determines end-game scenarios and victory conditions.
- Calculates final scores and rankings.
- Displays leaderboards and rewards.

![End of Game](/media/readme_images/endofgame.png)

### User Authentication
- Users can register, login, and logout of their accounts.
- Authentication is implemented using Django's built-in authentication system.

![Login](/media/readme_images/login.png)

### Trading Screen
![Trading Screen](/media/readme_images/items.png)
### Profile Management
- Authenticated users can access their profiles, view their information, and make changes if necessary.
- Superusers have access to an admin panel.

### Scores 
- users can view their own scores and other players top scores from thier profile
![Scores](/media/readme_images/profile.png)

### Toasts 
- Toasts for alerts and game actions are thoughout the site
![Toasts](/media/readme_images/toasts.png)
![Toasts](/media/readme_images/toast2.png)
### Collectibles and Trading
- **Market Exploration:** Users can explore virtual markets filled with a variety of collectibles.
- **Buying and Selling:** Players can use virtual funds to buy and sell collectibles, aiming to make a profit.

### Game Difficulty Selection
- **Difficulty Levels:** Users can choose the game difficulty level (easy, medium, difficult) before starting the game.

### Backpack Management
- **Limited Capacity:** Players have a backpack with limited capacity to carry items.
- **Efficient Management:** They need to manage their backpack space efficiently while collecting items.

### Market Trends and Fluctuations
- **Strategic Decisions:** Users need to keep an eye on market trends and fluctuations in item prices to make strategic decisions.

### Time Limit
- **Limited Time:** Time is limited in the game, with each passing day bringing new challenges and opportunities.

### Tutorial Modal
- **Guidance:** A modal dialog explains how to play the game, outlining steps such as starting with funds, exploring markets, buying and selling collectibles, managing the backpack, and achieving victory.

### Responsive Design
- **Optimal Viewing:** The interface is designed to be responsive, ensuring compatibility and optimal viewing across various devices and screen sizes.




## Scalability and Future Development

While the basic elements for a trading game are in place, there is much room for a more enjoyable playing experience.  Some ideaa for future development include:

- **Loan Sharks**: Introducing the risk of borrowing from loan sharks would add a layer of financial pressure and consequence management for players and mak for a more enjoyable experience.
- **Police Encounters**: Incorporating random police encounters would inject a sense of urgency and risk into navigating between locations, adding a dynamic element to gameplay.
- **Tipoffs**: Implementing tipoffs or warnings about police activity or rival traders' movements could introduce strategic decision-making and anticipation elements.
- **Undercover Operations**: Including undercover operations or informant mechanics would provide players with valuable insights and opportunities for espionage and counterintelligence.
- **Black Market Deals**: Offering opportunities for black market transactions would present players with higher-risk, higher-reward avenues for profit and intrigue.
- **Gang Warfare**: Introducing conflicts and alliances with rival trader factions could open up possibilities for negotiation, conflict resolution, and territorial control.
- **Smuggling Operations**: Allowing players to undertake smuggling operations could introduce challenges and rewards related to navigating borders and evading detection.
- **Legal Troubles**: Including legal troubles such as lawsuits or fines could introduce additional challenges and consequences for players' actions.

## Wireframe
Original Concept designed on lucid 

![Junk Trader Wireframes](/media/readme_images/wireframe1.jpeg)
![Junk Trader Wireframes](/media/readme_images/wireframe2.jpeg)
![Junk Trader Wireframes](/media/readme_images/wireframe3.jpeg)
![Junk Trader Wireframes](/media/readme_images/wireframe4.jpeg)

## Technologies Used
JUNKTRADER leverages a range of technologies to ensure a seamless user experience:

- **HTML5** for structuring the content.
- **CSS** for styling and layout.
- **JavaScript** for interactive features.
- **Font Awesome** for icons.
- **Bootstrap** for enhanced styling.
- **Google Fonts** to enhance typography.
- **JQuery** for dynamic behavior.
- **Python** for server-side scripting.
- **Jinja templating** for rendering dynamic content.
- **SQL** for database queries 
- **Adobe Express** for logo and image generation
- **AWS** for media and static file handling
- **Git and GitHub** for version control and project hosting.

## Testing

### User Stories Testing
Here's how Junk Trader fulfills the expectations of its users:

- **Navigating through Junk Trader is intuitive, thanks to its user-friendly layout and easily accessible content.** The platform has been meticulously designed with user experience in mind, ensuring that users can effortlessly find their way around and access the content they seek.

- **The platform effectively serves its purpose by connecting players with trading opportunities and collectibles.** Junk Trader's core functionality is tested to ensure that it seamlessly connects users with trading options, collectibles, and in-game opportunities, meeting the expectations of a diverse player base.

- **Junk Trader offers a console for interactive 3D models, enhancing the overall user experience.** Interactive 3D models are tested to provide a seamless viewing experience, ensuring that users can engage with collectibles and trading items effectively.

- **Players can create accounts, manage their backpack, and actively engage within the game community.** All user-related features are extensively tested to guarantee that players can easily create accounts, manage their inventory, and actively participate in community interactions.

- **The design and color scheme contribute to an immersive gaming experience.** Junk Trader's visual elements and design choices are tested to enhance the overall appeal of the platform, contributing to an immersive and engaging gaming experience.

Testing Junk Trader against these user stories ensures that the platform delivers on its promises and provides a user-friendly and captivating experience for all its players.


### Automated vs Manual Testing

In testing Junk Trader, a combination of automated and manual testing approaches was employed, each serving specific purposes depending on the nature of the testing required.

**Automated Testing:**
A straightforward test was created to ensure the home app to make sure it is working correctly. It sends a request to the main page and checks the response's status code. If the status code is 200, it means everything is working as expected.


        from django.test import TestCase
        from django.urls import reverse

        class HomePageTestCase(TestCase):
            
            def test_main_page_response(self):
                # Send a GET request to the main page
                response = self.client.get(reverse('home:index'))
                # Check if the response status code is 200
                self.assertEqual(response.status_code, 200)

In this test:

TestCase from django.test for creating a test case.
Import reverse from django.urls to generate the URL for the home view.
Define a test method test_main_page_response to check the response of the main page.
Inside the test method uses self.client.get() to send a GET request to the main page using the generated URL.
Self.assertEqual() to assert that the response status code is 200, indicating that the page is accessible.

## Manual Tests

1. **User Registration and Login:**
   - Tested the user registration process by creating a new account with a unique username and password.
   - Logged in with the newly created account to verify that the login functionality works.
   - Attempted logging in with incorrect credentials to ensure that the system handles authentication errors properly.

2. **Navigation and UI Layout:**
   - Explored the platform to ensure that navigation is intuitive and the UI layout is user-friendly.
   - Checked for consistent design elements and proper alignment of elements across different pages.

3. **Profile Management:**
   - Verified that users can edit their profiles.
   - Checked if changes made to the profile are reflected correctly throughout the platform.

4. **Backpack Management:**
   - Tested the functionality related to managing the user's backpack, including adding, removing, and viewing items.
   - Ensured that the backpack capacity is accurately represented and enforced.

5. **Trading Window:**
   - Navigated to the trading window to view tradable items.
   - Checked if users can browse available items, view item details, and initiate trade transactions.

6. **Market Trends and Fluctuations:**
   - Monitored market trends and fluctuations to ensure that prices are dynamically adjusted based on supply and demand.
   - Verified that users receive accurate and timely information about market conditions.

7. **Upgrade System:**
   - Explored the upgrade system to understand available upgrades and their effects on gameplay.
   - Tested the process of purchasing and applying upgrades to enhance user experience and gameplay mechanics.

8. **Error Handling and Validation:**
   - Deliberately triggered various error conditions, such as submitting invalid input or exceeding limits, to assess how the system handles errors.
   - Verified that users receive appropriate error messages and the system gracefully handles exceptional scenarios.

9. **Performance Testing:**
    - Observed the platform's performance under different load conditions to ensure responsiveness and scalability.
    - Checked for any latency issues, slow loading times, or performance bottlenecks.

10. **Security Testing:**
    - Evaluated the platform's security measures, including authentication mechanisms, data encryption, and protection against common vulnerabilities such as XSS and CSRF.
    - Verified that user data is securely stored and transmitted.

11. **Accessibility Testing:**
    - Ensured that the platform is accessible to users with disabilities by testing with assistive technologies such as screen readers and keyboard navigation.
    - Checked for compliance with accessibility standards and guidelines.

These manual tests cover various aspects of Junk Trader, ensuring that the platform meets user expectations, provides a seamless user experience, and maintains security, performance, and accessibility standards.

## Database Configuration

In the Junk Trader application, the database configuration plays a crucial role in managing data storage and relationships between different components. Below is an outline of the database configuration for the application:

#### Models Overview:
1. **Collectable Model:**
   - `name`: CharField (max_length=100)
   - `description`: TextField
   - `price`: DecimalField (max_digits=6, decimal_places=2)
   - `previous_price`: DecimalField (max_digits=10, decimal_places=2, default=0)
   - `image_url`: URLField (max_length=1024, null=True, blank=True)
   - `image`: ImageField (null=True, blank=True)
   - `glb_file`: FileField (upload_to='glb_files/', null=True, blank=True)

2. **Location Model:**
   - `name`: CharField (max_length=100)
   - `description`: TextField
   - `picture`: ImageField (upload_to='location_pictures/')

3. **Upgrade Model:**
   - `name`: CharField (max_length=100)
   - `price`: DecimalField (max_digits=10, decimal_places=2)
   - `glb_file`: FileField (upload_to='glb_files/', null=True, blank=True)
   - `capacity`: IntegerField (default=50)

4. **UserProfile Model (Player Model):**
   - `user`: OneToOneField to User (on_delete=models.CASCADE)
   - `scores`: IntegerField (default=0)
   - `date`: DateField (auto_now_add=True)

#### Database Relationships:
- **Collectable - Location:** There is no direct relationship between Collectable and Location models.
- **Collectable - Upgrade:** There is no direct relationship between Collectable and Upgrade models.
- **UserProfile - Upgrade:** There is no direct relationship between UserProfile and Upgrade models.
- **UserProfile - Collectable:** There is no direct relationship between UserProfile and Collectable models.

#### Database Diagram:
The database diagram visually illustrates the structure of the database, including the tables and their relationships. It provides a clear overview of how the Collectable, Location, Upgrade, and UserProfile models are interconnected within the database schema.

#### Database Configuration:
Configuring the database involves setting up the database backend, defining models, performing migrations, and managing database operations using Django's Object-Relational Mapping capabilities. Django offers convenient tools for managing database interactions, ensuring efficient storage, retrieval, and management of data according to the requirements of the Junk Trader game.


                      +------------------+           +-------------------+             +--------------+
                      |    Collectable   |           |     Upgrade       |             |    Player    |
                      +------------------+           +-------------------+             +--------------+
                      | _id              |           | _id               |             | _id          |
                      | name             |           | name              |             | username     |
                      | description      |           | price             |             | score        |
                      | price            |           | glb_file          |             |              |
                      | previous_price   |           | capacity          |             |              |
                      | image_url        |           +-------------------|             |              |
                      | image            |                               |             |              |
                      | glb_file         |                               |             |              |
                      +------------------+                               |             |              |
                               |                                        |             |              |
                               |                                        |             |              |
                               |                                        |             |              |
                               |                                        |             |              |
                               |                                        |             |              |
                      +------------------+                               |             |              |
                      |     Location     |                               |             |              |
                      +------------------+                               |             |              |
                      | _id              |                               |             |              |
                      | name             |                               |             |              |
                      | description      |                               |             |              |
                      | picture          |-------------------------------|             |              |
                      +------------------+                                              |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          |              |
                                                                                          +--------------+



### Backpack App Contexts:

#### `backpack_contents`:
- **Description:** Retrieves the contents of the user's backpack from the session and calculates various statistics such as total value, total quantity, and total number of unique collectables.
- **Variables:**
  - `backpack_items`: List containing dictionaries for each item in the backpack, including item ID, quantity, collectable details, and subtotal.
  - `total`: Total value of all items in the backpack.
  - `total_quantity`: Total quantity of all items in the backpack.
  - `collectable_count`: Total number of unique collectables in the backpack.
  - `grand_total`: Overall total value of all items in the backpack.
- **Usage:** Typically used to render the backpack contents in templates, providing information about the items stored in the backpack.

#### `total_amount`:
- **Description:** Returns the total amount in the user's backpack.
- **Variables:**
  - `total_amount`: List containing the total amount.
- **Usage:** Provides the total amount to be used in various parts of the application, such as displaying the total cost of items in the backpack.

#### `days_played`:
- **Description:** Retrieves the number of days played from the session.
- **Variables:**
  - `days_played`: Number of days played by the user.
- **Usage:** Typically used to display the number of days played in templates or views to provide feedback to the user about their progress.

These contexts are essential for providing information about the user's backpack and gameplay progress within the application. They are utilized to render dynamic content in templates and views, enhancing the user experience.


## Deployment

JUNK TRADER is successfully deployed on Heroku, You can access the live site at [JUNK TRADER Website Link](https://junktrader-d1896583f35f.herokuapp.com/).

## Credits

### JUNK TRADER vs BOUTIQUE ADO

Junktrader has leveraged the technology and architecture of the Code Institute Boutique_Ado project, introducing significant modifications to create a trading game platform. The project's foundation builds upon the eCommerce architecture, emphasising the adaptability and reusability of technology across diverse use cases.


**Database Management and AWS**

Similar to Boutique Ado, JUNK TRADER maintains the CRUD (Create, Read, Update, Delete) database practices at its core. JUNK TRADER utilises practices to handle buying and selling, and user interactions. 

**Deployment on Heroku**

In line with the Boutique Ado's deployment approach, JUNK TRADER is hosted on Heroku, ensuring scalability and accessibility for a broad user base. Heroku's reliability for web applications supports JUNK TRADER in reaching a wide audience.


### Content
GLB Viewer instructions.
- https://www.youtube.com/watch?v=lsTc8WypC18

Inspiration for gameplay from DopeWars
- https://codepen.io/boomer1204/pen/MKWyQR

Django Views and URLS instructions
- https://www.youtube.com/watch?v=Z4D3M-NSN58&list=PLzMcBGfZo4-kQkZp-j9PNyKq7Yw5VYjq9
- ChatGPT for help with some Views and URL paths

- Redirects, Returns and User restriction 
https://stackoverflow.com/questions/67610712/how-do-i-restrict-an-users-access-with-flask-principal-and-flask-security

### Media
- All 3D images are from SketchFab and the content is owned by the creators.  
- The Logo was designed by Ben Hayes on Adobe Express
- The Background Image is from Adobe Express



