import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} olarak giriş yaptı ve hazır!")
    await bot.change_presence(activity=discord.Game(name="!bilgi yaz ve keşfet!"))

@bot.command()
async def bilgi(ctx):
    embed = discord.Embed(
        title="Kullanılabilir Komutlar",
        description="Atık türleri hakkında bilgi almak için aşağıdaki komutları kullanabilirsiniz:",
        color=0x00ff00
    )
    embed.add_field(name="!pil", value="Pillerin çevresel etkileri hakkında bilgi alırsınız.", inline=False)
    embed.add_field(name="!plastik", value="Plastiklerin çevresel etkileri hakkında bilgi alırsınız.", inline=False)
    embed.add_field(name="!cam", value="Cam atıkların çevresel etkisi hakkında bilgi alırsınız.", inline=False)
    embed.add_field(name="!metal", value="Metal atıkların çevresel etkisi hakkında bilgi alırsınız.", inline=False)
    embed.add_field(name="!kağıt", value="Kağıt atıkların geri dönüşüm süreci hakkında bilgi alırsınız.", inline=False)
    embed.set_footer(text="Daha fazla bilgi için komutları kullanabilirsiniz!")
    await ctx.send(embed=embed)

@bot.command()
async def pil(ctx):
    embed = discord.Embed(
        title="Pillerin Çevresel Etkileri",
        description=(
            "Piller, çevreye zararlı kimyasal maddeler içerir. Kadmiyum, cıva ve kurşun gibi ağır metaller "
            "toprağı ve suyu kirletebilir. Çöpe atılan bir pilin doğada çözünmesi yüzlerce yıl sürebilir. "
            "Lütfen pilleri geri dönüşüm kutularına atmayı unutmayın."
        ),
        color=0xff0000
    )
    file = discord.File("pil_zararlari.jpg", filename="pil_zararlari.jpg")
    embed.set_image(url="attachment://pil_zararlari.jpg")
    await ctx.send(embed=embed, file=file)

@bot.command()
async def plastik(ctx):
    embed = discord.Embed(
        title="Plastiklerin Çevresel Etkileri",
        description=(
            "Plastikler doğada çok uzun yıllar boyunca çözünmeden kalabilir ve yaban hayatını tehdit eder. "
            "Denizlerdeki plastik atıklar deniz canlıları için büyük bir tehlike oluşturur. "
            "Plastikleri geri dönüşüme kazandırarak çevremizi koruyabilirsiniz."
        ),
        color=0x1e90ff
    )
    file = discord.File("plastik_zararlari.jpg", filename="plastik_zararlari.jpg")
    embed.set_image(url="attachment://plastik_zararlari.jpg")
    await ctx.send(embed=embed, file=file)

@bot.command()
async def cam(ctx):
    embed = discord.Embed(
        title="Cam Atıkların Çevresel Etkileri",
        description=(
            "Cam atıklar doğada çözünmez ve yüzlerce yıl boyunca çevreyi kirletebilir. "
            "Ancak cam, %100 geri dönüştürülebilir ve tekrar kullanılabilir bir malzemedir. "
            "Lütfen cam atıkları geri dönüşüm kutularına atın."
        ),
        color=0x00ced1
    )
    file = discord.File("cam_zararlari.jpg", filename="cam_zararlari.jpg")
    embed.set_image(url="attachment://cam_zararlari.jpg")
    await ctx.send(embed=embed, file=file)

@bot.command()
async def metal(ctx):
    embed = discord.Embed(
        title="Metal Atıkların Çevresel Etkileri",
        description=(
            "Metal atıklar doğada uzun yıllar boyunca kalabilir ve çevresel zararlar verebilir. "
            "Metallerin geri dönüştürülmesi hem çevreyi korur hem de enerji tasarrufu sağlar. "
            "Metal atıklarınızı geri dönüşüm kutularına atmayı unutmayın."
        ),
        color=0x808080
    )
    file = discord.File("metal_zararlari.jpg", filename="metal_zararlari.jpg")
    embed.set_image(url="attachment://metal_zararlari.jpg")
    await ctx.send(embed=embed, file=file)

@bot.command()
async def kağıt(ctx):
    embed = discord.Embed(
        title="Kağıt Atıkların Geri Dönüşüm Süreci",
        description=(
            "Kağıt atıkların geri dönüşümü, doğal kaynakları korumak için oldukça önemlidir. "
            "Kağıt geri dönüştürülerek daha az ağaç kesilir ve enerji tasarrufu sağlanır. "
            "Kağıt atıkları geri dönüşüm kutularına atmayı unutmayın."
        ),
        color=0xffd700
    )
    file = discord.File("kagit_zararlari.jpg", filename="kagit_zararlari.jpg")
    embed.set_image(url="attachment://kagit_zararlari.jpg")
    await ctx.send(embed=embed, file=file)


TOKEN = ""
bot.run(TOKEN)