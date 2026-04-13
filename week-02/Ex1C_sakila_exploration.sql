/*
a) In the actor table, identification information about the actor is included, such as their ID in the DVD inventory system, their first name, and last name. 
b) In the film table, there is information about the attributes about the films including title, description, rating, rental rates, and so on. 
c) Another table that includes columns for both actor_id and film_id is the film_actor table.
d) The rental table includes attributes about rental activity, such as the film rented, what date and time it was rented and returned, who from staff completed handled the purchase, and the customer who rented it. However, the information is hard to read because the information retrieves attirbutes in numberical format, its not user-friednly so we can't see customer names, film names, staff names, all key imformation.  
e) The inventory table includes attributes about physical store inventory of each film across stores, and when each record was last updated. 
f) In order to understand the names of all films that were rented on a specific date, I need tables film, rental, and inventory. They are related to each other because they share attributes such as film_id, inventory_id or last_updated. The inventory_id can be used to tell which physical copy of a film was rented, and its relationship to the film table through film_id tells us the actual title of the film. 
*/

SELECT rental_id, rental_date, inventory_id FROM rental;
SELECT inventory_id, film_id FROM inventory; 
SELECT film_id, title FROM film;