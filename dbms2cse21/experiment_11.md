## Experiment 11 – Advanced Queries & Data Manipulation
# Aim:- To perform advanced SQL operations including DELETE, subqueries, aggregate functions, and conditional filtering on the employee, department, and salgrade tables using MariaDB.

# Query1️:- Delete employees who joined before 31-Dec-1982 and whose department location is 'DELHI' or 'MUMBAI'.
```sql
DELETE FROM employee
WHERE hiredate < '1982-12-31'
AND deptno IN (
SELECT deptno FROM department
WHERE location IN ('DELHI', 'MUMBAI'));
```
# Query2️:- Display employee name, job, department name and location for managers.
```sql
SELECT e.ename, e.job, d.dname, d.location
FROM employee e
JOIN department d ON e.deptno = d.deptno
WHERE e.job = 'MANAGER';
```
# Query3️:- Display name and job of employee if his salary equals highest salary of his grade.
```sql
SELECT e.ename, e.job
FROM employee e
JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
AND e.sal = (SELECT MAX(e2.sal)
FROM employee e2
JOIN salgrade s2 ON e2.sal
WHERE s2.grade = s.grade);
```
# Query4️:- Find top 5 earners of the company.
```sql
SELECT ename, sal
FROM employee
ORDER BY sal DESC
LIMIT 5;
```
# Query5️:- Display employees who are getting highest salary.
```sql
SELECT ename
FROM employee
WHERE sal = (SELECT MAX(sal) FROM employee);
```
# Query6️:- Display employees whose salary equals average of max and min salary.
```sql
SELECT ename, sal
FROM employee
WHERE sal = (
(SELECT MAX(sal) FROM employee) +
(SELECT MIN(sal) FROM employee)) / 2;
```
# Query7️:- Display department names where at least 3 employees work.
```sql
SELECT d.dname
FROM department d
JOIN employee e ON d.deptno = e.deptno
GROUP BY d.dname
HAVING COUNT(*) >= 3;
```
# Query8️:- Display manager names whose salary is more than average salary of company.
```sql
SELECT ename
FROM employee
WHERE job = 'MANAGER'
AND sal > (SELECT AVG(sal) FROM employee);
```
# Query9️:- Display managers whose salary is more than average salary of their employees.
```sql
SELECT m.ename
FROM employee m
WHERE m.job = 'MANAGER'
AND m.sal > (SELECT AVG(e.sal)
FROM employee e
WHERE e.mgr = m.empno);
```
# Query10:- Display employee name, salary, commission and net pay where net pay ≥ any employee salary.
```sql
SELECT ename, sal, comm,
(sal + IFNULL(comm,0)) AS net_pay
FROM employee
WHERE (sal + IFNULL(comm,0)) >= ANY (
SELECT sal FROM employee);
```