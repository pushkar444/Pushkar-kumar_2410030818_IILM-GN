## Experiment 8 – Joins & Advanced Queries
# Aim:- To perform SQL queries using joins, self-joins, aggregate functions, and table modifications on the employee, department, and salgrade tables using MariaDB.

# Query1️:- Create the salgrade table.
```sql
CREATE TABLE salgrade (
grade CHAR(1),
losal INT,
hisal INT
);
```
# Query2️:- Insert values into salgrade.
```sql
INSERT INTO salgrade VALUES
('A', 700, 1200),
('B', 1201, 1400),
('C', 1401, 2000),
('D', 2001, 3000),
('E', 3001, 9999);
```
# Query3️:- Verify the salgrade table.
```sql
SELECT * FROM salgrade;
```
# Query4️:- Alter the department table to add location.
```sql
ALTER TABLE department
ADD location VARCHAR(20);
```
# Query5️:- Update department locations.
```sql
UPDATE department SET location = 'MUMBAI' WHERE deptno = 10;
UPDATE department SET location = 'CHENNAI' WHERE deptno = 20;
UPDATE department SET location = 'HYDERABAD' WHERE deptno = 30;
UPDATE department SET location = 'DELHI' WHERE deptno = 40;
```
# Query6️:- Display all employees with their department name.
```sql
SELECT e.ename, d.dname
FROM employee e
JOIN department d
ON e.deptno = d.deptno;
```
# Query7️:- Display employees whose manager name is 'JONES' along with their manager name.
```sql
SELECT e.ename AS employee, m.ename AS manager
FROM employee e
JOIN employee m
ON e.mgr = m.empno
WHERE m.ename = 'JONES';
```
# Query8️:- Display employee name, job, department name, manager name, and grade department-wise.
```sql
SELECT e.ename, e.job, d.dname,
m.ename AS manager,s.grade
FROM employee e
JOIN department d ON e.deptno = d.deptno
LEFT JOIN employee m ON e.mgr = m.empno
JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
ORDER BY d.dname;
```
# Query9️:- List employee name, job, salary grade, and department name for everyone except 'CLERK', sorted by highest salary.
```sql
SELECT e.ename, e.job, d.dname, s.grade, e.sal
FROM employee e
JOIN department d ON e.deptno = d.deptno
JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
WHERE e.job <> 'CLERK'
ORDER BY e.sal DESC;
```
# Query10:- Display employee name, job and manager (including employees without manager).
```sql
SELECT e.ename, e.job,
IFNULL(m.ename, 'NO MANAGER') AS manager
FROM employee e
LEFT JOIN employee m
ON e.mgr = m.empno;
```
# Query1️1️:- List employee details who earn 36000 annually or are not clerks.
```sql
SELECT e.ename, e.job, (e.sal * 12) AS annual_salary,e.deptno, d.dname, s.grade
FROM employee e
JOIN department d ON e.deptno = d.deptno
JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
WHERE (e.sal * 12 = 36000) OR e.job <> 'CLERK';
```
# Query1️2️:- List employee details who earn 30000 annually and are not clerks.
```sql
SELECT e.ename, e.job, (e.sal * 12) AS annual_salary,e.deptno, d.dname, s.grade
FROM employee e
JOIN department d ON e.deptno = d.deptno
JOIN salgrade s ON e.sal BETWEEN s.losal AND s.hisal
WHERE (e.sal * 12 = 30000) AND e.job <> 'CLERK';
```
# Query1️3️:- List employee and manager details including 'NO MANAGER'.
```sql
SELECT e.empno, e.ename,
IFNULL(m.empno, 'NO MANAGER') AS manager_no,
IFNULL(m.ename, 'NO MANAGER') AS manager_name
FROM employee e
LEFT JOIN employee m
ON e.mgr = m.empno;
```
# Query1️4️:- Display department name, department number, and total salary.
```sql
SELECT d.dname, d.deptno,
SUM(e.sal) AS total_salary
FROM department d
JOIN employee e ON d.deptno = e.deptno
GROUP BY d.deptno, d.dname;
```
# Query1️5️:- Display employee number, name and department location.
```sql
SELECT e.empno, e.ename, d.location
FROM employee e
JOIN department d ON e.deptno = d.deptno;
```
# Query1️6️:- Display employee name and department name.
```sql
SELECT e.ename, d.dname
FROM employee e
JOIN department d ON e.deptno = d.deptno;
```