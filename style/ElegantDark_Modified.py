ELEGANTDARK = """/*
ElegantDark Style Sheet for QT Applications
Author: Jaime A. Quiroga P.
Company: GTRONICK
Last updated: 17/04/2018
Available at: https://github.com/GTRONICK/QSS/blob/master/ElegantDark.qss
*/
QMainWindow {
	background-color:rgb(82, 82, 82);
}
QTextEdit {
	background-color:rgb(42, 42, 42);
	color: rgb(0, 255, 0);
}
QPushButton{
	border-style: outset;
	border-width: 2px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-bottom-color: rgb(58, 58, 58);
	border-bottom-width: 1px;
	border-style: solid;
	color: rgb(255, 255, 255);
	padding: 2px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));
}
QPushButton:hover{
	border-style: outset;
	border-width: 2px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));
	border-bottom-color: rgb(115, 115, 115);
	border-bottom-width: 1px;
	border-style: solid;
	color: rgb(255, 255, 255);
	padding: 2px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));
}
QPushButton:pressed{
	border-style: outset;
	border-width: 2px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(62, 62, 62, 255), stop:1 rgba(22, 22, 22, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-bottom-color: rgb(58, 58, 58);
	border-bottom-width: 1px;
	border-style: solid;
	color: rgb(255, 255, 255);
	padding: 2px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));
}
QPushButton:disabled{
	border-style: outset;
	border-width: 2px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-bottom-color: rgb(58, 58, 58);
	border-bottom-width: 1px;
	border-style: solid;
	color: rgb(0, 0, 0);
	padding: 2px;
	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));
}
QLineEdit {
	border-width: 1px; border-radius: 4px;
	border-color: rgb(58, 58, 58);
	border-style: inset;
	padding: 0 8px;
	color: rgb(255, 255, 255);
	background:rgb(100, 100, 100);
	selection-background-color: rgb(187, 187, 187);
	selection-color: rgb(60, 63, 65);
}
QLabel {
	color:rgb(255,255,255);	
}
QProgressBar {
	text-align: center;
	color: rgb(240, 240, 240);
	border-width: 1px; 
	border-radius: 10px;
	border-color: rgb(58, 58, 58);
	border-style: inset;
	background-color:rgb(77,77,77);
}
QProgressBar::chunk {
	background-color: qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));
	border-radius: 5px;
}
QMenuBar {
	background:rgb(82, 82, 82);
}
QMenuBar::item {
	color:rgb(223,219,210);
	spacing: 3px;
	padding: 1px 4px;
	background: transparent;
}

QMenuBar::item:selected {
	background:rgb(115, 115, 115);
}
QMenu::item:selected {
	color:rgb(255,255,255);
	border-width:2px;
	border-style:solid;
	padding-left:18px;
	padding-right:8px;
	padding-top:2px;
	padding-bottom:3px;
	background:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));
	border-bottom-color: rgb(58, 58, 58);
	border-bottom-width: 1px;
}
QMenu::item {
	color:rgb(223,219,210);
	background-color:rgb(78,78,78);
	padding-left:20px;
	padding-top:4px;
	padding-bottom:4px;
	padding-right:10px;
}
QMenu{
	background-color:rgb(78,78,78);
}
QTabWidget {
	color:rgb(0,0,0);
	background-color:rgb(247,246,246);
}
QTabWidget::pane {
		border-color: rgb(77,77,77);
		background-color:rgb(101,101,101);
		border-style: solid;
		border-width: 1px;
    	border-radius: 6px;
}
QTabBar::tab {
	padding:2px;
	color:rgb(250,250,250);
  	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));
	border-style: solid;
	border-width: 2px;
  	border-top-right-radius:4px;
   border-top-left-radius:4px;
	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));
	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));
	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));
	border-bottom-color: rgb(101,101,101);
}
QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {
  	background-color:rgb(101,101,101);
  	margin-left: 0px;
  	margin-right: 1px;
}
QTabBar::tab:!selected {
    	margin-top: 1px;
		margin-right: 1px;
}
QCheckBox {
	color:rgb(223,219,210);
	padding: 2px;
}
QCheckBox:hover {
	border-radius:4px;
	border-style:solid;
	padding-left: 1px;
	padding-right: 1px;
	padding-bottom: 1px;
	padding-top: 1px;
	border-width:1px;
	border-color: rgb(87, 97, 106);
	background-color:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 150), stop:1 rgba(93, 103, 113, 150));
}
QCheckBox::indicator:checked {
	border-radius:4px;
	border-style:solid;
	border-width:1px;
	border-color: rgb(180,180,180);
  	background-color:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));
}
QCheckBox::indicator:unchecked {
	border-radius:4px;
	border-style:solid;
	border-width:1px;
	border-color: rgb(87, 97, 106);
  	background-color:rgb(255,255,255);
}
QStatusBar {
	color:rgb(240,240,240);
}
QWidget {
	background-color:rgb(82, 82, 82);
}
QLabel {
	rgb(255, 255, 255)
	font: 8pt "Segoe UI";
}"""