from discord.ext import commands


class KyoryuKingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def kyoryu(self, ctx):
        await ctx.send("🦖 Kyoryu King Dex is alive!")


async def setup(bot):
    await bot.add_cog(KyoryuKingCog(bot))
