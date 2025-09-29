@echo off
REM Script interactivo para actualizar el repositorio Los Contactos de Mamá

REM Ir al directorio del proyecto
cd "C:\Users\6QW61LA\PycharmProjects\pythonProject\web pages\los contactos de mama"

REM Agregar todos los cambios
"C:\Program Files\Git\cmd\git.exe" add .

REM Pedir mensaje de commit al usuario
set /p commit_msg=Escribe el mensaje del commit:

REM Verificar si el usuario ingresó un mensaje
if "%commit_msg%"=="" (
    set commit_msg=Auto commit %date% %time%
)

REM Hacer commit
"C:\Program Files\Git\cmd\git.exe" commit -m "%commit_msg%"

REM Subir cambios al repositorio remoto en GitHub
"C:\Program Files\Git\cmd\git.exe" push https://gilbertomorelos@github.com/gilbertomorelos/loscontactosdemama.git main

echo.
echo ¡Listo! Los cambios se subieron a GitHub.
pause

