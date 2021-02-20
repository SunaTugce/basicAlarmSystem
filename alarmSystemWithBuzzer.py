import RPi.GPIO as GPIO
import time
import smtplib

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)  # PIR
GPIO.setup(24, GPIO.OUT)  # Buzzer


def sendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("sender@gmail.com", "password")

    message = "There is somebody in your home!!"
    server.sendmail("sender@gmail.com", "receiver@gmail.com", message)
    server.quit()
    return


try:
    time.sleep(2)

    while True:
        if GPIO.input(23):
            GPIO.output(24, True)
            time.sleep(1)
            GPIO.output(24, False)
            print("Motion Detected!")
            sendMail()
            time.sleep(5)
        time.sleep(0.1)

except:
    GPIO.cleanup()


