USE [test]
GO

/****** Object:  Table [dbo].[DimDate]    Script Date: 3/25/2016 9:50:08 AM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[DimDate](
    [DateKey] [int] NOT NULL,
    [YearWeekDOW] [INT] NOT NULL,
    [FullDate] [date] NOT NULL,
    [WeekdayOfMonth] [tinyint] NOT NULL,
    [EnglishDayOfWeek] [nvarchar](10) NOT NULL,
    [EnglishMonthName] [nvarchar](10) NOT NULL,
    [SpanishDayOfWeek] [nvarchar](10) NOT NULL,
    [SpanishMonthName] [nvarchar](10) NOT NULL,
    [FrenchDayOfWeek] [nvarchar](10) NOT NULL,
    [FrenchMonthName] [nvarchar](10) NOT NULL,
    [ItalianDayOfWeek] [nvarchar](10) NOT NULL,
    [ItalianMonthName] [nvarchar](10) NOT NULL,
 CONSTRAINT [PK_DimDate_DateKey] PRIMARY KEY CLUSTERED 
(
    [DateKey] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, FILLFACTOR = 100) ON [PRIMARY]
) ON [PRIMARY]

GO

CREATE NONCLUSTERED INDEX [IX_YearWeekDOW] ON [dbo].[DimDate]
(
    [YearWeekDOW] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
GO
