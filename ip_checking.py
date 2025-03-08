import subprocess
import time
import smtplib
import csv
import matplotlib.pyplot as plt
import datetime

def ping_ip(ip):
  """Pings an IP address and returns True if it is up, 
    False if it is down."""
  try:
    subprocess.check_output(["ping", "-c", "1", ip])
    return True
  except subprocess.CalledProcessError:
    return False
  
exceptions = ["10.15.14.5"]
    
def log_ip(ip, status):
    """Logs the IP address and its status to a file."""
    with open("network_log_data.csv", "a", newline="") as f:
      writer = csv.writer(f)
      now = datetime.datetime.now()
      writer.writerow([now, ip, status])
      print(f" {ip}: {status}")
        
def send_email(subject, body):
    """Sends an email with the given subject and body."""
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("____u@gmail.com", "password")
    server.sendmail("gmail_id of sender", 
                  "gmail_id of receiver",
                  f"Subject: {subject} \n\n{body}")
    server.quit()
        
def plot_ping_graph(ips, ping_time):
    fig, ax = plt.subplots()
    ax.plot(ips, ping_time)
    ax.set_xlabel("IP Address")
    ax.set_ylabel("Ping Times (ms)")
    
def main():
  """The main function that pings IP addresses 
  and sends an email if any are down."""
  ip_addresses = [f"10.15.14.{i}" for i in range(1, 255)]

  while True:
    for ip in ip_addresses:
      status = ping_ip(ip)
      log_ip(ip, status)

    time.sleep(30)

if __name__ == "__main__":
    main()