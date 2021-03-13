# -*- coding: utf-8 -*-

import requests  # Для запросов и получения контента
import settings  # json и ссылка на сайт
from bs4 import BeautifulSoup  # модуль для парсинга
import json  # модуль для легкой работы с json файлами
import datetime  # модуль для работы с временем
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import settings
import random


def send_msg(message, ID, vk_session):
    vk_session.method("messages.send",
                      {"user_id": ID,
                       "message": message,
                       "random_id": 0})


def get_tags_a(n, s):
    """переменные"""
    HEADERS = {
        "Users-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0"
    }

    response = requests.get(settings.BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    global all_tags_main
    all_tags_a = []  # список всех ссылок подзадач
    all_tags_main = []  # список выбранных пользователем подзадач

    """получения всех ссылок"""
    tags_a = soup.find_all("div", class_="cat_children")  # все подзадачи задач
    tags_a = tags_a[n - 1]
    for i in tags_a.find_all("a", class_="cat_name", href=True):
        all_tags_a.append(i["href"])
    """конец получения всех ссылок"""

    """получение ссылки подзадач"""
    for i in range(len(s)):
        all_tags_main.append(all_tags_a[int(s[i]) - 1])
    return all_tags_main


"""конец получения ссылок подзадач"""


def get_quest(tags_a, count, working):
    global true_answer, false_answer, answer_quest

    def answer(soup, working):

        """номера всех задач на странице"""
        if working:
            global page_answer
            page_answer = []  # номера задач для получения ответа
            for i in soup.find_all("a", href=True):
                if i["href"][:9] == "/problem?":
                    page_answer.append(i["href"])

            return page_answer

    """конец и больше не используется"""

    def quest_write(soup, count):
        """заполнение задач существующих на странице"""
        global all_quest
        all_quest = []
        quest = soup.find_all("div", align="justify", class_="pbody")
        count_for = 0
        for j in quest:
            if count != count_for and len(j.find("p").get_text(strip=True)) != 0:
                all_quest.append(j.find("p").get_text(strip=True))
                count_for += 1
        return all_quest

    """конец заполнение задач"""

    """точка отсчета"""
    for i in range(count):
        sort_random = ["hardr", "hard", "fav", "ids", "idsr"]
        work = requests.get(
            f"https://math-ege.sdamgia.ru{tags_a[0]}&sort={sort_random[random.randint(0, len(sort_random))]}")  # делаем запрос на выбранную подзадачу пользователя
        soup_quest = BeautifulSoup(work.content, "html.parser")
        page_take_quest = soup_quest.findAll("div", class_="answer")  # получения всех ответов на странице
        answer_MAIN = []  # ответы которые конвертированы в int
        for answer_i in page_take_quest:  # парсим page_take_quest
            answer_MAIN.append(answer_i.find("span", style="letter-spacing: 2px;").get_text(strip=True)[7:])
        quest_write(soup=soup_quest, count=count)  # вывод всех задач на странице
        send_msg(message=all_quest[i], ID=ID, vk_session=vk_session)

        answer(soup_quest, working)  # ответы на выбранной странице
        send_msg(message="Ответ: ", ID=ID, vk_session=vk_session)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me:
                    answer_quest = event.text
                    break

        if answer_quest == answer_MAIN[i]:
            true_answer += 1
        elif answer_quest == 00:
            false_answer += 1
        else:
            false_answer += 1
        return true_answer, false_answer


def parse():
    """переменные"""

    main_quest = []  # список основных задач
    under_main_quest = []  # список основных под задач
    dictData = json.loads(settings.jsonData)  # превращения из строки в json
    global true_answer, false_answer, selection_for_the_tasks, count_quest, repeat, number_quest

    """вывод основых заданий"""
    for i in range(len(dictData["constructor"])):
        # вывод всех основных задач
        main_quest.append(str(i + 1) + ") " + dictData["constructor"][i]["title"] + "\n")  # массив с задачами
    """конец вывода основных заданий"""
    send_msg(message="".join(main_quest), ID=ID, vk_session=vk_session)
    """выбор задания"""
    send_msg(message="ЧТО БУДЕМ РЕШАТЬ? Введите цифру", ID=ID, vk_session=vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                number_quest = int(event.text)  # выбор задания
                if 0 < number_quest <= 35:
                    break
                elif number_quest <= 0 or number_quest > 35:
                    send_msg(message="Вы вели некорректное число, повторите попытку", ID=ID, vk_session=vk_session)
                    send_msg(message="ЧТО БУДЕМ РЕШАТЬ? Введите цифру", ID=ID, vk_session=vk_session)
                    number_quest = int(event.text)
                else:
                    send_msg(message="Число вводить надо, а не текст", ID=ID, vk_session=vk_session)
                    parse()
    send_msg(message="Вы выбрали - " + dictData["constructor"][number_quest - 1]["title"], ID=ID, vk_session=vk_session)
    """конец выбора заданий"""

    """вывод подзадач"""
    down_main_quest = []
    for i in range(len(dictData["constructor"][number_quest - 1]["subtopics"])):
        down_main_quest.append(str(i + 1) + ") " + dictData["constructor"][number_quest - 1]["subtopics"][i][
            "title"] + "\n")
    """конец вывода подзадач"""
    send_msg(message="".join(down_main_quest), ID=ID, vk_session=vk_session)
    """выбор подзадачи"""
    send_msg(message="Какое задание? Введите цифру", ID=ID, vk_session=vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                selection_for_the_tasks = list(event.text)  # выбор подзадач
                if int(selection_for_the_tasks[0]) <= 0 or int(selection_for_the_tasks[0]) > len(down_main_quest):
                    send_msg(message="Вы вели некорректное число, повторите попытку", ID=ID, vk_session=vk_session)
                    send_msg(message="Какое задание? Введите цифру", ID=ID, vk_session=vk_session)
                elif 0 < int(selection_for_the_tasks[0]) <= len(down_main_quest):
                    break
    select_quest = []
    for i in range(len(selection_for_the_tasks)):
        select_quest.append(dictData["constructor"][number_quest - 1]["subtopics"][int(selection_for_the_tasks[i]) - 1][
                                "title"])
        under_main_quest.append(
            dictData["constructor"][number_quest - 1]["subtopics"][int(selection_for_the_tasks[i]) - 1][
                "title"])  # заполнение списка выбранных подзадач
    send_msg(message="".join(select_quest), ID=ID, vk_session=vk_session)

    """конец выбор подзадачи"""
    """спрашиваем количество задач"""
    send_msg(message="Сколько хотите решить задач, введите число[ 1 - 5 ]: ", ID=ID, vk_session=vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                count_quest = int(event.text)
                if 0 < count_quest <= 5:
                    break
                elif count_quest <= 0 or count_quest > 5:
                    send_msg(message="Вы вели некорректное число, повторите попытку", ID=ID,
                             vk_session=vk_session)
                    send_msg(message="Сколько хотите решить задач, введите число[ 1 - 5 ]: ", ID=ID,
                             vk_session=vk_session)
    send_msg(message=f"Будем решать {count_quest} задачи ", ID=ID, vk_session=vk_session)
    """конец"""

    """получение заданий"""
    global working
    working = True

    get_tags_a(n=number_quest, s=selection_for_the_tasks)  # получения ссылок на выбранные пользователем подзадач(и)
    get_quest(tags_a=all_tags_main, count=count_quest, working=working)  # получения задач и ответы

    """конец получение заданий"""
    """подвод итогов"""
    if true_answer >= false_answer > 0:
        send_msg(
            message=f"Ты ответил на целых ->{true_answer} задач правильно, но и ответил неправильно на ->{false_answer} задач",
            ID=ID, vk_session=vk_session)

    elif true_answer > false_answer == 0:
        send_msg(message=f"Ты гуру, ответил на все вопросы правильно, без единой ошибки ", ID=ID, vk_session=vk_session)


    elif true_answer <= false_answer and true_answer > 0:
        send_msg(
            message=f"старайся лучше, ибо ты ответил на->{true_answer} задач правильно, а неправильных ответов у тебя ->{false_answer}",
            ID=ID, vk_session=vk_session)


    elif true_answer < false_answer and true_answer == 0:
        send_msg(
            message=f"у тебя {true_answer} правильных ответов, зато eсть время подготовится, ведь до егэ осталось,{((6 - datetime.datetime.now().month))} месяцев",
            ID=ID, vk_session=vk_session)
    send_msg(
        message="Eсли хочешь попробровать еще раз свои силы напиши '1', иначе '0'",
        ID=ID, vk_session=vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                repeat = event.text
                break
    if repeat == "1":  # запуск заново программы
        parse()
    else:
        vk_session.method("messages.send",
                          {"user_id": ID,
                           "message": "До скорой встречи!",
                           "random_id": 0})
    """конец итогов"""


def vk():
    global vk_session, session_api, longpoll, ID
    vk_session = vk_api.VkApi(token=settings.TOKEN)
    session_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            msg = event.text.lower()
            ID = event.user_id
            user_use = [ID]
            if msg == "запуск":
                global false_answer, true_answer
                false_answer = true_answer = 0
                parse()


"""точка отсчета кода"""
while True:
    try:
        if __name__ == '__main__':
            vk()
    except Exception:
        pass
