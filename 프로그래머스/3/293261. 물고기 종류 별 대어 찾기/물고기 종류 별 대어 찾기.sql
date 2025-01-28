SELECT ID, FISH_NAME, LENGTH
FROM FISH_INFO FI
INNER JOIN FISH_NAME_INFO FAI
ON FI.FISH_TYPE = FAI.FISH_TYPE
WHERE LENGTH = (SELECT MAX(LENGTH)
               FROM FISH_INFO
               WHERE FISH_TYPE = FI.FISH_TYPE)
ORDER BY ID