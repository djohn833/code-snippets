DECLARE @Dates AS TABLE (
	DateKey INT PRIMARY KEY,
	YearWeekDOW INT NOT NULL,
	FullDate DATE NOT NULL,
	WeekdayOfMonth TINYINT NOT NULL
);

INSERT INTO @Dates (DateKey, YearWeekDOW, FullDate, WeekdayOfMonth)
SELECT
	 10000*YEAR(DateValue) + 100*MONTH(DateValue) + DAY(DateValue)
	,1000*YEAR(DateValue) + 10*DATEPART(WEEK, DateValue) + DATEPART(WEEKDAY, DateValue)
	,DateValue
	,ROW_NUMBER() OVER (PARTITION BY YEAR(DateValue), MONTH(DateValue), DATEPART(weekday, DateValue) ORDER BY DAY(DateValue))
FROM Numbers n
CROSS APPLY (SELECT DATEADD(day, Number, '2015-01-01')) AS Date(DateValue)
WHERE DateValue BETWEEN '2015-01-01' AND '2016-12-31';

SELECT *
FROM @Dates;


DECLARE @EnglishNames AS TABLE (
	DateKey INT PRIMARY KEY,
	[MonthName] nvarchar(10) NOT NULL,
	[DayOfWeek] nvarchar(10) NOT NULL
);

DECLARE @SpanishNames AS TABLE (
	DateKey INT PRIMARY KEY,
	[MonthName] nvarchar(10) NOT NULL,
	[DayOfWeek] nvarchar(10) NOT NULL
);

DECLARE @FrenchNames AS TABLE (
	DateKey INT PRIMARY KEY,
	[MonthName] nvarchar(10) NOT NULL,
	[DayOfWeek] nvarchar(10) NOT NULL
);

DECLARE @ItalianNames AS TABLE (
	DateKey INT PRIMARY KEY,
	[MonthName] nvarchar(10) NOT NULL,
	[DayOfWeek] nvarchar(10) NOT NULL
);


SET LANGUAGE us_english;

INSERT INTO @EnglishNames (DateKey, [MonthName], [DayOfWeek])
SELECT
	 DateKey
	,DATENAME(month, FullDate)
	,DATENAME(weekday, FullDate)
FROM @Dates;

SET LANGUAGE spanish;

INSERT INTO @SpanishNames (DateKey, [MonthName], [DayOfWeek])
SELECT
	 DateKey
	,DATENAME(month, FullDate)
	,DATENAME(weekday, FullDate)
FROM @Dates;

SET LANGUAGE french;

INSERT INTO @FrenchNames (DateKey, [MonthName], [DayOfWeek])
SELECT
	 DateKey
	,DATENAME(month, FullDate)
	,DATENAME(weekday, FullDate)
FROM @Dates;

SET LANGUAGE italian;

INSERT INTO @ItalianNames (DateKey, [MonthName], [DayOfWeek])
SELECT
	 DateKey
	,DATENAME(month, FullDate)
	,DATENAME(weekday, FullDate)
FROM @Dates;

SET LANGUAGE us_english;


BEGIN TRAN

INSERT INTO [dbo].[DimDate]
    ([DateKey]
	,[YearWeekDOW]
    ,[FullDate]
	,[WeekdayOfMonth]
	,[EnglishMonthName]
    ,[SpanishMonthName]
    ,[FrenchMonthName]
    ,[ItalianMonthName]
    ,[EnglishDayOfWeek]
	,[SpanishDayOfWeek]
	,[FrenchDayOfWeek]
	,[ItalianDayOfWeek])
SELECT
	 d.DateKey
	,d.[YearWeekDOW]
	,d.FullDate
	,d.WeekdayOfMonth
	,en.[MonthName]
	,sp.[MonthName]
	,fr.[MonthName]
	,it.[MonthName]
	,en.[DayOfWeek]
	,sp.[DayOfWeek]
	,fr.[DayOfWeek]
	,it.[DayOfWeek]
FROM @Dates d
JOIN @EnglishNames en ON d.DateKey=en.DateKey
JOIN @SpanishNames sp ON d.DateKey=sp.DateKey
JOIN @FrenchNames  fr ON d.DateKey=fr.DateKey
JOIN @ItalianNames it ON d.DateKey=it.DateKey;

SELECT *
FROM dbo.DimDate dd
WHERE dd.DateKey BETWEEN 20150101 AND 20151231;

COMMIT