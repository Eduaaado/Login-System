import gspread
import regex as re
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Accounts').sheet1

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def submit(self):
    email = self.lineEmail.text().strip()
    user = self.lineUser.text().strip()
    passwd = self.linePasswd.text().strip()

    infos = [email, user, passwd]

    if '' not in infos:
        if re.search(regex, email):
            i = 1
            while sheet.row_values(i):
                if email == sheet.row_values(i)[0]:
                    error(self, 'This email is already registered')
                    return
                i+=1
            else:
                error(self, '')
                sheet.update_cell(i, 1, email)
                sheet.update_cell(i, 2, user)
                sheet.update_cell(i, 3, passwd)
        else:
            error(self, 'Invalid email')
    else:
        error(self, 'Something is wrong. Check your infos.')

def login(self):
    email = self.lineEmail.text().strip()
    passwd = self.linePasswd.text().strip()

    infos = [email, passwd]

    if '' not in infos:
        if re.search(regex, email):
            if email in sheet.col_values(1):
                ind = sheet.col_values(1).index(email)+1
                if passwd == sheet.row_values(ind)[2]:
                    error(self, 'Access granted')
                else:
                    error(self, 'Wrong password')
            else:
                error(self, 'This email is not registered')          
        else:
            error(self, 'This email is not valid')      

def error(self, message):
    self.lbError.setText(message)


if __name__ == '__main__':
    data = sheet.get_all_records()

    row = sheet.row_values(1)
    col = sheet.col_values(1)
    if 'Email' in col:
        col = col.index('Email')

    print(col)
