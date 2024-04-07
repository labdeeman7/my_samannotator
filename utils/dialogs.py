import sys
import os
from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout,
                             QComboBox, QPushButton, QLineEdit, QLabel)
from PyQt5.QtCore import pyqtSignal


class ImageNavigationWidget(QDialog):
    
    imageSelected = pyqtSignal(int)
    
    def __init__(self, parent, image_list, init_index=0):
        super(ImageNavigationWidget, self).__init__(parent)
        self.image_list = image_list
        self.setWindowTitle("Image Navigator")
        # Ensure the starting index is within the valid range
        if not (0 <= init_index < len(self.image_list)):
            init_index = 0
        self.init_index = init_index
        self.init_ui()
    
    def init_ui(self):
        self.index_edit = QLineEdit()
        self.index_label = QLabel(f"/{len(self.image_list)}")
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")
        self.image_dropdown = QComboBox()
        
        self.index_edit.setFixedWidth(60)  # Set the width of QLineEdit
        
        # Populate the dropdown with images
        for image_path in self.image_list:
            img_name = os.path.basename(image_path)[:-4]
            self.image_dropdown.addItem(os.path.basename(img_name))
        
        # Set the starting index
        self.image_dropdown.setCurrentIndex(self.init_index)
        self.index_edit.setText(str(self.init_index + 1))
        
        # Connect signals to slots
        self.ok_button.clicked.connect(self.on_ok)
        self.cancel_button.clicked.connect(self.close)  # Does nothing, just close
        self.index_edit.textChanged.connect(self.on_index_change)
        self.image_dropdown.activated.connect(self.on_dropdown_change)  # For double click as well

        # Layouts
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.index_edit)
        top_layout.addWidget(self.index_label)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)
        
        main_layout = QVBoxLayout(self)
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.image_dropdown)
        main_layout.addLayout(button_layout)

    def on_ok(self):
        current_index = self.image_dropdown.currentIndex()
        self.imageSelected.emit(current_index)
        self.close()
        # Logic to move to the selected image goes here

    def on_index_change(self, text):
        if text.isdigit():
            index = int(text) - 1  # Subtract 1 because comboBox indices are 0-based
            if 0 <= index < len(self.image_list):
                self.image_dropdown.setCurrentIndex(index)

    def on_dropdown_change(self, index):
        # No need to simulate an "OK" button click if you only want to highlight the selection
        self.index_edit.setText(str(index + 1))



