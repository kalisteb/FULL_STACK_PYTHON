USE world;

-- 1
SELECT 
    countries.name, languages.language, languages.percentage
	FROM countries, languages
        WHERE languages.language = 'Slovene'
        AND countries.id = languages.country_id
        ORDER BY languages.percentage DESC;

-- 2
SELECT 
    countries.name, COUNT(cities.id) AS cities
	FROM countries, cities
		WHERE countries.id = cities.country_id
		GROUP BY countries.name
		ORDER BY cities DESC;

-- 3
SELECT 
    cities.name, cities.population, countries.id AS country_id
	FROM countries, cities 
		WHERE countries.id = cities.country_id
        AND countries.name = 'Mexico'
        AND cities.population > 500000
		ORDER BY cities.population DESC;

-- 4
SELECT 
    countries.name, languages.language, languages.percentage
	FROM countries, languages
		WHERE countries.id = languages.country_id
			AND languages.percentage > 89
			ORDER BY languages.percentage DESC;
-- 5
SELECT 
    countries.name, countries.surface_area, countries.population
	FROM countries
		WHERE surface_area < 501
        AND population > 100000;

-- 6
SELECT 
    name, government_form, capital, life_expectancy
	FROM countries
		WHERE government_form = 'Constitutional Monarchy'
        AND capital > 200
        AND life_expectancy > 75;

-- 7
SELECT 
    countries.name AS country_name, cities.name AS city_name, cities.district AS district, cities.population
	FROM countries, cities
    WHERE countries.id = cities.country_id
		AND countries.name = 'Argentina'
        AND cities.district = 'Buenos Aires'
        AND cities.population > 500000;

-- 8
SELECT 
    region, COUNT(name) AS 'countries'
	FROM countries
		GROUP BY (region)
		ORDER BY countries DESC;