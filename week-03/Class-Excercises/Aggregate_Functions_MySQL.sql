-- ============================================================
-- Aggregate Functions in MySQL: Examples and Best Practice
-- Sharleen Guerrero 
-- April 23, 2026
-- ============================================================

-- Aggregate functions perform a calculation on a set of values and return a single aggregated result. Typically used in GROUP BY to summarize data.
USE sakila;

-- Using COUNT()
SELECT COUNT(*) FROM table_name;
SELECT COUNT(column_name) FROM table_name; -- Counts only non-NULL values

-- Example for COUNT(): Suppose you want to count how many films belong to a specific category (for example, the "Action" category), you can join the film and category tables.
SELECT COUNT(*)
FROM film frating
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = 'Action';


-- Task: Create a business question for the sakila database and write a query to address it.
-- How many unique actors have appeared in PG-rated films for each category?
-- Tables I need: actor, film_actor, film, film_category, category
-- Keys I need: category_id, film_id, actor_id
SELECT c.name AS 'CategoryName', COUNT(DISTINCT a.actor_id) AS 'ActorCount'
FROM category c
INNER JOIN film_category fc 
	ON c.category_id = fc.category_id
INNER JOIN film f 
	ON fc.film_id = f.film_id
INNER JOIN film_actor fa 
	ON f.film_id = fa.film_id
INNER JOIN actor a 
	ON fa.actor_id = a.actor_id
WHERE f.rating = 'PG'
GROUP BY c.name;
-- Managment can use these results to make better stocking decisions. Sports, family, and children categories have the highest count.