from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor,\
						Text, OpenLink,Location, EMPTY_KEYBOARD
from discord_webhook import DiscordWebhook, DiscordEmbed
from config import settings


bot = Bot(settings['api_key'])

# Ответчик на текс
@bot.on.private_message(text=["Привет","прив","Хай"])
async def hi_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer("Привет, {}".format(users_info[0].first_name)+" чем я могу тебе помочь?")

# Создание кнопок
@bot.on.private_message(text=["menu","меню","Начать","start","Start"])
async def handler(message: Message):
	keyboard = Keyboard()

	keyboard.add(Text("Техническая поддержка"), color=KeyboardButtonColor.POSITIVE)
	keyboard.add(Text("FAQ"), color=KeyboardButtonColor.POSITIVE)
	
	# Перенос кнопок ниже
	keyboard.row()

	keyboard.add(Text("Убрать кнопки"), color=KeyboardButtonColor.NEGATIVE)
	
	# keyboard.add(OpenLink("https://vk.com/market-192558128", "Товары"), color=KeyboardButtonColor.PRIMARY)
	# keyboard.add(OpenLink("https://vk.com/albums-192558128", "Портфолио"), color=KeyboardButtonColor.PRIMARY)

	await message.answer("Привет! Я включил тебе клавиатуру, но если тебе она не нужна просто нажми на соотвествующую кнопку.", keyboard=keyboard)

@bot.on.private_message(text="FAQ")
async def faq(message: Message):
	await message.answer(f"FAQ: Пам парам \n"
						f"Пам парам \n"
						f"Приветсвую смотрящих"
						)

# Удаление кнопок
@bot.on.private_message(text="Убрать кнопки")
async def remove(message: Message):
	await message.answer("Кнопки были убраны😱\nЧтобы вернуть их напишите еще раз Начать", keyboard=EMPTY_KEYBOARD)

# Отправка в ДС
@bot.on.private_message(text="Техническая поддержка")
async def ds(message: Message):

	users_info = await bot.api.users.get(message.from_id)
	webhook = DiscordWebhook(url=settings['webhook'])
	embed = DiscordEmbed(title='Нужны операторы!', description='Новый запрос в группе от **{}**'.format(users_info[0].first_name)+' **{}**'.format(users_info[0].last_name)+'\n'+'Ссылка на сообщение **https://vk.com/'+settings['linkvk']+'?sel={}**'.format(users_info[0].id), color='03b2f8')
	webhook.add_embed(embed)
	webhook.execute()
	await message.answer("Ищем свободных операторов💭")
bot.run_forever()