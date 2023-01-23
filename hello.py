import webbrowser
import time
import win32com.client

shell = win32com.client.Dispatch("WScript.Shell")

url = "www.gmail.com"
email_to = "MarcoRuvoletto321@gmail.com"
subject = "Double Triple Bossy Deluxe"
msg = "I'll take a Double Triple Bossy Deluxe on a raft, 4x4 animal style, extra shingles with a shimmy and a squeeze, light axle grease; make it cry, burn it, and let it swim."
webbrowser.open(url)
time.sleep(13)
shell.SendKeys("c", 0)
time.sleep(1)
shell.SendKeys(email_to, 0)
time.sleep(1)
shell.SendKeys("{TAB}", 0)
time.sleep(1)
shell.SendKeys("{TAB}", 0)
time.sleep(1)
shell.SendKeys(subject, 0)
time.sleep(1)
shell.SendKeys("{TAB}", 0)
time.sleep(1)
shell.SendKeys(msg, 0)
time.sleep(1)
shell.SendKeys("{TAB}")
time.sleep(1)
shell.SendKeys("{ENTER}", 0)
