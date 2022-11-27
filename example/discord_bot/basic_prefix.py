import discord

import vacefron

from discord.ext import commands

intents= discord.Intents.default()


class MyBot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix="!", intents=intents, **kwargs)
        self.vac_api= vacefron.Client()
        

    #Optional
    async def close(self):
        await self.vac_api.close()
        await super().close()

bot= Bot()   

@bot.command()
async def peposign(ctx, text: str):
    image = await bot.vac_api.peeposign(text)
    f =  discord.File(await image.read(), "peposign.png")
    embed= discord.Embed(title="Peposign")
    embed.set_image(url=image.url)
    await ctx.send(embed=embed)
  
  
  
bot.run("")
