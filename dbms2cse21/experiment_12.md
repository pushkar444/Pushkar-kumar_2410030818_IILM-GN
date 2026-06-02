## EXPERIMENT 12
# Aim:- To perform advanced SQL operations using subqueries, joins, and delete statements for data manipulation and analysis.
 
# Query1:-1. Display those employees whose salary is less than his manager but more than salary of any other managers.
```sql 
SELECT E.ENAME
FROM EMPLOYEE E
JOIN EMPLOYEE M ON E.MGR = M.EMPNO
WHERE E.SAL < M.SAL
AND E.SAL > ANY (SELECT SAL FROM EMPLOYEE WHERE JOB = 'MANAGER');
```
# Query2:-2. Find out the number of employees whose salary is greater than their manager salary?
```sql
SELECT COUNT(*) 
FROM EMPLOYEE E
JOIN EMPLOYEE M ON E.MGR = M.EMPNO
WHERE E.SAL > M.SAL;
```
# Query3:-3. Display those managers who are not working under president but they are working under any other manager?
```sql
SELECT E.ENAME
FROM EMPLOYEE E
JOIN EMPLOYEE M ON E.MGR = M.EMPNO
WHERE E.JOB = 'MANAGER'
AND M.JOB <> 'PRESIDENT';
```
# Query 4:-4. Delete those department where no employee working?
```sql
DELETE FROM DEPARTMENT
WHERE DEPTNO NOT IN (SELECT DISTINCT DEPTNO FROM EMPLOYEE);
```
# Query 5:-5. Delete those records from emp table whose deptno not available in dept table?
```sql
DELETE FROM EMPLOYEE
WHERE DEPTNO NOT IN (SELECT DEPTNO FROM DEPARTMENT);
```
# Query 6:-6. Display those earners whose salary is out of the grade available in sal grade table?
```sql
SELECT ENAME, SAL
FROM EMPLOYEE E
WHERE NOT EXISTS (
  SELECT *
  FROM SALGRADE S
  WHERE E.SAL BETWEEN S.LOSAL AND S.HISAL
);
```
# Query 7:- 7. Display employee name, sal, comm. And whose net pay is greater than any other in the company?
```sql
SELECT ENAME, SAL, COMM, (SAL + IFNULL(COMM,0)) AS NET_PAY
FROM EMPLOYEE
WHERE (SAL + IFNULL(COMM,0)) = (
  SELECT MAX(SAL + IFNULL(COMM,0)) FROM EMPLOYEE
);
```
# Query 8:-8. Display those employees who are working in sales or research?
```sql
SELECT E.ENAME
FROM EMPLOYEE E
JOIN DEPARTMENT D ON E.DEPTNO = D.DEPTNO
WHERE D.DNAME IN ('SALES','RESEARCH');
```
# Query 9:-9. Display the grade of jones?
```sql
SELECT S.GRADE
FROM EMPLOYEE E
JOIN SALGRADE S ON E.SAL BETWEEN S.LOSAL AND S.HISAL
WHERE E.ENAME = 'JONES';
```
# Query 10:-10. Display the department name the no of characters of which is equal to no of employees in any other department?
```sql
SELECT DNAME
FROM DEPARTMENT
WHERE LENGTH(DNAME) IN (
  SELECT COUNT(*) 
  FROM EMPLOYEE 
  GROUP BY DEPTNO
);
```