from PyQt5 import uic, QtWidgets

def main() :
    print("Etec")

app = QtWidgets.QApplication([])
agenda = uic.loadUi('agenda.ui')
agenda.btnCadastro.clicked.connect(main)

agenda.show()
app.exec()