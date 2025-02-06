CREATE DATABASE student_dropout;
USE student_dropout;

CREATE TABLE students (
	student_id varchar(50) primary key,
    name varchar(100),
    age int,
    gender varchar(10)
);
CREATE TABLE performance (
	performance_id int primary key,
    student_id varchar(50),
    semester varchar(20),
    core_subjects float,
    elective_subjects float,
    cgpa float,
    foreign key (student_id) references students(student_id) on delete cascade
);
CREATE TABLE attendance (
	performance_id int primary key,
    student_id varchar(50),
    semester varchar(20),
    total_absence int,
    attendance_rate int,
    foreign key (student_id) references students(student_id) on delete cascade
);
CREATE TABLE disciplinary_actions (
	performance_id int primary key,
    student_id varchar(100),
    semester varchar(20),
    action_taken int,
    remarks varchar(100),
    foreign key (student_id) references students(student_id) on delete cascade
);
SET FOREIGN_KEY_CHECKS = 1;
SELECT * FROM students;
SELECT * FROM performance;
SELECT * FROM attendance;
SELECT * FROM disciplinary_actions;

SHOW TABLES;

SELECT COUNT(*) FROM students;
SELECT COUNT(*) FROM performance;
SELECT COUNT(*) FROM attendance;
SELECT COUNT(*) FROM disciplinary_actions;











