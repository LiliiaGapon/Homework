#1 -- database
create database if not exists courses;

create table if not exists students (student_no int auto_increment, 
                                     teacher_no int, 
									  course_no int, 
						           student_name varchar(255), 
                                          email varchar(255), 
                                     birth_date date,
                                     primary key (student_no, birth_date));
                                     
create table if not exists teachers (teacher_no int, 
								   teacher_name varchar(255), 
                                       phone_no bigint);
create table if not exists courses (course_no int, 
								  course_name varchar(255),
                                   start_date date,
                                     end_date date);
                                     
create index students_ind on students (email);

create unique index teachersPhone_ind on teachers (phone_no);

alter table students
partition by range (year(students.birth_date)) (
                                 partition p1 values less than (2001),
                                 partition p2 values less than (2002),
                                 partition p3 values less than (2003)
                                 );

#2
insert into students (teacher_no, course_no, student_name, email, birth_date)
values (100,25,'Kolesnik Anna','kol_anna@gmail.com','2001-12-03'),
       (101,26,'Kogut Yulia','kogyul@gmail.com','2000-05-06'),
       (101,26,'Kogut Yurii','kogyur@gmail.com','2000-05-06'),
       (101,26,'Velychko Andrii','velyk@gmail.com','2000-03-03'),
       (101,26,'Torlop Dmytro','tordim@gmail.com','2000-07-04'),
       (100,25,'Leichenko Viktoriya','Leichenko@gmail.com','2001-09-08'),
       (100,25,'Leichenko Oleksandr','Leichenko-olex@gmail.com','2001-07-21'),
       (102,27,'Koval Viktoriya','koval_viktoriya@gmail.com','2002-09-08'),
       (102,27,'Koval Dmytro','koval_dima@gmail.com','2002-07-15'),
       (102,27,'Ignat Anastasia','ignat_anastasia@gmail.com','2002-12-24');
	
insert into teachers (teacher_no, teacher_name, phone_no)
values (100,'Minka G.V.',380978569475),
       (101,'Timoshenko D.T.',380665746594),
       (102,'Gogol S.M.',380931256987);
       
insert into courses (course_no, course_name, start_date, end_date)
values (25,'English 5','2022-09-01', '2023-05-31'),
       (26,'Polska 5','2022-09-01', '2023-05-31'),
       (27,'Spenish 5','2022-09-01', '2023-05-31');

#3
explain select*
from students
where birth_date between '2000-01-01' and '2000-12-31';
-- id, select_type, table, partitions, type, possible_keys, key, key_len, ref, rows, filtered, Extra
-- '1', 'SIMPLE', 'students', 'p1',     'ALL', NULL,          NULL, NULL,  NULL, '4', '25.00', 'Using where'

#4
explain select*
from teachers
where phone_no = 380665746594;
-- id, select_type, table, partitions, type, possible_keys, key, key_len, ref, rows, filtered, Extra
--  '1', 'SIMPLE', 'teachers', NULL,   'const', 'teachersPhone_ind', 'teachersPhone_ind', '9', 'const', '1', '100.00', NULL

alter table teachers alter index teachersPhone_ind invisible;
explain select*
from teachers
where phone_no = 380665746594;
-- id, select_type, table, partitions, type, possible_keys, key, key_len, ref, rows, filtered, Extra
-- '1', 'SIMPLE', 'teachers', NULL,    'ALL', NULL,         NULL, NULL,   NULL, '3', '33.33', 'Using where'

alter table teachers alter index teachersPhone_ind visible;

#5
insert into students (teacher_no, course_no, student_name, email, birth_date)
values (102,27,'Ignat Anton','ignat_anton@gmail.com','2002-07-24'),
       (102,27,'Ignat Anton','ignat_anton@gmail.com','2002-07-24'),
       (102,27,'Ignat Anton','ignat_anton@gmail.com','2002-07-24');
       
#6
select* 
from students 
where student_name in (select student_name from students group by student_name having COUNT(*) > 1);


-- Query
#1
select year(from_date), round(avg(salary)) as avgSalary
from salaries
where from_date<='2005-01-01'
group by year(from_date)
order by year(from_date);

#2
select dept_no, round(avg(salary)) as avgSalary
from salaries t1
join dept_emp t2
on t1.emp_no=t2.emp_no
where t1.to_date>now()
group by dept_no
order by dept_no;

#3
select dept_no,year(t1.from_date), round(avg(salary)) as avgSalary
from salaries t1
join dept_emp t2
on t1.emp_no=t2.emp_no
group by dept_no,year(t1.from_date)
order by dept_no;

#4 
select year(t1.from_date) 'year',dept_no, round(avg(salary)) as avgSalary,count(t1.emp_no) allem
from salaries t1
join dept_emp t2
on t1.emp_no=t2.emp_no
group by year(t1.from_date)  ,dept_no
order by year(t1.from_date),allem desc;

#5
SELECT  t1.emp_no,t1.dept_no,t1.from_date,t1.to_date,t2.birth_date,concat(t2.first_name,' ',t2.last_name) fullname,t2.hire_date,t3.salary,t4.title
FROM dept_manager t1
join employees t2
on t1.emp_no=t2.emp_no
join salaries t3
on t1.emp_no=t3.emp_no
join titles t4
on t1.emp_no=t4.emp_no
where t1.to_date>now()
order by t1.from_date
limit 1

#6
select *,(salary-avgSal)diff
from
(select t1.emp_no,salary,t2.dept_no, round(avg(salary)over(partition by dept_no)) avgSal
from salaries t1
join dept_emp t2
on t1.emp_no=t2.emp_no
where t1.to_date>now() 
and t2.to_date>curdate())a
order by diff desc
limit 10

#7
select*,round(totalSal/12) 'sal/mon',count(emp_no)over(partition by dept_no) numEm, round(salary/12) osal  
from
(select dept_no,t1.emp_no,salary,sum(salary)over(partition by dept_no) as totalSal
from salaries t1
join dept_emp t2
on t1.emp_no=t2.emp_no
where t1.to_date>now() 
and t2.to_date>curdate()
order by dept_no,salary)a
order by osal 
       