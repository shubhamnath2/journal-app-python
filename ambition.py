import datetime as dt
import re

class ambition():

    def __init__(self,username,password,file_name):
        self.username = username
        self.password = password
        self.file_name = file_name

    def read_journal(self):
        ###SHOW JOURNAL OF THE USERNAME
        journal_file = username + '_journal.txt'

        try:
            print("*********************************************************************")
            for line in reversed(list(open(journal_file))): ###STUDY ONCE
                print(line.rstrip())
        except FileNotFoundError:
            print("You need to write your first journal!!!")
        else:
            pass
        print("*********************************************************************")

    def create_journal(self):
        ###CREATE JOURNAL OF THE USERNAME
        journal_file=username+'_journal.txt'
        f=open(journal_file, "a")

        journal_msg=input("Write the content of the journal:")
        timestamp=dt.datetime.now()
        formatted_timestamp=timestamp.strftime("%d %b %Y %I:%M%p - ")

        line_no=0
        with open(journal_file,'r') as f:
            for line in f:
                line_no=line_no + 1

        if line_no<=49:
            f=open(journal_file,'a')
            f.write(formatted_timestamp+journal_msg+'\n')
            f.close()
        else:#QUEUE
            with open(journal_file,'r') as fin:
                lines=fin.readlines()
            with open(journal_file, 'w') as fout:
                fout.writelines(lines[1:]) ###STUDY
                fout.write(formatted_timestamp + journal_msg + '\n')

        amb.read_journal()

    def journal_option(self,username):
        ###JOURNAL MENU
        print("\n******** MY JOURNAL ********")
        print("Logging In: Welcome %s\n"%username)

        enter_or_show_journal="Please enter the option:\nShow Journal: 1\nWrite Journal: 2\nEnter: "
        option = int(input(enter_or_show_journal))

        if option==1:
            amb.read_journal()
        elif option==2:
            amb.create_journal()
        else:
            return


    def check_duplicate_username(self,file_name,username):
        ###CHECK NO 2 SAME USERNAME
        with open(file_name,'r') as f:
            line = f.readline()
            while line:
                existing_username=line.split(",", 1)[0]
                if username==existing_username:
                    return -1
                line = f.readline()
        f.close()

    def login_user(self):
        ###USER LOGIN
        flag=0

        #CHECK IF USERNAME EXIST OR NOT
        try:
            with open(file_name, 'r') as f:
                first = f.read(1)
                if not first:
                    print("Empty, You must sign up")
                    return
            f.close()
        except FileNotFoundError:
            print("Username file doesn't exist, you need to create one")
            return
        else:
            pass

        #AUTHENTICATION
        with open(file_name, 'r') as f:
            line = f.readline()
            while line:
                existing_username = line.split(",", 1)[0]
                existing_password = line.split(",", 1)[1].strip()  ##TAKING enter button as char

                if username == existing_username and password == existing_password:
                    flag=1
                    break
                line = f.readline()

        if flag==0:
            print("Username/Password does not match/exist")
            return
        amb.journal_option()

    def create_user(self):
        ###CREATE USER
        #STRING WHITESPACE REMOVAL perform with regular expression(studythis)
        for string in username:
            if string == ' ' or string=='' or string==',':
                return

        for string in password:
            if string == ' ' or string=='' or string==',':
                return

        #Check if user details is empty/full or not
        line_no=0
        f=open(file_name,'a')
        with open(file_name,'r') as f:
            first = f.read(1)
            if not first:
                print("Empty, will write first data")
            else:
                for line in f:
                    line_no = line_no + 1
                    if line_no >= 10:
                        print("Users has reached maximum level.")
                        return
        f.close()

        #Check username duplicacy
        flag=amb.check_duplicate_username(file_name,username)
        if flag==-1:
            print("Duplicacy of record will be created.")
            return

        #Write the details and logging to journal
        f = open(file_name, "a")
        f.write("%s,%s\n" % (username, password))
        f.close()
        print("User created,now logging to journal")
        self.login_user()

#### APPLICATION BEGINS ####

msg="Login: 1\nSign Up: 2\n"
print(msg)
try:
    option=int(input("Enter the Option:"))
except ValueError:
    print("Value Error")
    exit()
else:
    pass

username=input("Username: ")
password=input("Password: ")
file_name="users_list.txt"

amb=ambition(username,password,file_name)

if option==1:
    amb.login_user()
elif option==2:
    amb.create_user()
else:
    print("Exiting the Application")
    exit()