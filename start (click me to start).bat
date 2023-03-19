@echo off
echo Starting Prasvulsian Translator...
pause
rem Install required packages
python -m pip install flask
python -m pip install openai

rem Set the console background color to blue and the text color to white
color 1F

rem Print text with style
echo ^|____________________________________^|
echo ^| Prasvulsian Translator has loaded! ^|
echo ^| In your browser type               ^|
echo ^| http://localhost:5000/?            ^|
echo ^|____________________________________^|
rem Start the Flask application in a new command prompt window
call python py\app.py

rem Wait for the application to start
timeout /t 5 /nobreak > NUL

pause
