import telebot
import psycopg2

CHAVE_API = "7158257619:AAHxd48GcMA7FdX77bBDY9v0utKz0QvI6ZY"
bot = telebot.TeleBot(CHAVE_API)

conversas_em_andamento = {}

# Função para conectar ao banco de dados e buscar informações do aluno pelo RE
def get_student_info(re_alu):
    try:
        # Conexão com o banco de dados
        conn = psycopg2.connect(
            database="alunos",
            host="localhost",
            user="postgres",
            password="1234",
            port="5432"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT nome_alu, data_nascimento_alu, cpf_alu, nome_responsavel_alu, documento_alu FROM alunos WHERE re_alu = %s", (re_alu,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

@bot.message_handler(commands=["segunda"])
def segunda(mensagem):
    bot.reply_to(mensagem, "Qual problema você encontrou?")
    
@bot.message_handler(commands=["terceira"])
def terceira(mensagem): 
    bot.reply_to(mensagem, "Certo, o que precisa?")

@bot.message_handler(commands=["primeira"])
def primeira(mensagem): 
    conversas_em_andamento[mensagem.chat.id] = "obter_nome"  
    bot.reply_to(mensagem, "Informe seu nome completo, por favor.")

@bot.message_handler(func=lambda mensagem: True)
def responder(mensagem): 
    chat_id = mensagem.chat.id
    estado = conversas_em_andamento.get(chat_id)

    if estado == "obter_nome":
        nome = mensagem.text
        conversas_em_andamento[chat_id] = "obter_nasc"  
        bot.reply_to(mensagem, "Agora, informe a data de nascimento do aluno.")
    elif estado == "obter_nasc":
        nasc = mensagem.text
        conversas_em_andamento[chat_id] = "obter_re"  
        bot.reply_to(mensagem, "Por fim, qual é o RE do aluno.")
    elif estado == "obter_re":
        re = mensagem.text
        student_info = get_student_info(re)
        conversas_em_andamento.pop(chat_id)  

        if student_info:
            nome_alu, data_nascimento_alu, cpf_alu, nome_responsavel_alu, documento_alu = student_info
            response = (f"Informações do Aluno:\n"
                        f"Nome: {nome_alu}\n"
                        f"Data de Nascimento: {data_nascimento_alu}\n"
                        f"CPF: {cpf_alu}\n"
                        f"Responsável: {nome_responsavel_alu}\n"
                        f"Documento: {documento_alu}")
        else:
            response = "Aluno não encontrado. Verifique o número do RE e tente novamente."
        
        bot.reply_to(mensagem, response)
    else:
        texto = """
        Clique na opção que condiz com sua necessidade:
        /primeira - Consultar dados do aluno que você é responsável
        /segunda - Relatar um problema 
        /terceira - Outro tipo de solicitação"""
        bot.reply_to(mensagem, texto)

bot.polling()