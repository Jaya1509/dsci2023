# dsci2023
Complete User Manual: https://www.canva.com/design/DAFmDli4nHY/Rwan4qkL5C2HvekXVZ7_tQ/edit?utm_content=DAFmDli4nHY&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

always remove tensorflow-intel from requirements.txt before pushing code

python-3.9.13 is important

Kinda mind-blowing how this simple task is so complicated in Python. Here is what I think is the best way to do it automatically.

To Intialize this app on your local(One time).
1) Clone repository on local
2) Install conda on your machine
3) conda create --name dscienv (This is to create a python environment)
4) conda activate dscienv (To activate the environment)
5) pip3 install -r requirements.txt (TO INSTALL DEPENDENCIES)
6) uvicorn main:app --reload (To run the application on local)

IMP : always add libraries/dependencies with version in requirements.in after doing pip install and
then
pip-compile 


 To run app later everytime:
 1)conda activate dscienv
 2)uvicorn main:app --reload


To remove all pycache : 
find . -type d -name  "__pycache__" -exec rm -r {} +

