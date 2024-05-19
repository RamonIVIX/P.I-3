import telebot
import psycopg2

#conexao = psycopg2.connect(database = "alunos",
#                           host = "localhost",
#                           user = "postgres",
#                           password = "1234",
 #                          port = "5432")


CHAVE_API = "7158257619:AAHxd48GcMA7FdX77bBDY9v0utKz0QvI6ZY"
bot = telebot.TeleBot(CHAVE_API)

conversas_em_andamento = {}
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
        conversas_em_andamento.pop(chat_id)  
        bot.reply_to(mensagem, "Obrigado, irei buscar as informações no banco de dados.")
    else:
        texto = """
        Clique na opção que condiz com sua necessidade:
        /primeira opção - consultar dados do aluno que você é responsável
        /segunda opção - relatar um problema 
        /terceira opção - outro tipo de solicitação"""
        bot.reply_to(mensagem, texto)
        return  # Adicionando o retorno aqui
bot.polling()