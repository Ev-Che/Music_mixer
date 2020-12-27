from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, \
    QFileDialog, QMessageBox

import logic


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.mixer = logic.Mixer()
        self.directory = ''
        self.setWindowTitle('Music mixer')

        folder_path = QHBoxLayout()

        self.path_label = QLabel(f'Selected directory: {self.directory}')
        folder_path.addWidget(self.path_label)

        folder_layout = QHBoxLayout()

        select_folder_button = QPushButton('Select folder')
        select_folder_button.clicked.connect(self.get_directory)

        shuffle_files_button = QPushButton('Shuffle')
        shuffle_files_button.clicked.connect(self.shuffle)

        folder_layout.addWidget(shuffle_files_button)
        folder_layout.addWidget(select_folder_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(folder_path)
        main_layout.addLayout(folder_layout)

        widget = QWidget()
        widget.setLayout(main_layout)

        self.setCentralWidget(widget)

    def get_directory(self):
        self.directory = QFileDialog.getExistingDirectory(self, 'Select folder', '.')
        self.path_label.setText(f'Selected directory: {self.directory}')

    def shuffle(self):
        if not self.directory:
            QMessageBox.critical(self, 'Error', 'Select folder first')
        else:
            error = self.mixer.shuffle(self.directory)
            if error:
                QMessageBox.critical(self, 'Error', 'No such directory')
            else:
                QMessageBox.information(self, 'Success', 'Successfully mixed')


if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()
