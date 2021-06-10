import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    

@bot.listen()
async def on_message(message):

    if "!franklin dolar" in message.content.lower():
            
        urldolaroficial = "https://api-dolar-argentina.herokuapp.com/api/dolaroficial"
        urldolarblue    = "https://api-dolar-argentina.herokuapp.com/api/dolarblue"
        urldolarturista = "https://api-dolar-argentina.herokuapp.com/api/dolarturista"
        urldolarbolsa   = "https://api-dolar-argentina.herokuapp.com/api/dolarbolsa"
        
       
        dolarblue    = requests.get(urldolarblue)
        dolarturista = requests.get(urldolarturista)
        dolarbolsa   = requests.get(urldolarbolsa)
        
        dolaroficial = dolaroficial.json()
        dolarblue    = dolarblue.json()     
        dolarturista = dolarturista.json()
        dolarbolsa   = dolarbolsa.json()
        
        embed=discord.Embed(title="Titulo", url="", description="Descripcion", color=0xFF5733)
        embed.set_author(name="Franklin", icon_url="https://qualitasaagg.files.wordpress.com/2018/10/ben_franklin_3.jpg")
        embed.set_thumbnail(url="https://qualitasaagg.files.wordpress.com/2018/10/ben_franklin_3.jpg")
        
        embed.add_field(name="Dolar Oficial", value="Compra : ${}  Venta ${}".format(dolaroficial['compra'],dolaroficial['venta']), inline=False) 
        embed.add_field(name="Dolar Blue",    value="Compra : ${}  Venta ${}".format(dolarblue['compra'],   dolarblue['venta']),    inline=False) 
        embed.add_field(name="Dolar Turista", value="Compra : ${}  Venta ${}".format(dolarturista['compra'],dolarturista['venta']), inline=False) 
        embed.add_field(name="Dolar Bolsa",   value="Compra : ${}  Venta ${}".format(dolarbolsa['compra'],  dolarbolsa['venta']),   inline=False) 
        embed.set_footer(text="Footer")
        
        await message.channel.send(embed=embed)
                                 
bot.run('ODQzMzA0NDQ5ODE2NjU3OTQw.YKB6eA.-m5Nf_SVtF40_9zD1ih-cdx5Nls')