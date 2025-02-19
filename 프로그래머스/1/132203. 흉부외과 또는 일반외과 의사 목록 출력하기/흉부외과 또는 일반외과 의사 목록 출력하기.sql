select DR_NAME,DR_ID,MCDP_CD,TO_CHAR(HIRE_YMD,'YYYY-MM-DD') as HIRE_YMD
from DOCTOR
where mcdp_cd = 'CS' OR mcdp_cd = 'GS'
order by hire_ymd desc, dr_name