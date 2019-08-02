import datetime as dt
import re
import os
import getpass

class Ambition():

    def __init__(self,username,password,file_name):
        self.username = username
        self.password = password
        self.file_name = file_name



    def read_journal(self,journal_file):
        ###SHOW JOURNAL OF THE USERNAME

        #CHECK IF FILE JOURNAL FILE EXIST OR NOT
        path_name = os.getcwd() + '/' + journal_file
        if os.path.exists(path_name) == False:
            print("You need to write your first journal!!!\nRedirecting to Journal Writing!!!\n")
            amb.create_journal(journal_file)
            return

        #RETRIEVE JOURNAL
        print("*"*70)
        os.chmod(path_name, 0o0777)
        for line in reversed(list(open(journal_file))):
            print(line.rstrip())
        os.chmod(path_name, ~0o0777)
        print("*"*70)



    def create_journal(self,journal_file):
        ###CREATE JOURNAL OF THE USERNAME

        # CREATE IF FILE JOURNAL FILE DOESN'T EXIST
        path_name = os.getcwd() + '/' + journal_file
        if os.path.exists(path_name) == False:
            f = open(journal_file, "a")

        os.chmod(path_name, 0o0777)
        f=open(journal_file, "a")

        #WRITING JOURNAL CONTENT
        journal_msg=input("Write the content of the journal:\n")
        timestamp=dt.datetime.now()
        formatted_timestamp=timestamp.strftime("%d %b %Y %I:%M%p - ")

        #WRITING IN THE JOURNAL, ONCE JOURNAL BUFFER FILLS, OLD ONES ARE REPLACED (QUEUE)
        line_no=0
        with open(journal_file,'r') as f:
            for line in f:
                line_no=line_no + 1

        if line_no<=2:
            f=open(journal_file,'a')
            f.write(formatted_timestamp+journal_msg+'\n')
            f.close()
        else:
            with open(journal_file,'r') as fin:
                lines=fin.readlines()
            with open(journal_file, 'w') as fout:
                fout.writelines(lines[1:])
                fout.write(formatted_timestamp + journal_msg + '\n')

        os.chmod(path_name, ~0o0777)
        amb.read_journal(journal_file)



    def journal_option(self):
        ###JOURNAL MENU

        print("\n******** MY JOURNAL ********")
        print("Logging In: Welcome %s\n"%username)

        enter_or_show_journal="Please enter the option:\nShow Journal: 1\nWrite Journal: 2\nEnter: "
        option=0
        try:
            option = int(input(enter_or_show_journal))
        except ValueError:
            print("Value Error, Closing the Journal")
        else:
            pass

        journal_file = username + '_journal.txt'

        if option==1:
            amb.read_journal(journal_file)
        elif option==2:
            amb.create_journal(journal_file)
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

        #FILE EXIST OR NOT
        try:
            path_name = os.getcwd() + '/' + file_name
            os.chmod(path_name, 0o0777)
        except FileNotFoundError:
            print("Username file doesn't exist.\nCreate the file by choosing the option 1 i.e. Sign Up.\nNow closing the application")
            return
        else:
            pass

        #CHECK IF USERNAME EXIST OR NOT
        with open(file_name, 'r') as f:
            first = f.read(1)
            if not first:
                print("Empty, You must sign up")
                os.chmod(path_name, ~0o0777)
                return
        f.close()

        #USER AUTHENTICATION
        flag = 0
        with open(file_name, 'r') as f:
            line = f.readline()
            while line:
                existing_username = line.split(",", 1)[0]
                existing_password = line.split(",", 1)[1].rstrip()  ##TAKING enter button as char

                if username == existing_username and password == existing_password:
                    flag=1
                    break
                line = f.readline()

        if flag==0:
            print("Username/Password does not match/exist")
            os.chmod(path_name, ~0o0777)
            return

        os.chmod(path_name, ~0o0777)

        print("Authentication Complete, now Starting the journal")
        amb.journal_option()



    def create_user(self):
        ###CREATE USER

        #GET FILE LOCATION
        path_name=os.getcwd()+'/'+file_name
        if os.path.exists(path_name)==False:
            f = open(file_name, 'a')
        os.chmod(path_name, 0o0777)

        #CHECK IF USERNAME HAS SPECIAL CHARACTER OR NOT
        regex=re.compile('[@_!#$%^"\'&*()<>?/\|}{~:]')
        if(regex.search(username)!=None):
            print("No Special Characters")
            os.chmod(path_name, ~0o0777)
            return

        #ChHECK IF USERNAME BUFFER(FILE) IS EMPTY OR NOT
        line_no=0
        with open(file_name,'r') as f:
            first = f.read(1)
            if not first:
                print("Empty, will write first data")
            else:
                for line in f:
                    line_no = line_no + 1
                    if line_no >= 10:
                        print("Users has reached maximum level.")
                        os.chmod(path_name, ~0o0777)
                        return

        #CHECK USERNAME DUPLICACY
        flag=amb.check_duplicate_username(file_name,username)
        if flag==-1:
            print("Duplicacy of record will be created.")
            os.chmod(path_name, ~0o0777)
            return

        #SIGNING UP AND LOGGING
        with open(file_name,"a") as f:
            f.write("%s,%s\n" % (username, password))

        os.chmod(path_name, ~0o0777)
        print("User created, now redirecting to Login for complete authentication")
        self.login_user()



#### APPLICATION BEGINS ####
msg="Login: 1\nSign Up: 2\n"
option=0
print(msg)
try:
    option=int(input("Enter the Option:"))
except ValueError:
    print("Value Error, Closing the application")
    exit()
else:
    pass

username=input("Username: ")
password=getpass.getpass('Password: ')
file_name="users_list.txt"

if password == '':
    exit()
amb=Ambition(username,password,file_name)

if option ==1:
    amb.login_user()
elif option==2:
    amb.create_user()
else:
    print("Exiting the Application")
    exit()