select DR_NAME,DR_ID,MCDP_CD,DATE_FORMAT(HIRE_YMD,'%Y-%m-%d') as HIRE_YMD
from DOCTOR
where mcdp_cd = 'CS' OR mcdp_cd = 'GS'
order by hire_ymd desc, dr_name