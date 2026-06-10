@echo off
cd /d C:\Users\owner\rasa_env
call Scripts\activate.bat
cd my_project_rasa
echo ????? ???? Rasa...
rasa run --enable-api --cors "*"
pause
