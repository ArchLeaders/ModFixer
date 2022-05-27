@ECHO OFF
SETLOCAL ENABLEDELAYEDEXPANSION

:: First selection | Set version bump mode
CLS
ECHO 1. Major
ECHO 2. Minor
ECHO 3. Hotfix
ECHO 4. Current
ECHO.

CHOICE /C 1234 /N /M "Select an option: "

SET vbump=SKIP

IF ERRORLEVEL 4 GOTO PROMPT
IF ERRORLEVEL 3 GOTO HOTFIX
IF ERRORLEVEL 2 GOTO MINOR
IF ERRORLEVEL 1 GOTO MAJOR

:MAJOR
ECHO Bumping version...
START "VBUMP" /WAIT /B "python.exe" "vbump.py" "0"
GOTO PROMPT

:MINOR
ECHO Bumping version...
START "VBUMP" /WAIT /B "python.exe" "vbump.py" "1"
GOTO PROMPT

:HOTFIX
ECHO Bumping version...
START "VBUMP" /WAIT /B "python.exe" "vbump.py" "2"
GOTO PROMPT

:PROMPT
FOR /F "tokens=*" %%x IN (.vscode\version) DO (
    SET ver=Version: %%x
)

FOR /F "tokens=*" %%x IN (.vscode\procfile) DO (
    SET repo=%%x
)

CLS
ECHO %ver%
ECHO Repo: %repo%
ECHO.

SET /P CONFIRM=Are you sure you wish to publish to %repo% (Y/N)? 
IF /I "%CONFIRM%" NEQ "Y" PAUSE & EXIT

ECHO.
ECHO Publishing, please wait...
ECHO.
ECHO Updating build...
START "PIP-UPGRADE-BUILD" /WAIT /B "pip.exe" "install" "-U" "build"

ECHO Updating twine...
START "PIP-UPGRADE-TWINE" /WAIT /B "pip.exe" "install" "-U" "twine"

ECHO Building...
START "BUILD-WHEEL" /WAIT /B "python.exe" "-m" "build"

ECHO Publishing...
START "UPLOAD-PYPI" /WAIT /B "python.exe" "-m" "twine" "upload" "--verbose" "--repository" "%repo%" "dist/*"

RMDIR /S /Q .\ModFixer.egg-info
RMDIR /S /Q .\dist

ECHO.
ECHO Operation completed.

PAUSE