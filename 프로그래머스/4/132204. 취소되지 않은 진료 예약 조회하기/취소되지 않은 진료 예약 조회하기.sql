select APNT_NO, (select PT_NAME from PATIENT where PT_NO = a.PT_NO) as PT_NAME, PT_NO, MCDP_CD, 
(select DR_NAME from DOCTOR where DR_ID = a.MDDR_ID) as DR_NAME, APNT_YMD
from APPOINTMENT a
where APNT_CNCL_YN = 'N' and APNT_YMD like '2022-04-13%' and MCDP_CD = 'CS'
order by APNT_YMD