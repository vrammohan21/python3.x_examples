from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
layout.addWidget(QLabel("Warehouse Management System"))
layout.addWidget(QPushButton("Manage Inventory"))
window.setLayout(layout)
window.show()
app.exec()