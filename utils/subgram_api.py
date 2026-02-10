# Или в чат (если нужно)
                        # await bot.send_message(chat.id, message_text, reply_markup=keyboard)
                    except Exception as e:
                        logging.error(f"Failed to send message to {user.id}: {e}")
        else:
            # Приветствуем пользователя
            await bot.send_message(
                chat_id=chat.id,
                text=f"👋 Добро пожаловать, {user.first_name or 'друг'}!"
            )

@dp.callback_query(F.data == "check_subs")
async def check_subs_handler(callback: types.CallbackQuery):
    user = callback.from_user
    
    await callback.answer("⏳ Проверяем подписки...")
    
    response = await get_subgram_sponsors(
        user_id=user.id,
        chat_id=TARGET_CHAT_ID,
        first_name=user.first_name or "",
        username=user.username or "",
        language_code=user.language_code or "ru",
        is_premium=bool(user.is_premium)
    )
    
    if response and response.get('status') != 'warning':
        await callback.message.edit_text("✅ Проверка пройдена! Добро пожаловать в чат!")
    else:
        await callback.answer("❌ Вы подписались не на все каналы", show_alert=True)

async def main():
    logging.info("Starting bot...")
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
