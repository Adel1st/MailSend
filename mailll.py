import os
import smtplib
from dotenv import load_dotenv
load_dotenv()
LOGIN = os.getenv('LOGIN')
PASSVORD = os.getenv('PASSVORD')
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(LOGIN, PASSVORD)
message = """\
From: gropius.adel@yandex.ru
To: gropius.adel@yandex.ru
Subject: Важно!
Content-Type: text/plain; charset="UTF-8";
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""
message = message.replace('%friend_name%', 'Igor')
message = message.replace('%my_name%', 'Adel')
message = message.replace('%website%', 'https://dvmn.org/profession-ref-program/adelgropius/pN5Ae/')
message = message.encode("UTF-8")
email_from = "gropius.adel@yandex.ru"
email_to = "gropius.adel@yandex.ru"
print(message)
server.sendmail(email_from, email_to, message)
server.quit()