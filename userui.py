from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QApplication, QWidget
from style import ElegantDark_Modified
from stringtable import MIT
from time import sleep
import sys, os, ctypes

THEME = ElegantDark_Modified.ELEGANTDARK

class Ui_ClickToGo_MainWidget():
    def __init__(self, object: object):
        self.setupUi(object)

    def setupUi(self, ClickToGo_MainWidget):
        if ClickToGo_MainWidget.objectName():
            ClickToGo_MainWidget.setObjectName(u"ClickToGo_MainWidget")
        ClickToGo_MainWidget.resize(400, 423)
        ClickToGo_MainWidget.setMinimumSize(QSize(400, 423))
        ClickToGo_MainWidget.setMaximumSize(QSize(400, 423))
        ClickToGo_MainWidget.setLayoutDirection(Qt.LeftToRight)
        ClickToGo_MainWidget.setStyleSheet(THEME)
        self.Header_Title = QLabel(ClickToGo_MainWidget)
        self.Header_Title.setObjectName(u"Header_Title")
        self.Header_Title.setGeometry(QRect(100, 20, 191, 51))
        self.Header_Title.setAutoFillBackground(False)
        self.Header_Title.setStyleSheet(u"font: 63 28pt \"Segoe UI Semibold\";")
        self.Header_Title.setTextFormat(Qt.MarkdownText)
        self.Header_Complementary = QLabel(ClickToGo_MainWidget)
        self.Header_Complementary.setObjectName(u"Header_Complementary")
        self.Header_Complementary.setGeometry(QRect(70, 80, 251, 16))
        self.Header_Complementary.setStyleSheet(u"font: 63 8pt \"Segoe UI Semibold\";")
        self.Input_ProjectPath = QLineEdit(ClickToGo_MainWidget)
        self.Input_ProjectPath.setObjectName(u"Input_ProjectPath")
        self.Input_ProjectPath.setGeometry(QRect(10, 130, 291, 20))
        self.Input_ProjectPath.setClearButtonEnabled(False)
        if len(sys.argv) > 1:
            self.Input_ProjectPath.setText(sys.argv[1])
        self.Input_PathChooseBtn = QPushButton(ClickToGo_MainWidget)
        self.Input_PathChooseBtn.setObjectName(u"Input_PathChooseBtn")
        self.Input_PathChooseBtn.setGeometry(QRect(310, 120, 81, 41))
        self.Input_PathChooseBtn.clicked.connect(self.get_folder)
        self.OtherOptionsGroup = QGroupBox(ClickToGo_MainWidget)
        self.OtherOptionsGroup.setObjectName(u"OtherOptionsGroup")
        self.OtherOptionsGroup.setGeometry(QRect(9, 260, 381, 91))
        self.OtherOptionsGroup.setCursor(QCursor(Qt.PointingHandCursor))
        self.OtherOptionsGroup.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.Checkbox_UseRSTinsteadOfMD = QCheckBox(self.OtherOptionsGroup)
        self.Checkbox_UseRSTinsteadOfMD.setObjectName(u"Checkbox_UseRSTinsteadOfMD")
        self.Checkbox_UseRSTinsteadOfMD.setGeometry(QRect(10, 40, 361, 20))
        self.Checkbox_AutoWriteMITLicense = QCheckBox(self.OtherOptionsGroup)
        self.Checkbox_AutoWriteMITLicense.setObjectName(u"Checkbox_AutoWriteMITLicense")
        self.Checkbox_AutoWriteMITLicense.setGeometry(QRect(10, 60, 361, 20))
        self.Checkbox_AddTestsFolder = QCheckBox(self.OtherOptionsGroup)
        self.Checkbox_AddTestsFolder.setObjectName(u"Checkbox_AddTestsFolder")
        self.Checkbox_AddTestsFolder.setGeometry(QRect(10, 20, 361, 20))
        self.NamingYourProjectGroup = QGroupBox(ClickToGo_MainWidget)
        self.NamingYourProjectGroup.setObjectName(u"NamingYourProjectGroup")
        self.NamingYourProjectGroup.setGeometry(QRect(9, 170, 381, 80))
        self.NamingYourProjectGroup.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.ProjectNameLabel = QLabel(self.NamingYourProjectGroup)
        self.ProjectNameLabel.setObjectName(u"ProjectNameLabel")
        self.ProjectNameLabel.setGeometry(QRect(10, 20, 181, 16))
        self.Input_ProjectName = QLineEdit(self.NamingYourProjectGroup)
        self.Input_ProjectName.setObjectName(u"Input_ProjectName")
        self.Input_ProjectName.setGeometry(QRect(10, 40, 181, 20))
        self.ModuleNameLabel = QLabel(self.NamingYourProjectGroup)
        self.ModuleNameLabel.setObjectName(u"ModuleNameLabel")
        self.ModuleNameLabel.setGeometry(QRect(200, 20, 171, 16))
        self.Input_ModuleName = QLineEdit(self.NamingYourProjectGroup)
        self.Input_ModuleName.setObjectName(u"Input_ModuleName")
        self.Input_ModuleName.setGeometry(QRect(200, 40, 171, 20))
        self.Input_CreateBtn = QPushButton(ClickToGo_MainWidget)
        self.Input_CreateBtn.setObjectName(u"Input_CreateBtn")
        self.Input_CreateBtn.setGeometry(QRect(10, 370, 379, 31))
        self.Input_CreateBtn.clicked.connect(self.create_scaffolding)
        self.ProjectFolderLabel = QLabel(ClickToGo_MainWidget)
        self.ProjectFolderLabel.setObjectName(u"ProjectFolderLabel")
        self.ProjectFolderLabel.setGeometry(QRect(10, 110, 91, 16))

        self.retranslateUi(ClickToGo_MainWidget)
        QMetaObject.connectSlotsByName(ClickToGo_MainWidget)
    # setupUi

    def retranslateUi(self, ClickToGo_MainWidget):
        ClickToGo_MainWidget.setWindowTitle(QCoreApplication.translate("ClickToGo_MainWidget", u"Click To Go - Python Scaffolding", None))
        ClickToGo_MainWidget.setWindowFilePath("")
        self.Header_Title.setText(QCoreApplication.translate("ClickToGo_MainWidget", u"Click To Go", None))
        self.Header_Complementary.setText(QCoreApplication.translate("ClickToGo_MainWidget", u"<html><head/><body><p align=\"center\">Get your scaffolding ready in a single click!</p></body></html>", None))
        self.Input_PathChooseBtn.setText(QCoreApplication.translate("ClickToGo_MainWidget", u"Open project \n"
"folder", None))
        self.OtherOptionsGroup.setTitle(QCoreApplication.translate("ClickToGo_MainWidget", u"Other options", None))
        self.Checkbox_UseRSTinsteadOfMD.setText(QCoreApplication.translate("ClickToGo_MainWidget", u"Use .rst instead of .md for documentation files", None))
        self.Checkbox_AutoWriteMITLicense.setText(QCoreApplication.translate("ClickToGo_MainWidget", u"Automatically write the MIT license template into the project", None))
        self.Checkbox_AddTestsFolder.setText(QCoreApplication.translate("ClickToGo_MainWidget", u"Add tests folder", None))
        self.NamingYourProjectGroup.setTitle(QCoreApplication.translate("ClickToGo_MainWidget", u"Naming your project", None))
        self.ProjectNameLabel.setText(QCoreApplication.translate("ClickToGo_MainWidget", u"Project Name:", None))
        self.ModuleNameLabel.setText(QCoreApplication.translate("ClickToGo_MainWidget", u"Module name (lowercase):", None))
        self.Input_CreateBtn.setText(QCoreApplication.translate("ClickToGo_MainWidget", u"Create scaffolding at chosen folder", None))
        self.ProjectFolderLabel.setText(QCoreApplication.translate("ClickToGo_MainWidget", u" Project Folder:", None))
    # retranslateUi

    def get_folder(self):
        folder_path = QFileDialog.getExistingDirectory(None, "Select Folder")
        self.Input_ProjectPath.setText(folder_path)

    def create_scaffolding(self):
        project_folder = self.Input_ProjectPath.text()

        if not os.path.isdir(project_folder): 
            ctypes.windll.user32.MessageBoxW(
                0, 
                "Please provide a valid folder path.", 
                "Invalid folder path", 
                0x00000010
            )
            return
        else:
            project_folder = os.path.abspath(project_folder)

        project_name = self.Input_ProjectName.text()
        module_name = self.Input_ModuleName.text().lower()
        options = {
            "addTests": self.Checkbox_AddTestsFolder.isChecked(),
            "useRST": self.Checkbox_UseRSTinsteadOfMD.isChecked(),
            "autoMIT": self.Checkbox_AutoWriteMITLicense.isChecked()
        }

        def create_module(): os.mkdir(project_folder + "\\" + module_name)
        def create_docs(): 
            os.mkdir(project_folder + "\\" + "docs")
            if options["useRST"]:
                indexRST = open(project_folder + "\\" + "docs" + "\\" + "index.rst", "w")
                indexRST.close()
            else:
                indexMD = open(project_folder + "\\" + "docs" + "\\" + "index.md", "w")
                indexMD.close()
        def create_tests(): os.mkdir(project_folder + "\\" + "tests")
        def create_licensefile(): 
            licensefile = open(project_folder + "\\" + "LICENSE", "w")
            if options["autoMIT"]: licensefile.write(MIT)
            licensefile.close()
        def create_readme():
            readme = open(project_folder + "\\" + "README.md", "w")
            readme.close()
            del readme
            readme = open(project_folder + "\\" + "README.rst", "w")
            readme.close()
        def create_changes():
            changes = open(project_folder + "\\" + "CHANGES.rst", "w")
            changes.close()
        def create_setup_py():
            setup_py = open(project_folder + "\\" + "setup.py", "w")
            setup_py.close()
        def create_init_py():
            init_py = open(project_folder + "\\" + module_name + "\\" + "__init__.py", "w")
            init_py.close()
            os.mkdir(project_folder + "\\" + module_name + "\\" + "lib")

        try:
            create_module()
            create_docs()
            if options["addTests"]: create_tests()
            create_licensefile()
            create_readme()
            create_changes()
            create_setup_py()
            create_init_py()
            sleep(0.5)
            ctypes.windll.user32.MessageBoxW(0, f"Project created successfully! Now you're ready to start development on {project_name}. ^‿^", "Success", 0x00000001)
        except:
            ctypes.windll.user32.MessageBoxW(0, "Something went wrong! \nTry again, and if the problem persists, try changing the project path.", "Error", 0x00000010)

        return

class Application:
    def launch():
        app = QApplication(sys.argv)
        widget = QWidget()
        ui = Ui_ClickToGo_MainWidget(widget)
        widget.show()
        sys.exit(app.exec())

Application.launch()