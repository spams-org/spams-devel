# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewdecomp_gui.ui'
#
# Created: Wed Mar 19 12:40:11 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DecompWindow(object):
    def setupUi(self, DecompWindow):
        DecompWindow.setObjectName(_fromUtf8("DecompWindow"))
        DecompWindow.resize(832, 698)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DecompWindow.sizePolicy().hasHeightForWidth())
        DecompWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(DecompWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.decompviewbb = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.decompviewbb.sizePolicy().hasHeightForWidth())
        self.decompviewbb.setSizePolicy(sizePolicy)
        self.decompviewbb.setMaximumSize(QtCore.QSize(16777215, 40))
        self.decompviewbb.setFrameShape(QtGui.QFrame.StyledPanel)
        self.decompviewbb.setFrameShadow(QtGui.QFrame.Raised)
        self.decompviewbb.setObjectName(_fromUtf8("decompviewbb"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.decompviewbb)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.DDnode_var = QtGui.QComboBox(self.decompviewbb)
        self.DDnode_var.setObjectName(_fromUtf8("DDnode_var"))
        self.DDnode_var.addItem(_fromUtf8(""))
        self.DDnode_var.addItem(_fromUtf8(""))
        self.DDnode_var.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.DDnode_var)
        self.DDall = QtGui.QPushButton(self.decompviewbb)
        self.DDall.setObjectName(_fromUtf8("DDall"))
        self.horizontalLayout.addWidget(self.DDall)
        self.DDClose = QtGui.QPushButton(self.decompviewbb)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.DDClose.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DDClose.setFont(font)
        self.DDClose.setObjectName(_fromUtf8("DDClose"))
        self.horizontalLayout.addWidget(self.DDClose)
        self.DDHelp = QtGui.QPushButton(self.decompviewbb)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 208, 200))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 104, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.DDHelp.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.DDHelp.setFont(font)
        self.DDHelp.setObjectName(_fromUtf8("DDHelp"))
        self.horizontalLayout.addWidget(self.DDHelp)
        self.gridLayout.addWidget(self.decompviewbb, 0, 0, 1, 1)
        self.VDframe = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.VDframe.sizePolicy().hasHeightForWidth())
        self.VDframe.setSizePolicy(sizePolicy)
        self.VDframe.setFrameShape(QtGui.QFrame.StyledPanel)
        self.VDframe.setFrameShadow(QtGui.QFrame.Raised)
        self.VDframe.setObjectName(_fromUtf8("VDframe"))
        self.verticalLayout = QtGui.QVBoxLayout(self.VDframe)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout.addWidget(self.VDframe, 2, 0, 1, 1)
        self.txtFrame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.txtFrame.sizePolicy().hasHeightForWidth())
        self.txtFrame.setSizePolicy(sizePolicy)
        self.txtFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.txtFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.txtFrame.setObjectName(_fromUtf8("txtFrame"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.txtFrame)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.spinLabel = QtGui.QLabel(self.txtFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinLabel.sizePolicy().hasHeightForWidth())
        self.spinLabel.setSizePolicy(sizePolicy)
        self.spinLabel.setObjectName(_fromUtf8("spinLabel"))
        self.horizontalLayout_2.addWidget(self.spinLabel)
        self.spinBox = QtGui.QSpinBox(self.txtFrame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(80)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.dummy = QtGui.QLabel(self.txtFrame)
        self.dummy.setText(_fromUtf8(""))
        self.dummy.setObjectName(_fromUtf8("dummy"))
        self.horizontalLayout_2.addWidget(self.dummy)
        self.gridLayout.addWidget(self.txtFrame, 1, 0, 1, 1)
        DecompWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(DecompWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 832, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        DecompWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(DecompWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        DecompWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DecompWindow)
        QtCore.QMetaObject.connectSlotsByName(DecompWindow)

    def retranslateUi(self, DecompWindow):
        DecompWindow.setWindowTitle(QtGui.QApplication.translate("DecompWindow", "Decomposition Window", None, QtGui.QApplication.UnicodeUTF8))
        self.DDnode_var.setItemText(0, QtGui.QApplication.translate("DecompWindow", "Decomposition on nodes", None, QtGui.QApplication.UnicodeUTF8))
        self.DDnode_var.setItemText(1, QtGui.QApplication.translate("DecompWindow", "Decomposition on variables", None, QtGui.QApplication.UnicodeUTF8))
        self.DDnode_var.setItemText(2, QtGui.QApplication.translate("DecompWindow", "Dict columns", None, QtGui.QApplication.UnicodeUTF8))
        self.DDall.setToolTip(QtGui.QApplication.translate("DecompWindow", "show main words for all items", None, QtGui.QApplication.UnicodeUTF8))
        self.DDall.setText(QtGui.QApplication.translate("DecompWindow", "Show/Hide all words", None, QtGui.QApplication.UnicodeUTF8))
        self.DDClose.setText(QtGui.QApplication.translate("DecompWindow", "CLOSE", None, QtGui.QApplication.UnicodeUTF8))
        self.DDHelp.setText(QtGui.QApplication.translate("DecompWindow", "HELP", None, QtGui.QApplication.UnicodeUTF8))
        self.spinLabel.setText(QtGui.QApplication.translate("DecompWindow", "num of text to view  : ", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    DecompWindow = QtGui.QMainWindow()
    ui = Ui_DecompWindow()
    ui.setupUi(DecompWindow)
    DecompWindow.show()
    sys.exit(app.exec_())

