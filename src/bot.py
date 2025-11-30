import discord
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv

from core.systems.character import criar_personagem

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

class AzuraRealm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="create",
        description="Cria seu personagem no Azura Realm."
    )
    async def create(
        self,
        interaction: discord.Interaction,
        nome: str,
        classe: str,
        str_: int,
        dex: int,
        con: int,
        int_: int,
        wis: int,
        cha: int
    ):
        atributos = {
            "STR": str_,
            "DEX": dex,
            "CON": con,
            "INT": int_,
            "WIS": wis,
            "CHA": cha
        }

        resultado = criar_personagem(
            str(interaction.user.id),
            nome,
            classe,
            atributos
        )

        if "erro" in resultado:
            await interaction.response.send_message(
                f"❌ {resultado['erro']}",
                ephemeral=True
            )
            return

        await interaction.response.send_message(
            f"🧙 Personagem criado!\n"
            f"**Nome:** {resultado['nome']}\n"
            f"**Classe:** {resultado['classe']}\n"
            f"**HP Inicial:** {resultado['hp']}\n"
            f"**Atributos:** {resultado['atributos']}"
        )

async def setup(bot):
    await bot.add_cog(AzuraRealm(bot))

async def main():
    async with bot:
        await bot.load_extension("__main__")
        await bot.start(TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
