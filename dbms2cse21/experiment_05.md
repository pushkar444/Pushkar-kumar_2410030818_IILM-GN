## Experiment 5 – Aggregate & String Functions
# Aim:- To perform aggregate functions and string operations on the employee table.

# Query 1:- Display the total number of employees working in the company.
```sql
SELECT COUNT(*) AS total_employees
FROM employee;
```
# Query 2:- Display the total salary being paid to all employees.
```sql
SELECT SUM(sal) AS total_salary
FROM employee;
```
# Query 3:- Display the maximum salary from employee table.
```sql
SELECT MAX(sal) AS maximum_salary
FROM employee;
```
# Query 4:- Display the minimum salary from employee table.
```sql 
SELECT MIN(sal) AS minimum_salary
FROM employee;
```
# Query 5:- Display the average salary from employee table.
```sql
SELECT AVG(sal) AS average_salary
FROM employee;
```
# Query 6:- Display the maximum salary being paid to clerk.
```sql
SELECT MAX(sal) AS max_clerk_salary
FROM employee
WHERE job = 'CLERK';
```
# Query 7:- Display the maximum salary being paid in dept no 20.
```sql
SELECT MAX(sal) AS max_salary_dept20
FROM employee
WHERE deptno = 20;
```
# Query 8:- Display the minimum salary paid to any salesman.
```sql
SELECT MIN(sal) AS min_salesman_salary
FROM employee
WHERE job = 'SALESMAN';
```
# Query 9:- Display the average salary drawn by managers.
```sql
SELECT AVG(sal) AS avg_manager_salary
FROM employee
WHERE job = 'MANAGER';
```
# Query 10:- Display the total salary drawn by analysts working in dept no 40.
```sql
SELECT SUM(sal) AS total_analyst_salary
FROM employee
WHERE job = 'ANALYST'
AND deptno = 40;
```
# Query 11:- Display the names of employees in uppercase.
```sql
SELECT UPPER(ename) AS uppercase_name
FROM employee;
```
# Query 12:- Display the names of employees in lowercase.
```sql
SELECT LOWER(ename) AS lowercase_name
FROM employee;
```
# Query 13:- Display the names of employees in proper case.
```sql
SELECT CONCAT(UPPER(LEFT(ename,1)), LOWER(SUBSTRING(ename,2))) AS proper_case_name
FROM employee;
```
# Query 14:- Display the length of your name using appropriate function.
```sql
SELECT LENGTH('ASHISH') AS name_length;
```
# Query 15:- Display the length of all employee names.
```sql
SELECT ename, LENGTH(ename) AS name_length
FROM employee;
```