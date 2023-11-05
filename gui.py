# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledZhLdGB.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt,
)
from PyQt5.QtGui import (
    QFont,
)
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1047, 687)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setSizeIncrement(QSize(7, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName("label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(0, 60))
        font = QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.load_frame = QFrame(self.centralwidget)
        self.load_frame.setObjectName("load_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.load_frame.sizePolicy().hasHeightForWidth())
        self.load_frame.setSizePolicy(sizePolicy3)
        self.load_frame.setFrameShape(QFrame.StyledPanel)
        self.load_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.load_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.load_line = QLineEdit(self.load_frame)
        self.load_line.setObjectName("load_line")

        self.horizontalLayout.addWidget(self.load_line)

        self.load_button = QPushButton(self.load_frame)
        self.load_button.setObjectName("load_button")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.load_button.sizePolicy().hasHeightForWidth())
        self.load_button.setSizePolicy(sizePolicy4)
        self.load_button.setMinimumSize(QSize(95, 0))

        self.horizontalLayout.addWidget(self.load_button)

        self.verticalLayout_2.addWidget(self.load_frame)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.verticalLayout_2.addItem(self.horizontalSpacer)

        self.text_frame = QFrame(self.centralwidget)
        self.text_frame.setObjectName("text_frame")
        self.text_frame.setFrameShape(QFrame.StyledPanel)
        self.text_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.text_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.logs_text = QTextBrowser(self.text_frame)
        self.logs_text.setObjectName("logs_text")
        self.logs_text.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.logs_text.sizePolicy().hasHeightForWidth())
        self.logs_text.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.logs_text, 1, 1, 1, 1)

        self.links_text = QTextEdit(self.text_frame)
        self.links_text.setObjectName("links_text")

        self.gridLayout.addWidget(self.links_text, 1, 0, 1, 1)

        self.links_label = QLabel(self.text_frame)
        self.links_label.setObjectName("links_label")

        self.gridLayout.addWidget(self.links_label, 0, 0, 1, 1)

        self.logs_label = QLabel(self.text_frame)
        self.logs_label.setObjectName("logs_label")

        self.gridLayout.addWidget(self.logs_label, 0, 1, 1, 1)

        self.verticalLayout_2.addWidget(self.text_frame)

        self.dir_frame = QFrame(self.centralwidget)
        self.dir_frame.setObjectName("dir_frame")
        self.dir_frame.setFrameShape(QFrame.StyledPanel)
        self.dir_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.dir_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.dir_line = QLineEdit(self.dir_frame)
        self.dir_line.setObjectName("dir_line")

        self.horizontalLayout_2.addWidget(self.dir_line)

        self.dir_button = QPushButton(self.dir_frame)
        self.dir_button.setObjectName("dir_button")
        sizePolicy4.setHeightForWidth(self.dir_button.sizePolicy().hasHeightForWidth())
        self.dir_button.setSizePolicy(sizePolicy4)
        self.dir_button.setMinimumSize(QSize(95, 0))

        self.horizontalLayout_2.addWidget(self.dir_button)

        self.verticalLayout_2.addWidget(self.dir_frame)

        self.submit_button = QPushButton(self.centralwidget)
        self.submit_button.setObjectName("submit_button")

        self.verticalLayout_2.addWidget(self.submit_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.load_frame.raise_()
        self.label.raise_()
        self.dir_frame.raise_()
        self.text_frame.raise_()
        self.submit_button.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1047, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.label.setText(
            QCoreApplication.translate("MainWindow", "LightShot Dwonloader", None)
        )
        self.load_button.setText(
            QCoreApplication.translate("MainWindow", "Load file", None)
        )
        self.links_text.setHtml(
            QCoreApplication.translate(
                "MainWindow",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">Links seperated by white spaces</p></body></html>',
                None,
            )
        )
        self.links_label.setText(
            QCoreApplication.translate("MainWindow", "Links", None)
        )
        self.logs_label.setText(QCoreApplication.translate("MainWindow", "Logs", None))
        self.dir_button.setText(
            QCoreApplication.translate("MainWindow", "Choose dir", None)
        )
        self.submit_button.setText(
            QCoreApplication.translate("MainWindow", "Download Screens", None)
        )

    # retranslateUi
