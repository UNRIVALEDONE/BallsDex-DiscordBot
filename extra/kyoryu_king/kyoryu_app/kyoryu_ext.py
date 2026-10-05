from ballsdex.core.bot import BallsDexBot


async def setup(bot: BallsDexBot):
    await bot.load_extension("kyoryu_app.cog")
