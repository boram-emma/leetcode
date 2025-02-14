# Write your MySQL query statement below
SELECT s.student_id as student_id, s.student_name as student_name, sb.subject_name as subject_name, count(e.subject_name) as attended_exams
from Students s
join Subjects sb
left join Examinations e
on s.student_id = e.student_id and sb.subject_name = e.subject_name
group by 1,2,3
order by 1,3

-- select st.student_id, st.student_name, ex.subject_name, count(*) as attended_exams
-- from Student st
-- join Examinations ex on st.student_id = ex.student_id
-- group by st.student_id, ex.subject_name
-- order by student_id, subject_name