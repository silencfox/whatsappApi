import pywhatkit as kit
import datetime
import time 
import pyautogui
from pynput.keyboard import Key, Controller
from pdf2image import convert_from_path

keyboard = Controller()

#python -m pip install pywhatkit --user
#python.exe -m pip install --upgrade pip --user
#python -m pip install pynput --user
#python -m pip install pywin32 --user
#python -m pip install pdf2image --user

#kit.sendwhatmsg_instantly(
#    phone_no="+13474608231", 
#    message="Howdy! This message will be sent instantly!",
#)



# Store Pdf with convert_from_path function
#images = convert_from_path('example.pdf')
# 
#for i in range(len(images)):
#   
#      # Save pages as images in the pdf
#    images[i].save('page'+ str(i) +'.jpg', 'JPEG')

fecha= print(datetime.date.today())


##  Send MSG Whatsapp
def send_whatsapp_message(msg: str):
    try:
        #kit.sendwhatmsg_instantly(
        #    phone_no="+13474608231", 
        #    message=msg,
        #    tab_close=True
        #)
        image="D:\proyectos\Python\whatapp\coop.jpg"
        phone="+18490000000"
        kit.sendwhats_image(phone, image, msg)

        time.sleep(10)
        pyautogui.click()
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    print(fecha)
    send_whatsapp_message(msg="Test message from a Python script! ")
    #kit.start_server()