text = ('lord_of_pizzas ddfdsfsd DF Gds sklaje3o4 lmsfl;s fsfdsfDFGdfere dsdfsdfsd') #Текст письма

def send_email ( message, recipient , sender = "university.help@gmail.com") :

    if not ((recipient.endswith( ".com") or recipient.endswith( ".ru") or recipient.endswith( ".net") )and "@" in recipient):
       stroke = "Невозможно отправить письмо с адреса "+ str(sender) + " на адрес " + str(recipient)
    elif  sender == recipient :
        stroke = "Нельзя отправить письмо самому себе!"
    elif  sender == "university.help@gmail.com" :
        stroke = "Письмо успешно отправлено с адреса "+ str(sender) + " на адрес " + str(recipient) + "."
    else :
        stroke = "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса "+ str(sender) + " на адрес " + str(recipient) + "."
    return stroke

print("1 message")
print(send_email(text,"university.help@net.com"))
print("2 message")
print(send_email(text,"university.help@gmail.com"))
print("3 message")
print(send_email(text,"university.help@net.com","university.hp@net.com"))
print("4 message")
print(send_email(text,"university.help-net.com"))