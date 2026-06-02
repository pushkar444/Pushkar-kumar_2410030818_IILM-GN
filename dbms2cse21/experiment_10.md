## Experiment 10 – Advanced Subqueries & Joins
# Aim:- To perform advanced SQL queries using subqueries, joins, comparison operators (ANY, ALL), and conditions on the employee, department, and salgrade tables using MariaDB.

# Query1️:- Display employees from dept 10 with salary greater than ANY employee in other departments.
```sql
SELECT ename
FROM employee
WHERE deptno = 10
AND sal > ANY (SELECT sal
FROM employee
WHERE deptno <> 10);
```
# Query2️:- Display employees from dept 10 with salary greater than ALL employees in other departments.
```sql
SELECT ename
FROM employee
WHERE deptno = 10
AND sal > ALL (SELECT sal
FROM employee
WHERE deptno <> 10);
```
# Query3️:- Display details of employees in SALES department with grade 'C'.
```sql
SELECT e.*
FROM employee e
JOIN department d ON e.deptno = d.deptno
JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
WHERE d.dname = 'SALES'
AND s.grade = 'C';
```
# Query4️:- Display employees who are not managers but are managers of others.
```sql
SELECT *
FROM employee
WHERE job <> 'MANAGER'
AND empno IN (SELECT mgr
FROM employee
WHERE mgr IS NOT NULL
);
```
# Query5️:- Display employees whose manager name is 'JONES'.
```sql
SELECT e.ename
FROM employee e
JOIN employee m ON e.mgr = m.empno
WHERE m.ename = 'JONES';
```
# Query6️:- Display employee names working in SALES department.
```sql
SELECT e.ename
FROM employee e
JOIN department d ON e.deptno = d.deptno
WHERE d.dname = 'SALES';
```
# Query7️:- Display employee name, dept name, salary and commission for salary between 2000 and 5000 and location is CHENNAI.
```sql
SELECT e.ename, d.dname, e.sal, e.comm
FROM employee e
JOIN department d ON e.deptno = d.deptno
WHERE e.sal BETWEEN 2000 AND 5000
AND d.location = 'CHENNAI';
```
# Query8️:- Display employees whose salary is greater than their manager's salary.
```sql
SELECT e.ename
FROM employee e
JOIN employee m ON e.mgr = m.empno
WHERE e.sal > m.sal;
```
# Query9️:- Display employees working in same department as their manager.
```sql
SELECT e.ename
FROM employee e
JOIN employee m ON e.mgr = m.empno
WHERE e.deptno = m.deptno;
```
# Query10:- Display grade and employee names for dept 10 or 30, grade not 'D', and hired before 31-Dec-1982.
```sql
SELECT e.ename, s.grade
FROM employee e
JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
WHERE e.deptno IN (10, 30)
AND s.grade <> 'D'
AND e.hiredate < '1982-12-31';
```