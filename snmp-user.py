import smtplib

server = smtplib.SMTP('replace_server')
server.set_debuglevel(1)

with open('wordlist.goes.here', 'r') as file:
    for line in file:
        username = line.strip()
        try:
            response = server.verify(username)
            if response[0] == 250:
                print(f"Valid user found: {username}")
        except Exception as e:
            print(f"Error checking {username}: {e}")

server.quit()

