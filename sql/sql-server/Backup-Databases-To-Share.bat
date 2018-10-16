@echo off

mkdir \\%1\c$\Share

icacls \\%1\c$\Share /grant Everyone:(OI)(CI)F /T

REM Create "Share" if it doesn't exist
wmic /node:%1 /user:"username" /password:"password" share call create "", "", "", "Share", "", "C:\Share", 0

sqlcmd -S %1 -U sqlusername -P sqlpassword -i Backup-Databases-To-Share.sql

msg %username% "Finished backup of %1"
