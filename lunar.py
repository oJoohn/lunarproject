import discord
import asyncio

client = discord.Client()
laranja = 0xff8c00
ano = '2020'
prefix = '!'
ultimaatt= '14/03/2020'
@client.event
async def on_ready():
    print("=================================")
    print("Nome: %s"%client.user.name)
    print("ID: %s"%client.user.id)
    print("Online em : {} Serves".format(str(len(client.guilds))))
    print('Em contato com : ' + str(len(set(client.get_all_members()))) + ' usuarios')
    print('Link de convite do {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print("=================================")

    while True:
        ebservers = str(len(client.guilds))
        ebplayers = str(len(set(client.get_all_members())))
        game = discord.Game("Lunar!")
        await client.change_presence(status=discord.Status.idle, activity=game)
        canalservers = client.get_channel(475432717031440395)
        await asyncio.sleep(3)
        game = discord.Game("BETA")
        await client.change_presence(status=discord.Status.idle, activity=game)
        canalusers = client.get_channel(475440504457396224)
        await asyncio.sleep(3)
        game = discord.Game("Lunar!")
        await client.change_presence(status=discord.Status.idle, activity=game)
        await asyncio.sleep(3)
        game = discord.Game("BETA")
        await client.change_presence(status=discord.Status.idle, activity=game)
        await asyncio.sleep(3)

@client.event
async def on_member_join(member):
    role = discord.utils.find(lambda r: r.name == "Novatouss", member.guild.roles)
    await member.add_roles(role)
@client.event
async def on_message(message):
    embedbanidobot = discord.Embed(
        title=None,
        color=laranja,
        description='' + message.author.mention + '\n'
                                                   'Você Foi Banido Permanentemente de Utilizar o Lunar\n'
                                                   'Você não poderá Utilizar meus Comandos'
    )
    embedbanidobot.set_author(name='Lunar - BANIMENTO', icon_url=client.user.avatar_url)
    embedbanidobot.set_footer(text=ano + ' © Lunar')
    errorembedpermi = discord.Embed(
        title=None,
        color=laranja,
        description='Você não tem permissão para executar esse comando',
    )
    errorembedpermi.set_author(name='Lunar - ERROR', icon_url=client.user.avatar_url)
    errorembedpermi.set_thumbnail(url='http://pizzarialukas.com.br/app/webroot/img/erro.png')
    errorembedpermi.set_footer(text=ano + ' © Lunar')

    boterrorembedpermi = discord.Embed(
        title=None,
        color=laranja,
        description='O Bot não tem permissão para executar essa ação',
    )
    boterrorembedpermi.set_author(name='Lunar - ERROR', icon_url=client.user.avatar_url)
    boterrorembedpermi.set_thumbnail(url='http://pizzarialukas.com.br/app/webroot/img/erro.png')
    boterrorembedpermi.set_footer(text=ano + ' © Lunar')

# ajuda------------------------------------------------------------------------------
    if message.content.lower().startswith(prefix + "ajuda"):
        channel = message.channel
        ajudaprincipal = discord.Embed(
            title='Central Ajuda',
            color=laranja,
            description='🔧 - Moderação\n 🎮 - Games \n 💿 - Musica'
        )
        ajudaprincipal.set_author(name='Lunar', icon_url=client.user.avatar_url)
        ajudaprincipal.set_footer(text=ano + ' © Lunar')
        await message.channel.send(embed=ajudaprincipal)

# avatar------------------------------------------------------------------------------
    if message.content.lower().startswith(prefix + "avatar"):
        avatarembed = discord.Embed(
            title=None,
            description=None,
            color=laranja
        )
        avatarembed.set_author(name="Lunar - AVATAR", icon_url=client.user.avatar_url)
        avatarembed.set_image(url=message.author.avatar_url)
        avatarembed.set_footer(text=ano + ' © Lunar')
        avatarmensagem = await message.channel.send(embed=avatarembed)
        await avatarmensagem.add_reaction("❤")

# botinfo------------------------------------------------------------------------------
    if message.content.lower().startswith(prefix + "botinfo"):
        embedbotinfo = discord.Embed(
            title=None,
            description="Meu Servidor: https://discord.gg/2YKVYaE \n Meu Site: https://Lunar.Space \n  󠁿󠁿󠁿 󠁿󠁿 󠁿",
            color=laranja
        )
        embedbotinfo.set_author(name='Lunar - INFO', icon_url=client.user.avatar_url)
        embedbotinfo.add_field(name='Meu Criador:',value="<@369962464613367811>")
        embedbotinfo.add_field(name='Meu Nome:',value=client.user.name)
        embedbotinfo.add_field(name='Online em:', value=(str(len(client.guilds))) + ' Servers')
        embedbotinfo.add_field(name='Usuários:', value=str(len(set(client.get_all_members()))) + ' Usuarios')
        embedbotinfo.add_field(name='Meu Niver:', value='13/03/2020')
        embedbotinfo.add_field(name='Ultima Att:',value=ultimaatt)
        embedbotinfo.add_field(name='Programado em:',value='Py')
        embedbotinfo.add_field(name='Biblioteca',value='discord.py Rewrite')
        embedbotinfo.add_field(name='Como estou:',value=':D')
        embedbotinfo.set_thumbnail(url=client.user.avatar_url)
        embedbotinfo.set_footer(text=ano + ' © Lunar')
        menssageminfo = await message.channel.send(embed=embedbotinfo)
        await menssageminfo.add_reaction("❤")

# marcação------------------------------------------------------------------------------

    if message.content.lower().startswith('lunar'):
        embedmention = discord.Embed(
            title=None,
            color=laranja,
            description="Oi! meu nome é Lunar e meu prefix é " + "'" + prefix + "'"
        )
        embedmention.set_author(name='Lunar', icon_url=client.user.avatar_url)
        embedmention.set_footer(text=ano + ' © Lunar')
        await message.channel.send(embed=embedmention)
    if message.content.lower().startswith('!lunar'):
        embedmention = discord.Embed(
            title=None,
            color=laranja,
            description="Oi! meu nome é Lunar e meu prefix é " + "'" + prefix + "'"
        )
        embedmention.set_author(name='Lunar', icon_url=client.user.avatar_url)
        embedmention.set_footer(text=ano + ' © Lunar')
        await message.channel.send(embed=embedmention)


client.run('Njg4MjA2NjU2NjYzODQ2OTEz.Xmw8vw.8kY_QDwez25c0SBw3omr2HZbhlU')