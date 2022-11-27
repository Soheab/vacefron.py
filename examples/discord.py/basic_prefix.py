import vacefron

import discord
from discord.ext import commands


intent = discord.Intents(guilds=True, messages=True, message_content=True)


class MyBot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix="!", intents=intents, **kwargs)
        self.vac_api= vacefron.Client()
        

    #Optional
    async def close(self):
        await self.vac_api.close()
        await super().close()

bot= MyBot()   

@bot.command()
async def peposign(ctx, text: str):
    image = await bot.vac_api.peeposign(text)
    embed= discord.Embed(title="Peposign")
    embed.set_image(url=image.url)
    await ctx.send(embed=embed)
  
  
  
bot.run(...)
