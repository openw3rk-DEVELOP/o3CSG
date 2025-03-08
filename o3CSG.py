# VERSION 5.1 | 2024
# Copyright (c) openw3rk INVENT
# ------------------------------

import sys
import hashlib
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QPushButton, QLabel, QLineEdit, QFileDialog, 
                             QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
# ---------------------------------------------------------
# openw3rk Checksum Generator [o3CSGenerator] | Version 5.1
# ---------------------------------------------^^^^^^^^^^^
# openw3rkCSGenerator COMES WITH ABSOLUTELY NO WARRENTY.
#  
# Copyright (c) openw3rk INVENT 
# ---------------------------------------------------------
class o3CSGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        print ("Welcome to o3CSGenerator | VERSION 5.1\nCopyright (c) openw3rk INVENT\n\n\nLogs and Errors:\n");
    def initUI(self):
        self.setWindowTitle("o3CSGenerator - Checksum generator")
        self.setWindowIcon(QIcon("o3CSG_logo.png")) 
        self.setGeometry(300, 200, 600, 400)  

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        self.file_path_input = QLineEdit(self)
        self.file_path_input.setPlaceholderText("File [PRESS: 'Browse']")
        self.file_path_input.setReadOnly(True)

        browse_btn = QPushButton("Browse", self)
        browse_btn.clicked.connect(self.browse_file)
        browse_btn.setFixedSize(115, 30)  

        self.result_label = QLabel("Checksum: ", self)

        generate_btn = QPushButton("Generate checksum ", self)
        generate_btn.clicked.connect(self.generate_checksum)
        generate_btn.setFixedSize(115, 30)  

        copy_btn = QPushButton("Copy", self)
        copy_btn.clicked.connect(self.copy_checksum)
        copy_btn.setFixedSize(115, 30) 
        main_layout.addWidget(self.file_path_input)
        main_layout.addWidget(browse_btn)
        main_layout.addWidget(self.result_label)
        main_layout.addWidget(generate_btn)
        main_layout.addWidget(copy_btn)
        copyright_label = QLabel("\no3CSGenerator | Version 5.1\n\nCopyright © 2024 openw3rk INVENT\nhttps://openw3rk.de\ndevelop@openw3rk.de", self)
        copyright_label.setAlignment(Qt.AlignCenter)
        copyright_label.setStyleSheet("font-size: 11px; color: #ccc;")
        main_layout.addWidget(copyright_label)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #2E2E2E;  
            }
            QLineEdit {
                padding: 10px;
                border: 1px solid #444;  
                border-radius: 5px;
                color: #fff;  
                background-color: #3C3C3C;  
            }
            QPushButton {
                background-color: black; 
                color: white;
                border: none;
                border-radius: 10px;
                font-size: 11px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QLabel {
                font-size: 14px;
                color: #fff;  
                margin-top: 10px;
            }
        """)

    def browse_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select File", "", "All Files (*);;HTML-Files (*.html);;Textfiles (*.txt)")
        if file_name:
            self.file_path_input.setText(file_name)
    def generate_checksum(self):
        file_path = self.file_path_input.text()
        if not file_path:
            self.result_label.setText("Select File to generate a checksum")
            return
        try:
            with open(file_path, 'rb') as f:
                file_content = f.read()
                checksum = hashlib.sha256(file_content).hexdigest()
                self.result_label.setText(f"Checksum: {checksum}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Cannot read File\n{e}")
    def copy_checksum(self):
        checksum_text = self.result_label.text().replace("Checksum: ", "")
        if checksum_text:
            clipboard = QApplication.clipboard()
            clipboard.setText(checksum_text)
            print ("LOG: Checksum copyd | Checksum generated with the o3CSGenerator.");
        else:
            print ("ERROR: Copy failed. Generate a checksum before try it to copy.");

if __name__ == '__main__':
    app = QApplication(sys.argv)
    generator = o3CSGenerator()
    generator.show()
    sys.exit(app.exec_())
