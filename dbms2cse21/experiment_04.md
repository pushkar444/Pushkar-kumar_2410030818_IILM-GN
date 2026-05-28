## Experiment 4 – Conditional Queries & Salary Calculations
# Aim:- To perform conditional filtering, salary calculations, updates, and pattern-based queries on the employee table.

# Query 1:- Display employees who joined before 30th June 1980 or after 31st Dec 1981.
```sql
SELECT ename, hiredate
FROM employee
WHERE hiredate < '1980-06-30'
OR hiredate > '1981-12-31';
```
# Query 2:- Display the names of employees whose second alphabet is 'A'.
```sql
SELECT ename
FROM employee
WHERE ename LIKE '_A%';
```
# Query 3:- Display the names of employees whose name is exactly five characters long.
```sql
SELECT ename
FROM employee
WHERE LENGTH(ename) = 5;
```
# Query 4:- Display the names of employees whose second alphabet is 'A' (Using SUBSTRING).
```sql
SELECT ename
FROM employee
WHERE SUBSTRING(ename, 2, 1) = 'A';
```
# Query 5:- Display the names of employees who are not working as salesman, clerk or analyst.
```sql
SELECT ename
FROM employee
WHERE job NOT IN ('SALESMAN', 'CLERK', 'ANALYST');
```
# Query 6:- Display employee name along with annual salary (sal * 12). Highest salary should appear first.
```sql
SELECT ename, sal * 12 AS annual_salary
FROM employee
ORDER BY annual_salary DESC;
```
# Query 7:- Display name, sal, hra, da, pf and total salary for each employee.
```sql
HRA = 15% of sal
DA = 10% of sal
PF = 5% of sal
Total Salary = (sal + hra + da) - pf
SELECT ename,
       sal,
       sal * 0.15 AS hra,
       sal * 0.10 AS da,
       sal * 0.05 AS pf,
       (sal + (sal * 0.15) + (sal * 0.10)) - (sal * 0.05) AS total_salary
FROM employee;
```
# Query 8:- Update salary by 10% increment for employees not eligible for commission.
```sql
UPDATE employee
SET sal = sal + (sal * 0.10)
WHERE comm IS NULL;
```
# Query 9:- Display employees whose salary is more than 3000 after giving 20% increment.
```sql
SELECT ename, sal * 1.20 AS increased_salary
FROM employee
WHERE sal * 1.20 > 3000;
```
# Query 10:- Display employees whose salary contains at least 3 digits.
```sql
SELECT ename, sal
FROM employee
WHERE sal >= 100;
```