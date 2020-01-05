# SQLScriptExec

Run Python in SSMS

 
EXECUTE sp_execute_external_script 
@language = N'Python',
@script=N'OutputDataSet = InputDataSet

for i in OutputDataSet["ename"]:
	print(i[0:4])

'
,@input_data_1 = N'SELECT [empno],[ename],sal,0 as Bonus from EMP'
WITH RESULT SETS ((EMPNO int, ENAME varchar(10), SAL float, Bonus float))
