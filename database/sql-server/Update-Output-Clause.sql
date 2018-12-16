-- Based on http://www.sqlservercentral.com/articles/T-SQL/156604/

-- Setup schema
IF OBJECT_ID('Department_SRC', 'U') IS NOT NULL
	DROP TABLE dbo.Department_SRC;

CREATE TABLE [dbo].[Department_SRC] (
	[DepartmentID] [smallint] IDENTITY(1,1) NOT NULL,
	[Name] varchar(50) NOT NULL,
	[GroupName] varchar(50) NOT NULL,
	[ModifiedDate] [datetime] NOT NULL
) ON [PRIMARY]

Insert into [dbo].[Department_SRC] ([Name], [GroupName], [ModifiedDate]) Values ('Engineering', 'Research and Development', getdate());


--Update the GroupName for the Department.
Update [Department_SRC]
Set [GroupName] = 'IT',
	ModifiedDate = Getdate()
OUTPUT
	 deleted.Name,
	 deleted.GroupName    as    GroupName_old, 
	 deleted.ModifiedDate as ModifiedDate_old, 
	inserted.GroupName    as    GroupName_new,
	inserted.ModifiedDate as ModifiedDate_new
Where [Name]='Engineering'


--capturing Updated values using table variable.
DECLARE @Updated table (
	[DepartmentID] int,
    [Name] varchar(50),
    [GroupName_old] varchar(50),
    [GroupName_new] varchar(50),
    [ModifiedDate_old] datetime,
    [ModifiedDate_new] datetime
);

Update [Department_SRC]
Set [GroupName] = 'IT', 
    ModifiedDate = Getdate()
OUTPUT
	 deleted.DepartmentID,
	 deleted.Name,
	 deleted.GroupName    as    GroupName_old, 
	 deleted.ModifiedDate as ModifiedDate_old, 
	inserted.GroupName    as    GroupName_new,
	inserted.ModifiedDate as ModifiedDate_new
INTO @Updated
Where [Name] = 'Engineering'

--Querying from @Updated output table
Select * from @Updated


---Type 3 table example
IF OBJECT_ID('Department_Type3', 'U') IS NOT NULL
	DROP TABLE dbo.Department_Type3;

CREATE TABLE [dbo].[Department_Type3] (
    [DepartmentID] [smallint] IDENTITY(1,1) NOT NULL,
    [Name] varchar(50)  NULL,
    [GroupName_old] varchar(50)  NULL,
    [GroupName_current] varchar(50)  NULL,
    [EffectiveDate] [datetime]  NULL
) ON [PRIMARY]
GO

---Insert some test values
Insert into [dbo].[Department_Type3] ([Name], [GroupName_current], [EffectiveDate]) Values ('Engineering', 'Research and Development', getdate());

Select * from [dbo].[Department_Type3]


--capturing Updated values using table variable.
DECLARE @Updated table (
	[DepartmentID] int,
    [Name] varchar(50),
    [GroupName_old] varchar(50),
    [GroupName_current] varchar(50),
    [ModifiedDate_old] datetime,
    [ModifiedDate_new] datetime
);

Update [Department_Type3]
Set [GroupName_current] = 'IT',
    EffectiveDate = Getdate()
OUTPUT
	 deleted.DepartmentID,
	 deleted.Name,
	 deleted.GroupName    as    GroupName_old, 
	 deleted.ModifiedDate as ModifiedDate_old, 
	inserted.GroupName    as    GroupName_new,
	inserted.ModifiedDate as ModifiedDate_new
INTO @Updated
Where [Name] = 'Engineering'

--Update the GroupName_old with old values
Update a
Set a.GroupName_old = b.GroupName_old,
    a.EffectiveDate = b.ModifiedDate_new
from [Department_Type3] as a
inner join @Updated as b
on a.DepartmentID = b.DepartmentID

--Querying the final table
Select * from [Department_Type3]
