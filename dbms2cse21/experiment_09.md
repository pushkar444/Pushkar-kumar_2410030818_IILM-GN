## Experiment 9 – Subqueries & Nested Queries
# Aim:- To perform SQL queries using subqueries, nested queries, and conditional filtering on the employee and department tables using MariaDB.

# Query1️:- Display the name of employee who earns highest salary.
```sql
SELECT ename
FROM employee
WHERE sal = (SELECT MAX(sal) FROM employee);
```
# Query2️:- Display employee number and name of clerk earning highest salary among clerks.
```sql
SELECT empno, ename
FROM employee
WHERE job = 'CLERK'
AND sal = (SELECT MAX(sal) FROM employee WHERE job = 'CLERK');
```
# Query3️:- Display names of salesman earning more than highest salary of any clerk.
```sql
SELECT ename
FROM employee
WHERE job = 'SALESMAN'
AND sal > (SELECT MAX(sal) FROM employee WHERE job = 'CLERK');
```
# Query4️:- Display names of clerks earning more than JAMES and less than SCOTT.
```sql
SELECT ename
FROM employee
WHERE job = 'CLERK'
AND sal > (SELECT sal FROM employee WHERE ename = 'JAMES')
AND sal < (SELECT sal FROM employee WHERE ename = 'SCOTT');
```
# Query5️:- Display names of employees earning more than JAMES or more than SCOTT.
```sql
SELECT ename
FROM employee
WHERE sal > (SELECT sal FROM employee WHERE ename = 'JAMES')
OR sal > (SELECT sal FROM employee WHERE ename = 'SCOTT');
```
# Query6️:- Display names of employees earning highest salary in their respective departments.
```sql
SELECT ename
FROM employee e
WHERE sal = (
SELECT MAX(sal)
FROM employee
WHERE deptno = e.deptno);
```
# Query7️:- Display names of employees earning highest salary in their respective job groups.
```sql
SELECT ename, job
FROM employee e
WHERE sal = (
SELECT MAX(sal)
FROM employee
WHERE job = e.job);
```
# Query8️:- Display employee names working in ACCOUNTING department.
```sql
SELECT ename
FROM employee
WHERE deptno = (
SELECT deptno
FROM department
WHERE dname = 'ACCOUNTING');
```
# Query9️:- Display employee names working in MUMBAI.
```sql
SELECT ename
FROM employee
WHERE deptno = (
SELECT deptno
FROM department
WHERE location = 'MUMBAI');
```
# Query10:- Display job groups having total salary greater than maximum salary of managers.
```sql
SELECT job
FROM employee
GROUP BY job
HAVING SUM(sal) > (
SELECT MAX(sal)
FROM employee
WHERE job = 'MANAGER');
```