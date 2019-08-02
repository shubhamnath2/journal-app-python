Personal Journal App

Created by Shubham Nath for AmbitionBox



Description:
This is an application created in python version 3.6 which records the journal of the user in a text file. This app will display latest 50 journal entries. Latest entry will be at the top of display, earlier entries will follow sequentially. Journal data that is saved in a file cannot be accessed by the user. The application will support multiple account creation, up to 10 accounts. Every user will have seperate data files in the application folder. For each user's journal entry, the time and date will be stamped.



Process:
This application is implemented in python 3.6 with PyCharm IDE. Python Virtual Environment is created for running the app with the environment folder 'venv'. 
Configure the terminal such that terminal runs in the 'venv' environment.



****ACTIVATING VIRTUAL ENVIRONMENT****
1) Install virtual environment

2) Create a folder(venv). Then create a Virtual Environment in it & install python(3.6) in the folder.
virtualenv -p /usr/bin/python3.6 /venv

3) Go to venv/bin/ and type 'source active', you will enter the new environment. To go out of the environment type deactivate. 



****STARTING THE APPLICATION****
1)Start the application in the terminal, typing the command 'python3.6 journal_app.py'.

2)It will ask for login(1) and sign up(2).

3)Then it will ask for username and password.

4)Choosing sign up(2) will first create 'users_list.txt' then create the user and password and store in the 'users_list.txt' as 'username,password' format. 

*Username will only accept alphabetical characters. After that, it will redirect to login for complete authentication. If already 10 accounts created, will stop the application by saying "Users has reached maximum level". Checks username duplicacy also. 

5)Choosing login(1) will check if the credentials matches. If 'users_list.txt' doesn't exist will ask for to create. If matches, then it will redirect to Journal menu. 

*Checks if username is there or not, If not then ask for sign up.

6)Journal Menu will ask for Show Jouranl(1) & Write Journal(2).

7)Show Journal(1) will show the journals of the user with timestamp value form latest on top to oldest at bottom. If journal file of the user doesn't there, it will redirect to Write Journal.

8)Write Journal(2) will write the input journal data with timestamp value upto 50. Latest 50 journals will display, discarding the older rest. And then it will redirect to Show Jouranal.
