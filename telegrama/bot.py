import telebot

CHAVE_API = "7158257619:AAHxd48GcMA7FdX77bBDY9v0utKz0QvI6ZY"

bot = telebot.TeleBot(CHAVE_API)


conversas_em_andamento = {}
@bot.message_handler(commands=["primeira"])
def primeira(mensagem): 
    conversas_em_andamento[mensagem.chat.id] = "obter_nome" 
    bot.reply_to(mensagem, "Informe seu nome completo, por favor.")

# Handler para mensagens normais
@bot.message_handler(func=lambda mensagem: True)
def responder(mensagem): 
    chat_id = mensagem.chat.id
    estado = conversas_em_andamento.get(chat_id)

    if estado == "obter_nome":
        nome = mensagem.text
        conversas_em_andamento[chat_id] = "obter_cpf" 
        bot.reply_to(mensagem, "Agora, informe o CPF do aluno.")
    elif estado == "obter_cpf":
        cpf = mensagem.text
        conversas_em_andamento[chat_id] = "obter_re"  
        bot.reply_to(mensagem, "Por fim, qual é o RE do aluno.")
    elif estado == "obter_re":
        re = mensagem.text
        conversas_em_andamento.pop(chat_id)  
        bot.reply_to(mensagem, "Obrigado, irei buscar as informações no banco de dados.")
        


@bot.message_handler(commands=["segunda"])
def segunda(mensagem): 
    pass

@bot.message_handler(commands=["terceira"])
def terceira(mensagem): 
    pass



def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def responder(mensagem): 
    texto = """
    Clique na opção que condiz com sua necessidade:
    /primeira opção - status de documentos do aluno que você é responsável
    /segunda opção - relatar um problema 
    /terceira opção - sugerir alguma melhoria"""
    bot.reply_to(mensagem, texto)




bot.polling()