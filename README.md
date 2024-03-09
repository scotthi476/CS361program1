Microservice Communication Contract

This microservice returns a list of recipes with a star rating requested by a user. Once a user selects the option in the main UI screen, a text “rating” is written to a text file, “callSearchMicroservice.txt”.  This text file works as a communication pipeline. Once the text “rating” is written, this microservice reads the request. Then the microservice converts the rating information to an integer format. (e.g., 4) (function name: convert_rating_int(rating)) then, queries recipe which are returned in a JSON format. Once a recipe is identified, a rating and a recipe name pairs are stored in a dictionary (search_recipe_rating(directory, key)). Then this microservices returns a list of rating and recipe name to the user (write_result(file, list)). 
Microservice request data and receive data Workflow:
 (1) User select star rating search from the UI
 run mainRatingSearchUI.py
 (2) a text “rating” is written to a text file “callSearchMicroservice.txt”
 (3) ratingSearchServiceUI.py is executed
 (4) An user enter a rating (e.g., 4)
 (5) the rating the user entered is written into rating.txt
 (6) ratingSearchService.py is executed

List of functions:
(1) convert_rating_int(rating)
(2) search_recipe_rating(directory, key)
(3) write_result(file, list)
