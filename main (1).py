import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QFileDialog, QLabel, QWidget
from PyQt5 import uic
import os
from PyQt5 import QtCore, QtGui, QtWidgets

import parameters_lib
import sqlite_for_project



class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):

        self.rls = None

        #отрисовка окна
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1093, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1041, 331))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(430, 10, 151, 31))
        self.label.setStyleSheet("font: 75 14pt \"Arimo\";")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(440, 80, 423, 60))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.g_prm = QtWidgets.QLabel(self.layoutWidget)
        self.g_prm.setObjectName("g_prm")
        self.verticalLayout_3.addWidget(self.g_prm)
        self.g_prd = QtWidgets.QLineEdit(self.layoutWidget)
        self.g_prd.setObjectName("g_prd")
        self.verticalLayout_3.addWidget(self.g_prd)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_4.addWidget(self.label_5)
        self.g_prm_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.g_prm_2.setObjectName("g_prm_2")
        self.verticalLayout_4.addWidget(self.g_prm_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(510, 50, 171, 18))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(870, 50, 58, 18))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.layoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget_2.setGeometry(QtCore.QRect(440, 160, 525, 60))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.g_prm_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.g_prm_3.setObjectName("g_prm_3")
        self.verticalLayout_9.addWidget(self.g_prm_3)
        self.s_prd = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.s_prd.setObjectName("s_prd")
        self.verticalLayout_9.addWidget(self.s_prd)
        self.horizontalLayout_4.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_10.addWidget(self.label_11)
        self.s_prm = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.s_prm.setObjectName("s_prm")
        self.verticalLayout_10.addWidget(self.s_prm)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(10, 80, 391, 60))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.cnr = QtWidgets.QLineEdit(self.widget)
        self.cnr.setObjectName("cnr")
        self.verticalLayout.addWidget(self.cnr)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.straight_r = QtWidgets.QLineEdit(self.widget)
        self.straight_r.setObjectName("straight_r")
        self.verticalLayout_2.addWidget(self.straight_r)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.widget1 = QtWidgets.QWidget(self.frame)
        self.widget1.setGeometry(QtCore.QRect(540, 240, 325, 58))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.widget1)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.g = QtWidgets.QLineEdit(self.widget1)
        self.g.setObjectName("g")
        self.verticalLayout_5.addWidget(self.g)
        self.widget2 = QtWidgets.QWidget(self.frame)
        self.widget2.setGeometry(QtCore.QRect(10, 160, 391, 60))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.widget2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.p = QtWidgets.QLineEdit(self.widget2)
        self.p.setObjectName("p")
        self.verticalLayout_6.addWidget(self.p)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.widget2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.f = QtWidgets.QLineEdit(self.widget2)
        self.f.setObjectName("f")
        self.verticalLayout_7.addWidget(self.f)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.widget3 = QtWidgets.QWidget(self.frame)
        self.widget3.setGeometry(QtCore.QRect(890, 80, 137, 61))
        self.widget3.setObjectName("widget3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.widget3)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.rls_potential = QtWidgets.QLineEdit(self.widget3)
        self.rls_potential.setObjectName("rls_potential")
        self.verticalLayout_8.addWidget(self.rls_potential)
        self.widget4 = QtWidgets.QWidget(self.frame)
        self.widget4.setGeometry(QtCore.QRect(80, 240, 256, 58))
        self.widget4.setObjectName("widget4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget4)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_12 = QtWidgets.QLabel(self.widget4)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_11.addWidget(self.label_12)
        self.r_max = QtWidgets.QLineEdit(self.widget4)
        self.r_max.setObjectName("r_max")
        self.verticalLayout_11.addWidget(self.r_max)
        self.upload_data = QtWidgets.QPushButton(self.centralwidget) #это reset data
        self.upload_data.setGeometry(QtCore.QRect(170, 370, 88, 34))
        self.upload_data.setObjectName("upload_data")
        self.upload_data_2 = QtWidgets.QPushButton(self.centralwidget) #это upload data
        self.upload_data_2.setGeometry(QtCore.QRect(20, 370, 88, 34))
        self.upload_data_2.setObjectName("upload_data_2")
        self.save_data = QtWidgets.QPushButton(self.centralwidget) #это save data
        self.save_data.setGeometry(QtCore.QRect(320, 370, 88, 34))
        self.save_data.setObjectName("save_data")

        self.upload_db = QtWidgets.QPushButton(self.centralwidget)
        self.upload_db.setGeometry(QtCore.QRect(470, 370, 88, 34))
        self.upload_db.setObjectName("upload_db")

        self.get_from_db = QtWidgets.QPushButton(self.centralwidget)
        self.get_from_db.setGeometry(QtCore.QRect(20, 420, 88, 34))
        self.get_from_db.setObjectName("get_from_db")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1093, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #запрет на изменение LineEdit
        self.r_max.setReadOnly(True)
        self.g_prd.setReadOnly(True)
        self.g_prm_2.setReadOnly(True)
        self.s_prd.setReadOnly(True)
        self.s_prm.setReadOnly(True)
        self.cnr.setReadOnly(True)
        self.f.setReadOnly(True)
        self.p.setReadOnly(True)
        self.g.setReadOnly(True)
        self.straight_r.setReadOnly(True)
        self.rls_potential.setReadOnly(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #связь кнопок с реализацией
        self.upload_data_2.clicked.connect(self.upload)
        self.upload_data.clicked.connect(self.reset)
        self.save_data.clicked.connect(self.save)
        self.upload_db.clicked.connect(self.save_to_db)
        self.get_from_db.clicked.connect(self.read_db)


    #реализация работы кнопок


    def upload(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Text Files (*.txt)", options = options)
        if fileName:
            self.readFile(fileName)

    def readFile(self, fileName):
        try:
            with open(fileName, 'r') as file:
                data = file.read().strip().split()
            if len(data) != 20:
                raise ValueError("File must contain exactly 20 variables")

            data = [float(value) for value in data]
            self.rls = parameters_lib.Parameters(*data)

            #заполняем LineEdits
            self.rls.calc_e()
            self.rls.calc_atm_loss()
            self.rls.calc_total_loss()
            self.rls.calc_m()
            self.rls.calc_cnr()


            self.rls.calc_cnr_loss()
            self.cnr.setText(str(self.rls.signal_to_noise_ratio_loss))


            self.rls.calc_straight_r()
            self.straight_r.setText(str(self.rls.straight_r))


            self.rls.calc_g_prd_earth(0.5)
            self.g_prd.setText(str(self.rls.g_prd_earth))


            self.rls.calc_g_prm_earth(0.5)
            self.g_prm_2.setText(str(self.rls.g_prm_earth))

            self.rls.calc_rls_potential()
            self.rls_potential.setText(str(self.rls.rls_potential))


            self.rls.calc_f()
            self.f.setText(str(self.rls.f))

            self.rls.calc_p_f()
            self.p.setText(str(self.rls.p))


            self.rls.calc_p0()

            self.rls.calc_s_prd()
            self.s_prd.setText(str(self.rls.s_prd))

            self.rls.calc_s_per()
            self.s_prm.setText(str(self.rls.s_per))


            self.rls.calc_max_r()
            self.r_max.setText(str(self.rls.r_max))


            self.rls.calc_g()
            self.g.setText(str(self.rls.g))


        except Exception as e:
            QMessageBox.critical(self, 'Error', str(e))



    def reset(self):
        self.rls = None
        self.r_max.clear()
        self.g_prd.clear()
        self.g_prm_2.clear()
        self.s_prd.clear()
        self.s_prm.clear()
        self.cnr.clear()
        self.f.clear()
        self.p.clear()
        self.g.clear()
        self.straight_r.clear()
        self.rls_potential.clear()

    def save(self):
        if self.rls == None:
            QMessageBox.critical(self, 'Error', 'Параметры РЛС не были вычислены -> выводить нечего')
            return

        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getSaveFileName(self, 'Save File', 'Text Files (*.txt)', options = options)

        if fileName:
            try:
                with open(fileName, 'w') as file:
                    data = []
                    data.append(self.rls.signal_to_noise_ratio_loss)
                    data.append(self.rls.straight_r)
                    data.append(self.rls.g_prd_earth)
                    data.append(self.rls.g_prm_earth)
                    data.append(self.rls.rls_potential)
                    data.append(self.rls.p)
                    data.append(self.rls.f)
                    data.append(self.rls.s_prd)
                    data.append(self.rls.s_per)
                    data.append(self.rls.r_max)
                    data.append(self.rls.g)
                    data = [str(item) for item in data]
                    file.write(' '.join(data))
                QMessageBox.information(self, 'Success', 'Data saved to file successfully!')
            except Exception as e:
                QMessageBox.critical(self, 'Error', f'An Error occurred: {e}')



    def save_to_db(self):
        if self.rls == None:
            QMessageBox.critical(self, 'Error', 'Параметры РЛС не были вычислены -> выводить нечего')
            return
        sqlite_for_project.parametrs(self.rls.signal_to_noise_ratio_loss, self.rls.straight_r, self.rls.g_prd_earth, self.rls.g_prm_earth,
                            self.rls.rls_potential, self.rls.p, self.rls.f, self.rls.s_prd, self.rls.s_per, self.rls.r_max, self.rls.g)                   #чтобы выгрузить в нужную бд, надо в функции изменить путь к бд
        QMessageBox.information(self, 'Success', 'Data saved to file successfully!')



    def read_db(self):
        try:
            data = sqlite_for_project.input_parametrs()
            data = [float(value) for value in data]
            self.rls = parameters_lib.Parameters(*data)

            #заполняем LineEdits
            self.rls.calc_e()
            self.rls.calc_atm_loss()
            self.rls.calc_total_loss()
            self.rls.calc_m()
            self.rls.calc_cnr()


            self.rls.calc_cnr_loss()
            self.cnr.setText(str(self.rls.signal_to_noise_ratio_loss))


            self.rls.calc_straight_r()
            self.straight_r.setText(str(self.rls.straight_r))


            self.rls.calc_g_prd_earth(0.5)
            self.g_prd.setText(str(self.rls.g_prd_earth))


            self.rls.calc_g_prm_earth(0.5)
            self.g_prm_2.setText(str(self.rls.g_prm_earth))

            self.rls.calc_rls_potential()
            self.rls_potential.setText(str(self.rls.rls_potential))


            self.rls.calc_f()
            self.f.setText(str(self.rls.f))

            self.rls.calc_p_f()
            self.p.setText(str(self.rls.p))


            self.rls.calc_p0()

            self.rls.calc_s_prd()
            self.s_prd.setText(str(self.rls.s_prd))

            self.rls.calc_s_per()
            self.s_prm.setText(str(self.rls.s_per))


            self.rls.calc_max_r()
            self.r_max.setText(str(self.rls.r_max))


            self.rls.calc_g()
            self.g.setText(str(self.rls.g))

        except Exception as e:
            QMessageBox.critical(self, 'Error', f'An Error occurred: {e}')






    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Параметры РЛС"))
        self.g_prm.setText(_translate("MainWindow", "Коэф-т усиления перед. антенны"))
        self.label_5.setText(_translate("MainWindow", "Коэф-т усиления прием. антенны"))
        self.label_4.setText(_translate("MainWindow", "С учетом влияния Земли"))
        self.g_prm_3.setText(_translate("MainWindow", "Эфф. площадь раскрыва перед. антенны"))
        self.label_11.setText(_translate("MainWindow", "Эфф. площадь раскрыва прием. антенны"))
        self.label_2.setText(_translate("MainWindow", "Сигнал-шум"))
        self.label_3.setText(_translate("MainWindow", "Дальность прямой видимости"))
        self.label_7.setText(_translate("MainWindow", "Двустор. диаграмма направленности по мощности"))
        self.label_8.setText(_translate("MainWindow", "Вероятность обнаружения цели"))
        self.label_9.setText(_translate("MainWindow", "Вероятность ложной тревоги"))
        self.label_10.setText(_translate("MainWindow", "Потенциал РЛС"))
        self.label_12.setText(_translate("MainWindow", "Максимальная дальность обнаружения"))
        self.upload_data.setText(_translate("MainWindow", "Reset Data"))
        self.upload_data_2.setText(_translate("MainWindow", "Upload Data txt"))
        self.save_data.setText(_translate("MainWindow", "Save to txt"))
        self.upload_db.setText(_translate("MainWindow", "Save to db"))
        self.get_from_db.setText(_translate("MainWindow", "Upload Data db"))


#вывод окна
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

