SELECT II.ITEM_ID, ITEM_NAME
FROM ITEM_INFO II
INNER JOIN ITEM_TREE IT
ON II.ITEM_ID = IT.ITEM_ID
WHERE PARENT_ITEM_ID IS NULL
ORDER BY II.ITEM_ID