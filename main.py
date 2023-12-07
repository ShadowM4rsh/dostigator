import pymorphy2
import datetime
import sqlite3
import sys
from dostigator import Ui_MainWindow
from goals import GoalMainWindow
from main_screen import Main_Screen
from konec import Kon_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QTableWidget, QTableWidgetItem


CREATE_DATABASE_QUERY = f"""
CREATE TABLE goal (
    name        TEXT REFERENCES people (id)
                     PRIMARY KEY
                     NOT NULL
                     UNIQUE,
    description TEXT,
    day_start   TEXT,
    day_finish  TEXT,
    achievement TEXT,
    iteration   TEXT
);
"""
class Database:
    def __init__(self, name):
        self.db_name = name
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()
        try:
            self.result = cur.execute(CREATE_DATABASE_QUERY).fetchall()
        except sqlite3.OperationalError:
            self.result = cur.execute("""SELECT * FROM  goal""").fetchall()
        cur.close()
        con.close()


db = Database("DB.db")
month = {"01": 31, "02": [28, 29], "03": 31, "04": 30, "05": 31, "06": 30, "07": 31, "08": 31,
         "09": 30, "10": 31, "11": 30, "12": 31}
monthi = {"1": 31, "2": [28, 29], "3": 31, "4": 30, "5": 31, "6": 30, "7": 31, "8": 31,
         "9": 30, "10": 31, "11": 30, "12": 31}
weekdays = {"Понедельник": 0,
        "Вторник": 1,
        "Среда": 2,
        "Четверг": 3,
        "Пятница": 4,
        "Суббота": 5,
        "Воскресенье": 6}


class Goal:
    def __init__(self, name, description, day_start, day_finish, achievement, iteration="Понедельник"):
        self.name = name
        self.description = description
        self.daystart = day_start.split("-")
        self.dayfinish = day_finish.split("-")
        self.achievement = achievement
        self.iteration = iteration
        self.remain_before = 0
        self.remain = 0

    def info(self):
        print(self.name, self.description, self.achievement, self.daystart, self.dayfinish,
              self.iteration, sep="\n", end="\n")

    def check(self):
        global month
        dayss = datetime.date(int(self.daystart[2]), int(self.daystart[1]), int(self.daystart[0]))
        daysf = datetime.date(int(self.dayfinish[2]), int(self.dayfinish[1]), int(self.dayfinish[0]))
        delta = daysf - dayss
        delta = int(str(delta).split()[0])
        if delta > 0:
            self.remain = delta
            self.daystart = dayss
            self.dayfinish = daysf
            return "done"
        elif delta == 0:
            return "Время достижения цели должно содержать минимум 1 день."
        else:
            return "Дата конца цели не может быть раньше даты начала."


    def left(self):
        dateee = datetime.date.today()
        day_start = datetime.date(int(self.daystart[0]), int(self.daystart[1]), int(self.daystart[2]))
        day_finish = datetime.date(int(self.dayfinish[0]), int(self.dayfinish[1]), int(self.dayfinish[2]))
        if dateee < day_start:
            delta = day_start - dateee
            delta = int(str(delta).split()[0])
            delta2 = day_finish - day_start
            self.remain_before = int(str(delta2).split()[0])
            return f"До начала цели {delta} дн."
        else:
            delta = day_finish - dateee
            if str(delta)[0] == "0":
                return "0"
            else:
                self.remain = int(str(delta).split()[0])
                return f"Осталось {self.remain} дн."

    def steps_to_complete(self):
        global monthi
        dateee = list(map(int, str(datetime.date.today()).split("-")))
        dcti = {}
        for _ in range(self.remain):
            if dateee[1] == 2:
                if (dateee[0] % 4 == 0 and dateee[0] % 100 != 0) or dateee[0] % 400 == 0:
                    if dateee[2] >= 1 and monthi[str(dateee[1])][1] >= dateee[2]:
                        n = datetime.date(dateee[0], dateee[1], dateee[2])
                        ne = datetime.date.weekday(n)
                        if str(ne) not in dcti:
                            dcti[str(ne)] = 1
                        else:
                            dcti[str(ne)] += 1
                    else:
                        dateee[1] += 1
                        dateee[2] = 1
                        n = datetime.date(dateee[0], dateee[1], dateee[2])
                        ne = datetime.date.weekday(n)
                        if str(ne) not in dcti:
                            dcti[str(ne)] = 1
                        else:
                            dcti[str(ne)] += 1
                else:
                    if dateee[2] >= 1 and monthi[str(dateee[1])][0] >= dateee[2]:
                        n = datetime.date(dateee[0], dateee[1], dateee[2])
                        ne = datetime.date.weekday(n)
                        if str(ne) not in dcti:
                            dcti[str(ne)] = 1
                        else:
                            dcti[str(ne)] += 1
                    else:
                        dateee[1] += 1
                        dateee[2] = 1
                        n = datetime.date(dateee[0], dateee[1], dateee[2])
                        ne = datetime.date.weekday(n)
                        if str(ne) not in dcti:
                            dcti[str(ne)] = 1
                        else:
                            dcti[str(ne)] += 1
            elif dateee[2] >= 1 and monthi[str(dateee[1])] >= dateee[2]:
                n = datetime.date(dateee[0], dateee[1], dateee[2])
                ne = datetime.date.weekday(n)
                if str(ne) not in dcti:
                    dcti[str(ne)] = 1
                else:
                    dcti[str(ne)] += 1
            else:
                if dateee[1] <= 11:
                    dateee[1] += 1
                    dateee[2] = 1
                    n = datetime.date(dateee[0], dateee[1], dateee[2])
                    ne = datetime.date.weekday(n)
                    if str(ne) not in dcti:
                        dcti[str(ne)] = 1
                    else:
                        dcti[str(ne)] += 1
                else:
                    dateee[0] += 1
                    dateee[1] = 1
                    dateee[2] = 1
                    n = datetime.date(dateee[0], dateee[1], dateee[2])
                    ne = datetime.date.weekday(n)
                    if str(ne) not in dcti:
                        dcti[str(ne)] = 1
                    else:
                        dcti[str(ne)] += 1
            dateee[2] += 1
        need_days = [weekdays[x] for x in self.iteration]
        summ = 0
        for elem in need_days:
            summ += dcti[str(elem)]
        return summ

    def add_data(self):
        con = sqlite3.connect("DB.db")
        cur = con.cursor()
        self.iteration = str(self.iteration)
        try:
            cur.execute(f"""INSERT INTO goal(
                     name,
                     description,
                     day_start,
                     day_finish,
                     achievement,
                     iteration) Values('{self.name}', '{self.description}', '{"-".join([str(x) for x in self.daystart])}', '{"-".join([str(x) for x in self.dayfinish])}',
                                        '{self.achievement}', "{self.iteration}")""")
        except sqlite3.IntegrityError:
            return "Данная цель уже существует, изменить её?"
        con.commit()
        cur.close()
        con.close()


    def get_data(self):
        con = sqlite3.connect("DB.db")
        cur = con.cursor()
        self.result = cur.execute("""SELECT * FROM  goal""").fetchall()
        cur.close()
        con.close()
        sl = {}
        for i in self.result:
            sl[i[0]] = list(i[1:])
        return sl

    def edit(self, args):
        con = sqlite3.connect("DB.db")
        cur = con.cursor()
        for elem in args:
            name = elem[0]
            value = elem[1]
            cur.execute(f"""UPDATE goal
                            SET {name} = "{value}"
                            WHERE name = '{self.name}'""")
        con.commit()
        cur.close()
        con.close()

    def clear(self):
        self.name = "Название"
        self.iteration = ["Понедельник, Вторник"]
        self.dayfinish = str(datetime.date.today())
        self.daystart = str(datetime.date.today())
        self.achievement = "Достижение"
        self.description = "Описание"

    def number_of_goal(self, num):
        l = self.get_data()
        li = list(l.keys())
        self.name = li[num - 1]
        self.daystart = l[li[num - 1]][1].split("-")
        self.dayfinish = l[li[num - 1]][2].split("-")
        self.iteration = l[li[num - 1]][4][2:-2]
        self.description = l[li[num - 1]][0]
        self.achievement = l[li[num - 1]][3]


aim = Goal("Ышшшшшш", "Описание", str(datetime.date.today()), str(datetime.date.today()), "Достижение", ["Понедельник"])


class OPENSCREEN(QMainWindow, Ui_MainWindow, GoalMainWindow, Kon_MainWindow):
    def __init__(self):
        super().__init__()
        self.start_screen = Ui_MainWindow()
        self.start_screen.setupUi(self)
        self.start_screen.Enter.clicked.connect(self.ifclick)


    def ifclick(self):
        self.hide()
        self.main_screen = Main_Screen()
        self.main_screen.setupUiii(self)
        self.show()
        self.main_screen.create.clicked.connect(self.create)
        self.main_screen.change.clicked.connect(self.edit)


    def create(self):
        self.goal_screen = GoalMainWindow()
        self.goal_screen.setupUii(self)
        self.show()
        self.goal_screen.submit.clicked.connect(self.subm_check)


    def subm_check(self):
        flag = True
        sl = aim.get_data()
        keys = list(sl.keys())
        date_start = [int(x) for x in self.goal_screen.date_start.text().split(".")]
        date_finish = [int(x) for x in self.goal_screen.date_finish.text().split(".")]
        if self.goal_screen.name_edit.text() == "":
            self.goal_screen.error_marker.setText("Не указано название цели.")
        elif self.goal_screen.name_edit.text() in keys:
            self.goal_screen.error_marker.setText("Цель с таким названием уже существует.")
        else:
            for i in self.goal_screen.iteration_edit.text().split(","):
                if i not in list(weekdays.keys()):
                    self.goal_screen.error_marker.setText("Неправильный формат дней недели.")
                    flag = False
            if flag is True:
                print("done")
                aim.name = self.goal_screen.name_edit.text()
                print("done1")
                aim.daystart = date_start
                print("done2")
                aim.dayfinish = date_finish
                print("done3")
                aim.iteration = self.goal_screen.iteration_edit.text().split(",")
                print("done4")
                aim.description = self.goal_screen.description_edit.text()
                print("done5")
                aim.achievement = self.goal_screen.goal_edit.text()
                print("done6")
                aim.add_data()
                print("done7")
                self.hide()
                """self.main_screen = Main_Screen()
                self.main_screen.setupUiii(self)
                self.show()"""
                self.ifclick()
    def edit(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = OPENSCREEN()
    ex.show()
    sys.exit(app.exec_())