SELECT
TITLE, BOARD.BOARD_ID, REPLY_ID, REPLY.WRITER_ID, REPLY.CONTENTS, 
DATE_FORMAT(REPLY.CREATED_DATE,'%Y-%m-%d') AS CREATED_DATE
FROM USED_GOODS_BOARD BOARD
INNER JOIN USED_GOODS_REPLY REPLY
ON BOARD.BOARD_ID = REPLY.BOARD_ID
WHERE
YEAR(BOARD.CREATED_DATE) = 2022 AND
MONTH(BOARD.CREATED_DATE) = 10
ORDER BY
REPLY.CREATED_DATE,
BOARD.TITLE
;