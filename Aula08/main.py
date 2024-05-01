from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_agenda"
)

def cadastrar():
    campoNome = agenda.textEdit_4.text()
    campoEmail = agenda.textEdit_5.text()
    campoTelefone = agenda.textEdit_2.text()
    
    if agenda.radioButton_2.isChecked():
        tipoTelefone = 'residencial'
    elif agenda.radioButton.isChecked():
        tipoTelefone = 'celular'
    else :
        tipoTelefone = 'nao especificado'    
    
    cursor = banco.cursor()
    cursor.execute("INSERT INTO tb_contatos (nome, email, telefone, tipoTelefone) values (%s, %s, %s, %s)", (str(campoNome), str(campoEmail), str(campoTelefone), str(tipoTelefone)))
    banco.commit()

def main() :
    cadastrar()
    
app = QtWidgets.QApplication([])
agenda = uic.loadUi("design.ui")

agenda.btnCadastro.clicked.connect(main)

agenda.show()
app.exec()









    


