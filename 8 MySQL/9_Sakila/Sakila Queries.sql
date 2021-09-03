USE sakila;

-- 1
SELECT city.city_id, city.city, customer.first_name, customer.last_name, customer.email, address.address
	FROM customer, city, address 
    WHERE city.city_id = 312 AND city.city_id = address.city_id AND address.address_id = customer.address_id;

-- 2
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
	FROM film INNER JOIN film_category ON film.film_id = film_category.film_id
        INNER JOIN category ON film_category.category_id = category.category_id
        AND category.name = 'Comedy';

-- 3
SELECT actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name, film.film_id, film.title, film.description, film.release_year
	FROM film INNER JOIN film_actor ON film.film_id = film_actor.film_id
        INNER JOIN actor ON film_actor.actor_id = actor.actor_id
        AND actor.actor_id = 5;

-- 4
SELECT store.store_id, city.city_id, customer.first_name, customer.last_name, customer.email, address.address
	FROM store, customer, city, address
		WHERE store.store_id = customer.store_id
        AND customer.address_id = address.address_id
        AND address.city_id = city.city_id
        AND store.store_id = 1
        AND (city.city_id = 1 OR city.city_id = 42 OR city.city_id = 312 OR city.city_id = 459);

-- 5
SELECT film.title, film.description, film.release_year, film.rating, film.special_features
	FROM actor, film, film_actor
        WHERE film.film_id = film_actor.film_id
        AND film_actor.actor_id = actor.actor_id
        AND film_actor.actor_id = 15
        AND film.rating = 'G'
        AND film.special_features LIKE '%behind the scenes%';

-- 6
SELECT film.film_id, film.title, film_actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) AS actor_name
	FROM actor, film, film_actor
        WHERE film.film_id = film_actor.film_id
        AND film_actor.actor_id = actor.actor_id
        AND film.film_id = 369;

-- 7
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre, film.rental_rate
	FROM film, category, film_category
		WHERE film.film_id = film_category.film_id 
        AND film_category.category_id = category.category_id 
        AND film.rental_rate = 2.99
        AND category.name = 'Drama';

-- 8
SELECT actor.actor_id, CONCAT(actor.first_name, " ", actor.last_name) AS actor_name, film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
	FROM actor, film, film_actor, category, film_category
        WHERE film.film_id = film_actor.film_id
        AND film_actor.actor_id = actor.actor_id
        AND film.film_id = film_category.film_id
        AND film_category.category_id = category.category_id
        AND actor.first_name = 'SANDRA'
        AND actor.last_name = 'KILMER'
        AND category.name = 'Action';