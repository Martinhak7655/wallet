import psycopg2
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

user_balance = [0]

connection = psycopg2.connect(
    host="localhost",
    database="wallet",
    user="postgres",
    password="MH2012"
)
cursor = connection.cursor()

create_table = '''
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL,
        mail VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL,
        balance VARCHAR(100) NOT NULL,
        create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
'''
cursor.execute(create_table)
connection.commit()

def quests(quest1=None, quest2=None):
    if quest1 == "Grancvel":
        return True
    elif quest2 == "Mutq gorcel":
        return True
    else:
        return

random_num = random.randint(1000, 9999)
def signin(username, mail, password, verify):
    if username == "" and mail == "" and len(password) <= 8:
        return False
    msg = MIMEMultipart()
    msg["From"] = "martinhakobyan2024@mail.ru"
    msg["To"] = mail
    msg["Subject"] = "Hastateq dzer account i verifikacumy"
    msg.attach(MIMEText(f"Dzer Verifikacman kody` {random_num}", 'plain'))
    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
    server.login("martinhakobyan2024@mail.ru", "qtuHVFSGgXNRyg1676Ja")
    server.sendmail("martinhakobyan2024@mail.ru", mail, msg.as_string())
    if verify == random_num:
        insert = '''
            INSERT INTO users (username, mail, password, balance) VALUES (%s, %s, %s, %s)
        '''
        cursor.execute(insert, (username, mail, password, user_balance[0],))
        connection.commit()
        return True

def signup(username, password):
    if username == "" and len(password) <= 8:
        return False
    select = '''
        SELECT * FROM users WHERE username = (%s) AND password = (%s);
    '''
    cursor.execute(select, (username, password,))
    connection.commit()
    users = cursor.fetchone()
    print(f"Bari Galust Dzer ej {users[1]}")
    return True

def getbalance(id_input):
    select = '''
        SELECT * FROM users WHERE id = (%s);
    '''
    cursor.execute(select, (id_input,))
    connection.commit()
    users = cursor.fetchone()
    print(f"Dzer balancy {users[4]} dram")
    return True

def cashin(sum, id_input):
    update = '''
        UPDATE users SET balance = (%s) WHERE id = (%s);
    '''
    cursor.execute(update, (user_balance[0] + sum, id_input,))
    connection.commit()
    return True

def cashout(sum, id_input):
    update = '''
            UPDATE users SET balance = (%s) WHERE id = (%s);
        '''
    cursor.execute(update, (user_balance[0] - sum, id_input,))
    connection.commit()
    return True

def poxancum(sum, id_input):
    update = '''
            UPDATE users SET balance = (%s) WHERE id = (%s);
        '''
    cursor.execute(update, (user_balance[0] + sum, id_input,))
    connection.commit()

while True:
    quest = input("Grancvel te Mutq gorcel:  ")
    if quests(quest1=quest):
            username_input = input("Greq dzer anuny:  ")
            mail_input = input("Greq dzer Maily:  ")
            password_input = input("Greq dzer passwordy:  ")
            verify_input = int(input("Greq mailum uxarkvac kody:  "))
            if signin(username=username_input, mail=mail_input, password=password_input, verify=verify_input):
                print("-" * 25)
                print("Register Succes")
                print("Check Balance: B")
                print("Cashin command: +")
                print("Cashout command: -")
                print("Poxancum: P")
                print("Exit: E")
                print("-" * 25)
                while True:
                    command = input("Greq commandy")
                    if command == "B":
                        id_input1 = input("Greq dzer idn")
                        if getbalance(id_input=id_input1):
                            print("procces succesed")
                        else:
                            print("Sxale")
                    elif command == "+":
                        Sum = int(input("Greq te vorqan gumareq uzum poxancel der hasvin"))
                        id_input1 = input("Greq dzer idn")
                        if cashin(sum=Sum, id_input=id_input1):
                            print("succes proccesed")
                    elif command == "-":
                        Sum = int(input("Greq te vorqan gumareq uzum hanel der hasvic"))
                        id_input1 = input("Greq dzer idn")
                        if cashout(sum=Sum, id_input=id_input1):
                            print("succes proccesed")
                    elif command == "P":
                        Sum = int(input("Greq te vorqa eq uzum poxancel"))
                        id_input1 = input("Greq te umeq uzum poxancel")
                        if poxancum(sum=Sum, id_input=id_input1):
                            print("Porcces Succesed")
                    elif command == "E":
                        print("Exit succes")
                        break
            else:
                print("*" * 25)
                print("Gorcuxutyunnery datark en!!")
                print("*" * 25)
    elif quests(quest2=quest):
        username_input = input("Greq Dzer anuny")
        password_inputs = input("Greq dzer passwordy")
        if signup(username=username_input, password=password_inputs):
            print("-" * 25)
            print("Register Succes")
            print("Check Balance: B")
            print("Cashin command: +")
            print("Cashout command: -")
            print("Poxancum: P")
            print("Exit: E")
            print("-" * 25)
            while True:
                command = input("Greq commandy")
                if command == "B":
                    id_input1 = input("Greq dzer idn")
                    if getbalance(id_input=id_input1):
                        print("procces succesed")
                    else:
                        print("Sxale")
                elif command == "+":
                    Sum = int(input("Greq te vorqan gumareq uzum poxancel der hasvin"))
                    id_input1 = input("Greq dzer idn")
                    if cashin(sum=Sum, id_input=id_input1):
                        print("succes proccesed")
                elif command == "-":
                    Sum = int(input("Greq te vorqan gumareq uzum hanel der hasvic"))
                    id_input1 = input("Greq dzer idn")
                    if cashout(sum=Sum, id_input=id_input1):
                        print("succes proccesed")
                elif command == "P":
                    Sum = int(input("Greq te vorqa eq uzum poxancel"))
                    id_input1 = input("Greq te umeq uzum poxancel")
                    if poxancum(sum=Sum, id_input=id_input1):
                        print("Porcces Succesed")
                elif command == "E":
                    print("Exit succes")
                    break
        else:
            print("*" * 25)
            print("Gorcuxutyunnery datark en!!")
            print("*" * 25)