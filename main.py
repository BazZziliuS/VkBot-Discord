from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor,\
						Text, OpenLink,Location, EMPTY_KEYBOARD
from discord_webhook import DiscordWebhook, DiscordEmbed
from config import settings


bot = Bot(settings['api_key'])
keyboard = ""

# Создание кнопок
@bot.on.private_message(text=["menu","меню","Начать","start","Start"])
async def handler(message: Message):
	global keyboard
	keyboard = Keyboard()
	keyboard.add(Text("Техническая поддержка"), color=KeyboardButtonColor.POSITIVE)
	keyboard.row()
	keyboard.add(Text("About"), color=KeyboardButtonColor.PRIMARY)
	keyboard.add(Text("Убрать кнопки"), color=KeyboardButtonColor.NEGATIVE)
	await message.answer("Привет! Я включил тебе клавиатуру, но если тебе она не нужна просто нажми на соотвествующую кнопку.", keyboard=keyboard)

# Текст о нас
@bot.on.private_message(text="About")
async def faq(message: Message):
	await message.answer(f"💥 О нас: \n"
						f"💕 В этой группе вы можете найти услуги по фотошопу, создание картинок, баннеров, редизайнов, мы занимаемся исключительно дизайном! \n"
						f"✔ Заказы выполняются в кратчайшие сроки!\n"
						f"😉 А еще мы учимся работать с Питоном.")

# Удаление кнопок
@bot.on.private_message(text="Убрать кнопки")
async def remove(message: Message):
	await message.answer('Кнопки были убраны😱\nЧтобы вернуть их напишите еще раз "Начать"', keyboard=EMPTY_KEYBOARD)

# Отправка в ДС
@bot.on.private_message(text="Техническая поддержка")
async def ds(message: Message):

	users_info = await bot.api.users.get(message.from_id)
	webhook = DiscordWebhook(url=settings['webhook'])
	embed = DiscordEmbed(title='', description='🔥Новый запрос в группе от **{}**'.format(users_info[0].first_name)+' **{}**'.format(users_info[0].last_name)+'\n'+'📧Ссылка на сообщение **https://vk.com/'+settings['linkvk']+'?sel={}**'.format(users_info[0].id), color='03b2f8')
	webhook.add_embed(embed)
	webhook.execute()
	await message.answer("Ищем свободных операторов💭")
bot.run_forever()
