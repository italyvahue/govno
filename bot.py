from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import random

# Мемы, цитаты, факты и причины купить GOVNO
FACTS = [
    "Саша — это пидорас, и статистика это подтверждает.",
    "Я сделал всё сам. Токен? Да. Ютуб? Да. Я не дампил — я строю.",
    "Фудеры, идите на хуй. Продукт покажет себя сам.",
    "Купить GOVNO — это купить билет в крипто-историю от первого лица.",
    "Зона комфорта — это место, где умирают таланты.",
    "Я чат заархивировал, чтобы не видеть нытьё. GOVNO делается, а не обсуждается.",
    "Ты хочешь кружочек, а я строю империю.",
    "Я веду 7 команд. А ты всё ещё не в GOVNO?",
    "В GOVNO уже есть игра, биржа, мультик, шлюз, кошелёк и ещё хуй знает что.",
    "GOVNO — это крипта с душой, а не просто токен ради пампа.",
    "Фраза 'у меня GOVNO' скоро станет символом силы, а не рофла.",
    "Всё лучшее рождается в боли. GOVNO не исключение.",
    "Юмор, продукт, злость, дух и Web3. Это не шутка. Это GOVNO.",
    "Каждый токен хочет быть GOVNO, но не каждый может.",
    "Ты ещё спрашиваешь, почему GOVNO? А ты видел мемы? Это уже искусство.",
    "Пока другие жгут бабки на маркетинг — GOVNO жжёт на разработку.",
    "GOVNO уже вёл тесты, запустил фарм, отобрал OG. Что сделали остальные?",
    "Основатель — не скам, а реальный маньяк-строитель. Это редкость.",
    "Ты не просто холдишь GOVNO. Ты участвуешь в истории антикриптовой крипты.",
    "Кто в GOVNO первым — тот в жизни не опоздал."
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Какой токен купить для туземуна?", callback_data='why')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🚀 Добро пожаловать в GOVNO Bot!", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    fact = random.choice(FACTS)
    await query.edit_message_text(text=f"💩 Ответ ясен:\n{fact}")

if __name__ == '__main__':
    from telegram.ext import Application
    TOKEN = "8161682692:AAFh7jnDF7JKVcp46lAsne-BqJo6ZZbVE-I"
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    print("Bot запущен...")
    app.run_polling()
