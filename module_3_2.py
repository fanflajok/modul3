def send_mail(message, recipient, *,sender = "univercity.help@gmail.com"):
        if not recipient.endswith((".com", ".net", ".ru")) or not sender.endswith((".com", ".net", ".ru")) or "@" not in recipient or "@" not in sender:
            print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient)
        elif recipient == sender:
            print("Нельзя отправить письмо самому себе!")
        elif sender == "univercity.help@gmail.com":
            print("Письмо успешно отправлено с адреса ", sender, "на адрес", recipient)
        else:
            print("Нестандартный отправитель")
send_mail("Привет", "fanflajok@gmail.com", sender = "blabla@mail.ru")
