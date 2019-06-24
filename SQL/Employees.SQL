drop table if exists departments;
drop table if exists dept_emp;
drop table if exists dept_manager;
drop table if exists employees;
drop table if exists salaries;
drop table if exists titles;

CREATE TABLE "departments" (
    "dept_no" VARCHAR   NOT NULL,
    "dept_name" VARCHAR   NOT NULL,
    CONSTRAINT "pk_departments" PRIMARY KEY (
        "dept_no"
     )
);

CREATE TABLE dept_emp (
	emp_no INT NOT NULL,
	dept_no varchar NOT NULL,
	from_date DATE NOT NULL,
	to_date DATE NOT NULL
);

CREATE TABLE dept_manager (
	dept_no varchar NOT NULL,
	emp_no INT NOT NULL,
	from_date DATE NOT NULL,
	to_date DATE NOT NULL
);

CREATE TABLE employees (
	emp_no INT NOT NULL,
	birth_date DATE NOT NULL,
	first_name varchar NOT NULL,
	last_name varchar NOT NULL,
	gender varchar NOT NULL,
	hire_date DATE NOT NULL,
CONSTRAINT "pk_employees" PRIMARY KEY (
        "emp_no"
	)
); 

CREATE TABLE salaries (
	emp_no INT NOT NULL,
	salary INT NOT NULL,
	from_date DATE NOT NULL,
	to_date DATE NOT NULL
); 

CREATE TABLE titles (
	emp_no INT NOT NULL,
	title varchar NOT NULL,
	from_date DATE NOT NULL,
	to_date DATE NOT NULL
); 

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "dept_emp" ADD CONSTRAINT "fk_dept_emp_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_dept_no" FOREIGN KEY("dept_no")
REFERENCES "departments" ("dept_no");

ALTER TABLE "dept_manager" ADD CONSTRAINT "fk_dept_manager_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "salaries" ADD CONSTRAINT "fk_salaries_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

ALTER TABLE "titles" ADD CONSTRAINT "fk_titles_emp_no" FOREIGN KEY("emp_no")
REFERENCES "employees" ("emp_no");

select * from departments;
select * from dept_emp;
select * from dept_manager;
select * from employees;
select * from salaries;
select * from titles;

--List the following details of each employee: employee number, last name, first name, gender, and salary.
select employees.emp_no, employees.last_name, employees.first_name, employees.gender, salaries.salary
FROM employees
JOIN salaries 
ON employees.emp_no=salaries.emp_no; 

--List employees who were hired in 1986.
select first_name, last_name, hire_date 
FROM employees 
WHERE hire_date between '01/01/1986' and '01/01/1987';


--List the manager of each department with the following information: department number, department name, the manager's 
--employee number, last name, first name, and start and end employment dates.

select 

--List the department of each employee with the following information: employee number, last name, first name, and department name.

--List all employees whose first name is "Hercules" and last names begin with "B."

--List all employees in the Sales department, including their employee number, last name, first name, and department name.

--List all employees in the Sales and Development departments, including their employee number, last name, first name, and 
--department name.

--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.



	