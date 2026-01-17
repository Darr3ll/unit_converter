import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,  # type: ignore
                             QComboBox, QLineEdit, QPushButton, QLabel, QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from unit_converter import convert_units, UNIT_DATA, format_number

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Universal Unit Converter Pro')
        self.setFixedWidth(400)
        self.setStyleSheet("background-color: #2f3640; color: white;")
        
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # Header
        header = QLabel("Universal Converter")
        header.setFont(QFont('Segoe UI', 18, QFont.Weight.Bold))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)

        # 1. Category Dropdown
        layout.addWidget(QLabel("Select Category:"))
        self.cat_combo = QComboBox()
        self.cat_combo.addItems(sorted(UNIT_DATA.keys()))
        self.cat_combo.setStyleSheet("background-color: #f5f6fa; color: black; padding: 5px;")
        self.cat_combo.currentTextChanged.connect(self.update_units)
        layout.addWidget(self.cat_combo)

        # 2. Value Input
        layout.addWidget(QLabel("Enter Value:"))
        self.value_input = QLineEdit()
        self.value_input.setPlaceholderText("e.g. 100")
        self.value_input.setStyleSheet("background-color: #f5f6fa; color: black; padding: 8px; font-size: 16px;")
        layout.addWidget(self.value_input)

        # 3. Units (Side by Side)
        unit_hbox = QHBoxLayout()
        self.from_combo = QComboBox()
        self.to_combo = QComboBox()
        for cb in [self.from_combo, self.to_combo]:
            cb.setStyleSheet("background-color: #f5f6fa; color: black; padding: 5px;")
        
        unit_hbox.addWidget(self.from_combo)
        unit_hbox.addWidget(QLabel("to"))
        unit_hbox.addWidget(self.to_combo)
        layout.addLayout(unit_hbox)

        # 4. Calculate Button
        self.calc_btn = QPushButton("CONVERT")
        self.calc_btn.setFixedHeight(45)
        self.calc_btn.setStyleSheet("""
            QPushButton {
                
                background-color: #00a8ff; 
                border-radius: 5px; 
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover { background-color: #0097e6; }
        """)
        self.calc_btn.clicked.connect(self.perform_conversion)
        layout.addWidget(self.calc_btn)

        # 5. Result Display
        self.result_box = QFrame()
        self.result_box.setStyleSheet("background-color: #353b48; border-radius: 10px; border: 1px solid #7f8fa6;")
        res_layout = QVBoxLayout(self.result_box)
        self.result_text = QLabel("---")
        self.result_text.setFont(QFont('Segoe UI', 14))
        self.result_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        res_layout.addWidget(self.result_text)
        layout.addWidget(self.result_box)

        self.setLayout(layout)
        self.update_units() # Initial units load

    def update_units(self):
        """Updates the From/To dropdowns based on the selected category."""
        category = self.cat_combo.currentText()
        units = list(UNIT_DATA[category].keys())
        self.from_combo.clear()
        self.to_combo.clear()
        self.from_combo.addItems(units)
        self.to_combo.addItems(units)

    def perform_conversion(self):
        try:
            val = float(self.value_input.text())
            cat = self.cat_combo.currentText()
            frm = self.from_combo.currentText()
            to = self.to_combo.currentText()
            
            res = convert_units(val, frm, to, cat)
            formatted = format_number(res)
            self.result_text.setText(f"{formatted} {to.upper()}")
        except ValueError:
            self.result_text.setText("Error: Enter a valid number")
        except Exception:
            self.result_text.setText("Conversion Error")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ConverterApp()
    window.show()
    sys.exit(app.exec())