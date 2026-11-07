from document_chatbot import build_faq_bot
bot=build_faq_bot()
print("Question: How do I reset my password?")
print(bot.reply("How do I reset my password?"))
