from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from datetime import datetime

TOKEN = "8690128213:AAFohMlhzSuoNVxUVdxlGw44sldQOYBfEJU"

def get_ci_time():
    return datetime.utcnow().strftime("%H:%M:%S")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot actif")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = get_ci_time()
    await update.message.reply_text(f"📊 SIGNAL\n⏰ {now}\n📈 BUY")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

print("Bot lancé...")
app.run_polling()
