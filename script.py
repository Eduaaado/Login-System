import mysql.connector
import regex as re

db = mysql.connector.connect(
    host='localhost',
    port='3307',
    user="root",
    passwd="usbw",
    database="loginsystem",
    auth_plugin='mysql_native_password'
) 
mycursor = db.cursor()
mycursor.execute('CREATE DATABASE IF NOT EXISTS loginsystem')
mycursor.execute('CREATE TABLE IF NOT EXISTS users (email VARCHAR(255), username VARCHAR(255), passwd VARCHAR(255))')

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def submit(self):
    email = self.lineEmail.text().strip()
    user = self.lineUser.text().strip()
    passwd = self.linePasswd.text().strip()

    infos = [email, user, passwd]

    if '' not in infos:
        if re.search(regex, email):
            mycursor.execute('SELECT email FROM users')
            if (email,) not in mycursor.fetchall():
                error(self, 'You signed up', 1)
                sql = 'INSERT INTO users (email, username, passwd) VALUES(%s, %s, %s)'
                val = (email, user, passwd)
                mycursor.execute(sql, val)
                db.commit()
            else: 
                error(self, 'This email is already registered', 0)
                return
        else:
            error(self, 'Invalid email', 0)
    else:
        error(self, 'Something is wrong. Check your infos.', 0)

def login(self):
    email = self.lineEmail.text().strip()
    passwd = self.linePasswd.text().strip()

    infos = [email, passwd]

    if '' not in infos:
        if re.search(regex, email):
            mycursor.execute('SELECT email FROM users')
            if (email,) in mycursor.fetchall():
                mycursor.execute('SELECT passwd FROM users WHERE email = %s', (email,))
                if (passwd,) == mycursor.fetchone():
                    error(self, 'Access granted', 1)
                else: 
                    error(self, 'Access denied', 0)
            else:
                error(self, 'This email is not registered', 0)          
        else:
            error(self, 'This email is not valid', 0)      

def error(self, message, _type):
    lb = self.lbError
    color = ['red', 'green']
    lb.setStyleSheet('color: {}'.format(color[_type]))
    lb.setText(message)
