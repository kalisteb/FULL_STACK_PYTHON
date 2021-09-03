USE friends;
-- X.
SELECT users.first_name, users.last_name, users2.first_name AS friend_first_name, users2.last_name AS friend_last_name 
	FROM users
		LEFT JOIN friendships ON users.id=friendships.user_id
		JOIN users AS users2 ON friendships.friend_id=users2.id;

-- 1.
SELECT users.first_name, users.last_name, users2.first_name AS friend_first_name, users2.last_name AS friend_last_name
	FROM users
        LEFT JOIN friendships ON users.id = friendships.friend_id
        AND users.first_name = 'Kermit'
        JOIN users AS users2 ON friendships.user_id = users2.id;

-- 2.
SELECT COUNT(friendships.id) AS 'Number of Friendships'
	FROM friendships;
    
-- 3.
SELECT users.first_name, users.last_name, COUNT(friendships.id) AS 'Number of Friends'
	FROM users
        LEFT JOIN friendships ON users.id = friendships.user_id
        JOIN users AS users2 ON friendships.friend_id=users2.id
		GROUP BY users.id
		ORDER BY 'Number of Friends' DESC
		LIMIT 1;

-- 4.
INSERT INTO users (first_name, last_name, created_at) VALUES ('Jhon', 'Doe', NOW());
INSERT INTO friendships (user_id, friend_id, created_at) VALUES (6, 2, NOW()),(6, 4, NOW()),(6, 5, NOW());

-- 5.
SELECT users.first_name AS friend_first_name, users.last_name AS friend_last_name, users2.first_name, users2.last_name
	FROM users
        LEFT JOIN friendships ON users.id = friendships.user_id
        JOIN users AS users2 ON friendships.friend_id = users2.id
        AND users2.first_name = 'Eli'
		ORDER BY users.first_name ASC;

-- 6
DELETE FROM friendships WHERE user_id=2 AND friend_id=5;

-- 7.
SELECT CONCAT(users.first_name, ' ', users.last_name) AS user_name, CONCAT(users2.first_name,' ',  users2.last_name) AS friend_name
	FROM users
        LEFT JOIN friendships ON users.id = friendships.user_id
        JOIN users AS users2 ON friendships.friend_id = users2.id;