/*VIEWS -------------------------*/

--------------------------------------------------------------------
CREATE VIEW `fpsgames` AS
(SELECT g1.game_name, g1.gametype
FROM games AS g1,creategamesrel AS g2 
WHERE g1.game_id = g2.game_id AND g2.contentdetails LIKE '%FPS%')

--------------------------------------------------------------------
CREATE VIEW TodayNews AS
(SELECT * 
FROM news AS n 
WHERE n.newsDate >= CURDATE())
------------------------------------------------------------

CREATE VIEW createdgamesbymod AS(
SELECT m.mod_nick, g1.game_name
FROM games AS g1, creategamesrel AS g2, moderator AS m
WHERE g1.game_id = g2.game_id AND g2.mod_id = m.mod_id)

-----------------------------------------------------------

CREATE VIEW whoaddmusic AS(
SELECT m2.mod_nick,m1.music_artist, m1.music_name
FROM music AS m1, createmusicrel AS c, moderator AS m2
WHERE m1.music_id = c.music_id AND c.mod_id = m2.mod_id)

------------------------------------------------------------

CREATE VIEW totalgamesaddedtoday AS(
SELECT COUNT(*) AS totalgame ,MAX(g2.date) AS Todaydate
FROM games AS g1, creategamesrel AS g2, moderator AS m 
WHERE g1.game_id = g2.game_id AND g2.mod_id = m.mod_id AND 
g2.date >= CURDATE()

------------------------------------------------------------


CREATE VIEW lasttenreview AS(
SELECT u.user_name,w.about,r.reviewdate,w.rating
FROM user_review AS r, general_user AS g, user AS u, userwritesrel AS w
WHERE g.usermail = u.user_mail AND g.user_id = r.user_id AND w.review_id = r.review_id
LIMIT 10)
-----------------------------------------------------------

CREATE VIEW topratedmusic AS(
SELECT m.music_name ,c.contentdetails
FROM music AS m, createmusicrel AS c
WHERE m.music_id = c.music_id
ORDER BY m.rating DESC
LIMIT 1)

----------------------------------------------------------

CREATE VIEW topratedgame AS(
SELECT g.game_name ,c.contentdetails,g.rating
FROM games AS g, creategamesrel AS c
WHERE g.game_id = c.game_id
ORDER BY g.rating DESC
LIMIT 1)

-----------------------------------------------------------
CREATE VIEW topratedmovie AS(
SELECT m.movie_name ,c.contentdetails,m.rating
FROM movies AS m, createmoviesrel AS c
WHERE m.movie_id = c.movie_id
ORDER BY m.rating DESC
LIMIT 1)
----------------------------------------------------------
