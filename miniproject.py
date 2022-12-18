from email import message
import time
from plyer import notification
if __name__=="__main__":
    while True:
        notification.notify(
        title="please drink water",
        message ="stabilize your heartbeat.",app_icon="C:\python,py\icon.ico",
        timeout=5
        )
        time.sleep(30)