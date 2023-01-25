from config import CONFIG
from crud.usersCRUD import CRUDUser
from loader import bot
from schemas import UserSchema
#  https://discord.gg/44Gs6nC2


@bot.event  # Когда пользователь подключился к серверу
async def on_member_join(member):
    a = str(member)
    get_user = await CRUDUser.get(user_name=a)

    await member.send("Привет, я Бот\n"
                      "Просмотр команд начинается с !start")

    for i in bot.get_guild(member.guild.id).channels:
        if i.name == "основной":
            await bot.get_channel(i.id).send(f"{member.mention}, Круто что ты с нами!\n"
                                             f"В лс инфо")

    if not get_user:
        name_server = str(member.guild.id)
        name_user = str(member)
        await CRUDUser.add(user=UserSchema(name_server=name_server,
                                           name_user=name_user,
                                           count=0)
                           )


@bot.event  # Когда пользователь покидает канал
async def on_member_remove(member):
    for channel in bot.get_guild(member.guild.id).channels:
        if channel.name == "основной":
            await bot.get_channel(channel.id).send(f"{member.mention}, Покинул нас!")


@bot.command()
async def start(ctx):
    author = ctx.message.author
    await ctx.send(f"{author.mention} Доступные команды :")


@bot.command()
async def commands(ctx, arg):
    author = ctx.message.author
    if arg == "None":
        await ctx.send(f"{author} Доступные команды :")
    elif arg == "Команды":
        pass
    else:
        await ctx.send(f"{author} Нет такой команды!")


if __name__ == '__main__':
    bot.run(CONFIG.BOT.TOKEN)
