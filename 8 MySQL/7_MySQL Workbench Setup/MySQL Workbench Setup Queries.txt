USE twitter;

SELECT * FROM tweets;

SELECT 
	id, tweet, created_at
	FROM tweets
	WHERE created_at < '2011-01-01 00:00:00';

INSERT INTO users (first_name, last_name, handle, birthday, created_at, updated_at)
VALUES ('Karina', 'Aliste', 'none', '1983-02-19', NOW(), NOW());

SELECT * FROM users;
    
UPDATE users 
	SET handle = 'all'
	WHERE id = 10;

SELECT * FROM users;

INSERT INTO users (first_name, last_name, handle, birthday, created_at, updated_at)
VALUES ('Karina', 'Aliste', 'none', '1983-02-19', NOW(), NOW());

SELECT * FROM users;

DELETE FROM users 
	WHERE id BETWEEN 6 AND 11;

SELECT * FROM users;