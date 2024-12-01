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
        balance INTEGER DEFAULT 0,
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
    print(f"{users[4]} dram")
    if users:
        return users[4]
    return True

def cashin(sum, id_input):
    update = '''
        UPDATE users SET balance = (%s) WHERE id = (%s);
    '''
    cursor.execute(update, (getbalance(id_input) + sum, id_input,))
    connection.commit()
    return True

def cashout(sum, id_input):
    if sum <= 100 or sum >= user_balance[0]:
        return False
    update = '''
            UPDATE users SET balance = (%s) WHERE id = (%s);
        '''
    cursor.execute(update, (getbalance(id_input) - sum, id_input,))
    connection.commit()
    return True

def poxancum(sum, id_input):
    update = '''
            UPDATE users SET balance = (%s) WHERE id = (%s);
        '''
    cursor.execute(update, (getbalance(id_input) + sum, id_input,))
    connection.commit()

def delete(mail, id, verify):
    if verify == "":
        return False
    msg = MIMEMultipart()
    msg["From"] = "martinhakobyan2024@mail.ru"
    msg["To"] = mail
    msg["Subject"] = "Hastateq dzer account i jnjman verifikacumy"
    msg.attach(MIMEText(f"Dzer Verifikacman kody` {random_num}", 'plain'))
    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
    server.login("martinhakobyan2024@mail.ru", "qtuHVFSGgXNRyg1676Ja")
    server.sendmail("martinhakobyan2024@mail.ru", mail, msg.as_string())
    if verify == random_num:
        delete = '''
            DELETE FROM users WHERE id = (%s);
        '''
        cursor.execute(delete, (id,))
        connection.commit()
        return True

def quests2(quest3=None, quest4=None, quest5=None):
    if quest3 == "Anun":
        return True
    elif quest4 == "Mail":
        return True
    elif quest5 == "Password":
        return True
    else:
        return False

def anvanpopoxum(anun, id):
    if anun == "" or id == "":
        return False
    update = '''
        UPDATE users SET username = (%s) WHERE id = (%s);
    '''
    cursor.execute(update, (anun, id,))
    connection.commit()
    return True

def mailpopoxum(mail, id):
    if mail == "" or id == "":
        return False
    update = '''
        UPDATE users SET mail = (%s) WHERE id = (%s);
    '''
    cursor.execute(update, (mail, id,))
    connection.commit()
    return True

def passwordpopoxum(password, id):
    if password == "" or id == "":
        return False
    update = '''
        UPDATE users SET password = (%s) WHERE id = (%s);
    '''
    cursor.execute(update, (password, id,))
    connection.commit()
    return True

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
                print("Popoxum: R")
                print("Delete account: D")
                print("Exit: E")
                print("-" * 25)
                while True:
                    command = input("Greq commandy")
                    if command == "B":
                        id_input1 = input("Greq dzer idn")
                        if getbalance(id_input=id_input1):
                            print(f"procces succesed ")
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
                    elif command == "D":
                        Mail = input("Greq dzer maily:  ")
                        id_input1 = input("Greq dzer idn:  ")
                        verify_input = int(input("Verifikacman kody:  "))
                        if delete(mail=Mail, id=id_input1, verify=verify_input):
                            print("Succes Procces")
                    elif command == "R":
                        harc = input("Uzumeq popoxel anun, mail, te password")
                        if quests2(quest3=harc):
                            anun_input = input("Greq popoxman entaka anuny")
                            id_input1 = input("Greq idn")
                            if anvanpopoxum(anun=anun_input, id=id_input1):
                                print("Succes Procces")
                        elif quests2(quest4=harc):
                            mail_input = input("Greq popoxman entaka anuny")
                            id_input1 = input("Greq idn")
                            if mailpopoxum(mail=mail_input, id=id_input1):
                                print("Succes Procces")
                        elif quests2(quest5=harc):
                            password_input = input("Greq popoxman entaka anuny")
                            id_input1 = input("Greq idn")
                            if passwordpopoxum(password=password_input, id=id_input1):
                                print("Succes Procces")
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
            print("Popoxum: R")
            print("Delete account: D")
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
                elif command == "D":
                    Mail = input("Greq dzer maily:  ")
                    id_input1 = input("Greq dzer idn:  ")
                    verify_input = int(input("Verifikacman kody:  "))
                    if delete(mail=Mail, id=id_input1, verify=verify_input):
                        print("Succes Procces")
                elif command == "R":
                    harc = input("Uzumeq popoxel anun, mail, te password")
                    if quests2(quest3=harc):
                        user_input = input("Greq popoxman entaka anuny")
                        id_input2 = input("Greq idn")
                        if anvanpopoxum(anun=user_input, id=id_input2):
                            print("Succes Procces")
                    elif quests2(quest4=harc):
                        mail_input = input("Greq popoxman entaka anuny")
                        id_input1 = input("Greq idn")
                        if mailpopoxum(mail=mail_input, id=id_input1):
                            print("Succes Procces")
                    elif quests2(quest5=harc):
                        password_input = input("Greq popoxman entaka anuny")
                        id_input1 = input("Greq idn")
                        if passwordpopoxum(password=password_input, id=id_input1):
                            print("Succes Procces")
        else:
            print("*" * 25)
            print("Gorcuxutyunnery datark en!!")
            print("*" * 25)