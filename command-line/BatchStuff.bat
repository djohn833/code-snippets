@ECHO OFF
SETLOCAL

REM See for modifiers: https://gist.github.com/zed/53402
SET ScriptPath=%~dp0
REM Strip the trailing backslash (see https://ss64.com/nt/syntax-substring.html)
SET ScriptPath=%ScriptPath:~0,-1%

REM Set SingleLineCommandResult to the result of a command
SET CommandString='...'
FOR /F "delims=" %%i IN (%CommandString%) DO SET SingleLineCommandResult=%%i
