from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, CallbackContext

# Token của bot Telegram
TOKEN = '7061710795:AAFW210fA7936MgbMRHNDi4sZYkRu3sSbkk'

# Hàm xử lý lệnh /start
async def start(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    # Tạo Reply Keyboard
    reply_keyboard = [
        [KeyboardButton("Reply Button 1"), KeyboardButton("Reply Button 2")],
        [KeyboardButton("Reply Button 3")]
    ]
    reply_markup = ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=True)

    # Tạo Inline Keyboard
    inline_keyboard = [
        [
            InlineKeyboardButton("CẬP NHẬT HỒ SƠ", callback_data='update_profile'),
            InlineKeyboardButton("THÔNG TIN LIÊN LẠC", callback_data='contact_info')
        ],
        [
            InlineKeyboardButton("XÁC MINH GIỚI TÍNH", callback_data='verify_gender'),
            InlineKeyboardButton("CHỨC NĂNG CHO NỮ", callback_data='female_features')
        ],
        [
            InlineKeyboardButton("💞 KÊNH GHÉP ĐÔI", callback_data='match_channel'),
            InlineKeyboardButton("NHÓM NỮ", callback_data='female_group')
        ]
    ]
    inline_markup = InlineKeyboardMarkup(inline_keyboard)

    # Gửi tin nhắn với Reply Keyboard và Inline Keyboard
    await context.bot.send_message(
        chat_id=chat_id,
        text="TRANG CHỦ",
        reply_markup=reply_markup
    )
    await context.bot.send_message(
        chat_id=chat_id,
        text="*HỒ SƠ CỦA BẠN*\n\n"
        "🏠\n"
        "Hạng: 🥉\n"
        "🗒️\n"
        "👤 Chưa xác minh giới tính hãy cập nhật hồ sơ\n"
        "🎂 0\n"
        "📏 0\n"
        "☎️\n\n"
        "Thời gian ghép đôi còn lại của bạn: 0 Ngày\n"
        "Số người đã ghép đôi: 18134\n"
        "<b>[QUẢNG CÁO]</b> <a href='https://www.google.com'>KIẾM TIỀN</a>",
        parse_mode='HTML',
        reply_markup=inline_markup
    )

# Hàm xử lý các callback từ Inline Keyboard
async def button(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Bạn đã nhấn nút: {query.data}")

# Hàm xử lý tin nhắn
async def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    await update.message.reply_text(f"Bạn đã gửi tin nhắn: {text}")

def main():
    # Khởi tạo Application
    application = Application.builder().token(TOKEN).build()

    # Thêm các handler cho các lệnh và callback
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Bắt đầu bot
    application.run_polling()

if __name__ == '__main__':
    main()
