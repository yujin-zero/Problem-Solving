SELECT RE.REST_ID, REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS, ROUND(AVG(REVIEW_SCORE),2) AS SCORE
FROM REST_REVIEW RE
JOIN REST_INFO INF
ON RE.REST_ID = INF.REST_ID
GROUP BY RE.REST_ID
HAVING ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, FAVORITES DESC