import discord
from discord import app_commands
import vacefron

from discord.ext import commands


class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(command_prefix="!",intents= discord.Intents.default(), **kwargs)
        self.vac_api= vacefron.Client()

    #Optional
    async def close(self):
        await self.vac_api.close()
        await super().close()

bot= Bot()   

@bot.tree.command()
async def peposign(interaction: discord.Interaction, text: str):
    image = await bot.vac_api.peeposign(text)
    f =  discord.File(await image.read(), "peposign.png")
    embed= discord.Embed(title="Peposign")
    embed.set_image(url=image.url)
    await interaction.response.send_message(embed=embed)
    # If it doesn't work then you should add await interaction.response.defer() then replace interaction.response.send_message with interaction.followup.send
  
  
bot.run("")
