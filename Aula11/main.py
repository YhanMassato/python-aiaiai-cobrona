from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_atv"
)

def Cadastrar():

    if atividade.greenLed.isChecked():
        corLed = 'verde'
    elif atividade.blueLed.isChecked():
        corLed = 'azul'
    elif atividade.redLed.isChecked():
        corLed = 'vermelho'
    else :
        corLed = 'none'    
    
    cursor = banco.cursor()
    cursor.execute("INSERT INTO tb_leds (ledCor) values (%s)", ([corLed]))
    banco.commit()
    print(f'O Valor {corLed} foi cadastrado no banco de dados')



app = QtWidgets.QApplication([])
atividade = uic.loadUi("design.ui")

atividade.enviar.clicked.connect(Cadastrar)

atividade.show()
app.exec()