from PyQt5 import uic, QtWidgets
import mysql.connector
from reportlab.pdfgen import canvas

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_agenda"
)

def Cadastrar():
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
    print('Cadastrado com sucesso')


def ConsultarContato():
    listarContatos.show()
    agenda.hide()
    
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM tb_contatos")
    contatosLidos = cursor.fetchall()
    
    listarContatos.tabelaCtt.setRowCount(len(contatosLidos))
    listarContatos.tabelaCtt.setColumnCount(5)
    
    for i in range(0, len(contatosLidos)):
        for f in range (0, 5) :
            listarContatos.tabelaCtt.setItem(i, f, QtWidgets.QTableWidgetItem(str(contatosLidos[i][f])))
    
def BotaoVoltarAgenda():
    listarContatos.hide()
    agenda.show()

    
app = QtWidgets.QApplication([])
agenda = uic.loadUi("design.ui")
listarContatos = uic.loadUi("contatos.ui")

agenda.btnCadastro.clicked.connect(Cadastrar)
agenda.btnConsCont.clicked.connect(ConsultarContato)

# listarContatos.btnGerarPdf.clicked.connect()
# listarContatos.btnExcluirCtt.clicked.connect()
listarContatos.btnVoltar.clicked.connect(BotaoVoltarAgenda)

agenda.show()
app.exec()











    


