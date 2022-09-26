WITH t1 AS ( 
	SELECT score, ROW_NUMBER ( ) OVER ( ORDER BY score DESC ) AS rank
	FROM Scores
	GROUP BY score 
) 
SELECT A.score, t1.rank
FROM Scores AS A INNER JOIN t1 ON A.score = t1.score 
ORDER BY A.score DESC