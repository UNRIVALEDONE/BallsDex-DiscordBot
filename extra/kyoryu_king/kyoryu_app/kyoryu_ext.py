from typing import TYPE_CHECKING

from discord.ext import commands

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot


class KyoryuCog(commands.Cog):
    def __init__(self, bot: "BallsDexBot"):
        self.bot = bot

    @commands.command()
    async def kyoryu(self, ctx: commands.Context["BallsDexBot"]):
        await ctx.send("🦖 Kyoryu King Dex is alive!")


async def setup(bot: "BallsDexBot"):
    await bot.add_cog(KyoryuCog(bot))
