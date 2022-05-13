import smtplib
from email.message import EmailMessage
import imghdr
import re

SMTP_SERVER = "smtp.gmail.com" #SMTP 접속을 위한 서버, 계정 설정
SMTP_PORT = 465 #google의 SMTP server 포트 주소는 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9-]+.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")

message = EmailMessage()
message.set_content("코드라이언 수업중 입니다.")

message["Subject"] = "제목입니다.."
message["From"] = "gmlquddl67@gmail.com"
message["To"] = "gmlquddl67@gmail.com"

with open("codelion.png","rb") as image:
    image_file = image.read()

image_type = imghdr.what('codelion',image_file)
message.add_attachment(image_file,maintype='image',subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("gmlquddl67@gmail.com","##########")

sendEmail("gmlquddl67@gmail.com")

smtp.quit()