import time
from datetime import datetime as dt

hosts_temp = "hosts"
host_path = r"C:/users/wizzy/desktop/python projects/project 3"
redirect_ip = "127.0.0.1"
websites = ["facebook.com", "www.facebook.com", "www.gmail.com", "gmail.com", "mail.google.com"]
year = dt.now().year
month = dt.now().month
day = dt.now().day

while True:
    if dt(year, month, day, 8) < dt.now() < dt(year, month, day, 16):
        print("Working Hours... Work! No facebook!")
        with open(hosts_temp, "r+") as file:
            content = file.read()
            for website in websites:
                if website not in content:
                    file.write("\n" + redirect_ip+ " " + website)
    else:
        with open(hosts_temp, 'r+') as file:
            content = file.readlines()

            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
                    
        print("Now you can facebook!")
    time.sleep(5)
