import discord
from discord import app_commands

bot= commands.Bot(command_prefix="!", intents= discord.Intents.default())
intents.message_content= True
vacefron = vacefron.Client()


@bot.tree.command()
async def peposign(interaction: discord.Interaction, text: str):
  image = await vacefron.vac_api.peeposign(text)
  f =  discord.File(await image.read(), "peposign.png")
  embed= discord.Embed(title="Peposign")
  embed.set_image(url=image.url)
  await interaction.response.send_message(embed=embed)
  
  
bot.run(token)
