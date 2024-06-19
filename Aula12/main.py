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

def excluirContato():
    linhaContato = listarContatos.tabelaCtt.currentRow()
    listarContatos.tabelaCtt.removeRow(linhaContato)
    
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM tb_contatos")

    contatos_lidos = cursor.fetchall()
    valorId = contatos_lidos[linhaContato][0]
    cursor.execute("DELETE FROM tb_contatos WHERE id=" + str(valorId))
    
def gerarPdf():
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM tb_contatos")
    contatos_lidos = cursor.fetchall()
    
    y = 0
    pdf = canvas.Canvas("lista_contatos.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200, 800, "Lista de Contatos")
    
    pdf.setFont("Times-Bold", 15)
    pdf.drawString(10, 750, "ID")
    pdf.drawString(60, 750, "NOME")
    pdf.drawString(180, 750, "EMAIL")
    pdf.drawString(370, 750, "TELEFONE")
    pdf.drawString(460, 750, "TIPO DE CONTATO")
    
    for i in range(0, len(contatos_lidos)):
        y = y + 50
        pdf.drawString(10, 750 - y, str(contatos_lidos[i][0]))
        pdf.drawString(60, 750 - y, str(contatos_lidos[i][1]))
        pdf.drawString(180, 750 - y, str(contatos_lidos[i][2]))
        pdf.drawString(370, 750 - y, str(contatos_lidos[i][3]))
        pdf.drawString(460, 750 - y, str(contatos_lidos[i][4]))
    
    pdf.save()
    print("PDF GERADO COM SUCESSO")
        
def BotaoVoltarAgenda():
    listarContatos.hide()
    agenda.show()

def Atualizar():
    id = update.idLine.text()
    nome = update.nomeLine.text()
    email = update.emailLine.text()
    telefone = update.telefoneLine.text()
    
    if update.radioButton_2.isChecked():
        tipoTelefone = 'residencial'
    elif update.radioButton.isChecked():
        tipoTelefone = 'celular'
    else :
        tipoTelefone = 'nao especificado' 
    
    try:
        cursor = banco.cursor()
        cursor.execute(f" UPDATE tb_contatos set nome='{nome}', email='{email}', telefone='{telefone}', tipoTelefone='{tipoTelefone}' where id={int(id)}")
        banco.commit()
        print(f'Dado do contato {nome} foram alterados com sucesso')
        VoltarContatos()
    except Exception as e:
        print(f'Ocorreu o erro {e} ao tentar atualizar os dados')
    
def InserirDados(id, nome, email, telefone, tipoTelefone):
    listarContatos.hide()
    update.show()
    update.idLine.setText(str(id))
    update.nomeLine.setText(str(nome))
    update.emailLine.setText(str(email))
    update.telefoneLine.setText(str(telefone))
    
    if tipoTelefone == "residencial":
        update.radioButton_2.setChecked(True)
    elif tipoTelefone == "celular":
        update.radioButton.setChecked(True)
    else:
        update.radioButton_2.setChecked(False)
        update.radioButton.setChecked(False)    

def Editar():
    linhaContato = listarContatos.tabelaCtt.currentRow()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM tb_contatos")
    contatos_lidos = cursor.fetchall()
    valorId = contatos_lidos[linhaContato][0]
    nomeCtt = contatos_lidos[linhaContato][1]
    emailCtt = contatos_lidos[linhaContato][2]
    telefoneCtt = contatos_lidos[linhaContato][3]
    
    if contatos_lidos[linhaContato][4] == "residencial":
        tipoTelefone = "residencial"
    elif contatos_lidos[linhaContato][4] == "celular":
        tipoTelefone = "celular"
    else:
        tipoTelefone = "nao especificado"
    
    
    InserirDados(valorId, nomeCtt, emailCtt, telefoneCtt, tipoTelefone)

def VoltarContatos():
    update.hide()
    listarContatos.show()
    ConsultarContato()

app = QtWidgets.QApplication([])
agenda = uic.loadUi("design.ui")
listarContatos = uic.loadUi("contatos.ui")
update = uic.loadUi("Update.ui")

update.btnUpdate.clicked.connect(Atualizar)
update.voltar.clicked.connect(VoltarContatos)

agenda.btnCadastro.clicked.connect(Cadastrar)
agenda.btnConsCont.clicked.connect(ConsultarContato)

listarContatos.btnGerarPdf.clicked.connect(gerarPdf)
listarContatos.btnExcluirCtt.clicked.connect(excluirContato)
listarContatos.btnVoltar.clicked.connect(BotaoVoltarAgenda)
listarContatos.editContact.clicked.connect(Editar)

agenda.show()
app.exec()











    


