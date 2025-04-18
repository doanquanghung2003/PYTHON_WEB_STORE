1.//Khoi tao moi truong:
pip install virtualenv          //Cai package moi truong ao - chi khoi chay khi chua cai dat
py -m venv name_env             //Ta folder name_env chua file moi truong (Doi ten di)
name_env\Scripts\activate.bat   //Active moi truong ao

2.//Cai dat package du an neu co (Su dung khi lam du an)
//Khi lam du an se co 1 file requirements.txt chua cac package can thiet cho du an, de cai dat:
py install -r requirements.txt 

3.//Them data vao database 
py .\manage.py makemigrations
py .\manage.py migrate


4.//Server
py .\manage.py runserver