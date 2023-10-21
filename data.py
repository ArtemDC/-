import json
class Question:
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    def show_quest(self, q_lb, rb_list):
        q_lb.setText(self.question)
        rb_list[0].setText(self.right)
        rb_list[1].setText(self.wrong1)
        rb_list[2].setText(self.wrong2)
        rb_list[3].setText(self.wrong3)
    def show_res(self, r_lb, answ_lb, rb_list):
        if rb_list[0].isChecked():
            r_lb.setText("Вірно")
        else:
            r_lb.setText("Невірно")
        answ_lb.setText(self.right)
data = [{"text":"Как зовут главных героев геншина?",
          "right answer":"Итер\Люмин", 
          "wrong1":"Сяо\Цици",
          "wrong2":"Итер\Кли",
          "wrong3":"Венти\Дилюк"},
          {"text":"Какой первый регион в геншине?",
          "right answer":"Монштад", 
          "wrong1":"Сумеру",
          "wrong2":"Инадзума",
          "wrong3":"Снежная"},
          {"text":"Что будет если наложить на противника статус пиро пока на нём был статус дендро?",
          "right answer":"Начнётся реакция горение", 
          "wrong1":"Начнётся реакция таяние",
          "wrong2":"Начнётся реакция перегрузка",
          "wrong3":"Начнётся реакция заряжен"},
          {"text":"Какой гарант круток в ивентном баннере?",
          "right answer":"90", 
          "wrong1":"80",
          "wrong2":"70",
          "wrong3":"60"},
          {"text":"Какая стихия у Гань юй?",
          "right answer":"Крио", 
          "wrong1":"Пиро",
          "wrong2":"Дендро",
          "wrong3":"Электро"},
          {"text":"Как называется реакция Пиро + Электро?",
          "right answer":"Перегрузка", 
          "wrong1":"Таяние",
          "wrong2":"Заряжен",
          "wrong3":"Кристализация"},
          {"text":"Какой ник у человека который вибыл нахиду и не играет?",
          "right answer":"Говноед", 
          "wrong1":"Скам",
          "wrong2":"Таджик",
          "wrong3":"Сухрик"},
          {"text":"Кто такая нахида?",
          "right answer":"Архонт", 
          "wrong1":"Лолька",
          "wrong2":"Нпс",
          "wrong3":"Антагонист"},
          {"text":"Кто такой дайнслейф?",
          "right answer":"Проклятый житель Каэнриарх", 
          "wrong1":"Искатель приключений",
          "wrong2":"Торговец",
          "wrong3":"Компаньён"},
          {"text":"Хойовёрс контора?",
          "right answer":"Настоящих мужчин", 
          "wrong1":"Идиотов",
          "wrong2":"Полный дураков",
          "wrong3":"Пи..."},
          {"text":"На какое аниме есть отсылки в геншине?",
          "right answer":"Джо Джо", 
          "wrong1":"Клинок рассекающий демонов",
          "wrong2":"Ван пис",
          "wrong3":"Токийский гуль"},
          {"text":"Чтобы прокачать сяо какие цветы нужны?",
          "right answer":"Цинь сынь", 
          "wrong1":"Мята",
          "wrong2":"Цветок сахарок",
          "wrong3":"Стеклянные колокольчики"},
          {"text":"Кем работает ризли в тюрьме?",
          "right answer":"Управляющим", 
          "wrong1":"Охранником",
          "wrong2":"Поваром",
          "wrong3":"Рабочим"},
          {"text":"Какая основная стихия в регионе Фонтейн?",
          "right answer":"Гидро", 
          "wrong1":"Пиро",
          "wrong2":"Анемо",
          "wrong3":"Гео"},
          {"text":"Скольно на данный момент игровых архонтов?",
          "right answer":"4", 
          "wrong1":"5",
          "wrong2":"3",
          "wrong3":"6"},
          {"text":"Какой был первый баннер в игре?",
          "right answer":"Венти", 
          "wrong1":"Джун ли",
          "wrong2":"Кли",
          "wrong3":"Джинн"},
          {"text":"Какой был максимальнный урон на Ху тао?",
          "right answer":"9999999", 
          "wrong1":"10 миллионов",
          "wrong2":"7 миллионов",
          "wrong3":"9 миллионов"},
          {"text":"Кто такой Нёвиллет?",
          "right answer":"Гидро дракон", 
          "wrong1":"Гидро Архонт",
          "wrong2":"Судья Фонтейна",
          "wrong3":"Друг Архонта"},
          {"text":"Из-за чего на первом баннере Кокоми на неё выплеснулся большой хейт?",
          "right answer":"Из-за на тот момент ненадобности в персонаже", 
          "wrong1":"Из-за её дизайна",
          "wrong2":"Из-за её характера по сюжету",
          "wrong3":"По приколу"},
          {"text":"Геншин фигня?",
          "right answer":"Полнейшая, не играйте в него", 
          "wrong1":"Лучшая игра всех времён",
          "wrong2":"Полнейшая имба",
          "wrong3":"Очень проработанная игра"}]
          
with open("berserk.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

q_list = []
with open("berserk.json", "r", encoding="utf-8") as file:
    data = json.load(file)
# print(type(data))
for question in data:
    q = Question(question["text"], question["right answer"], question["wrong1"], question["wrong2"], question["wrong3"])
    q_list.append(q)