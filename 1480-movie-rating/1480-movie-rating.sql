(SELECT U.name AS results FROM MovieRating MR INNER JOIN users U
ON MR.user_id = U.user_id GROUP BY MR.user_id
ORDER BY COUNT(movie_id) DESC, U.name LIMIT 1)

UNION ALL

(SELECT M.title AS results FROM MovieRating MR INNER JOIN movies M
ON MR.movie_id = M.movie_id
WHERE MONTH(MR.created_at)=02 AND YEAR(MR.created_at)=2020
GROUP BY MR.movie_id ORDER BY AVG(MR.rating) DESC, M.title LIMIT 1)