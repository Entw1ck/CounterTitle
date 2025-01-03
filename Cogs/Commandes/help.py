import discord
from discord.ext import commands
from discord import app_commands
import datetime

class Help(commands.Cog):
    def __init__(self, bot, hexcolor):
        self.bot = bot
        self.hexcolor = hexcolor

    @commands.hybrid_command(name='help', description="Affiche le paneau d'aide")
    @app_commands.describe(commande='La commande')
    @app_commands.choices(commande=[
    app_commands.Choice(name="ping", value="ping"),
    app_commands.Choice(name="cns", value="cns"),
    app_commands.Choice(name="mode", value="mode"),
    app_commands.Choice(name="help", value="help")
    ])
    async def help(self, ctx, commande='not specified'):
        if commande == 'not specified':
            helpembed = discord.Embed(
                title="Panneau d'aide",
                description="Voici les commandes que le bot prends en charge ainsi que leurs utilitées.\nPour rapelle, les arguments entre [] sont obligatoire, tandis que ceux entre <> sont facultatif",
                color=self.hexcolor,
                timestamp=datetime.datetime.now()
            )
            helpembed.set_image(url="https://i.ibb.co/0KTmLMs/Banner.jpg")
            helpembed.add_field(name="&ping", value="Le bot répond afin de vérifier sa présence en ligne", inline=False)
            helpembed.add_field(name="&cns [nouveau nom de serveur]", value="Change le nom du serveur", inline=False)
            helpembed.add_field(name="&mode", value="Change le mode du compteur de membre présent dans le titre", inline=False)
            helpembed.add_field(name="&help <commande>", value="Affiche le panneau d'aide", inline=False)
            await ctx.send(embed=helpembed)

        elif commande.lower() == 'ping' :
            helpembed = discord.Embed(
                title="Panneau d'aide",
                description="`&ping`\nCette commande vérifie l'état du bot, en indiquant la version, et où trouver la collection d'image qu'il utilise.\n\nPermission requises : Envoyer des messages",
                color=self.hexcolor,
                timestamp=datetime.datetime.now()
            )
            helpembed.set_image(url="https://i.ibb.co/Lh0sXqh/Help-alternative-embed.jpg")
            await ctx.send(embed=helpembed)
        
        elif commande.lower() == 'cns' :
            helpembed = discord.Embed(
                title="Panneau d'aide",
                description="`&cns [nom du serveur]`\nCette commande permet de changer le nom du serveur, en remplacent %membercount% par le nombre d'utilisateur divisé par 1000, puis arrondi par le mode.\n\nPermission requises : Administrateur",
                color=self.hexcolor,
                timestamp=datetime.datetime.now()
            )
            helpembed.set_image(url="https://i.ibb.co/Lh0sXqh/Help-alternative-embed.jpg")
            await ctx.send(embed=helpembed)

        elif commande.lower() == 'mode' :
            helpembed = discord.Embed(
                title="Panneau d'aide",
                description="`&mode [type]`\nCette commande séléctionne le mode d'affichage du nombre de membre\n\n**Usage:**\n\n`&mode 1` = arrondit au millième près\n`&mode 2` = arrondit au centième près\n`&mode 3` = arrondit au dixième près\n`&mode 4` = arrondit a l'unité près\n\nPermission requises : Administrateur",
                color=self.hexcolor,
                timestamp=datetime.datetime.now()
            )
            helpembed.set_image(url="https://i.ibb.co/Lh0sXqh/Help-alternative-embed.jpg")
            await ctx.send(embed=helpembed)

        elif commande.lower() == 'help' :
            helpembed = discord.Embed(
                title="Panneau d'aide",
                description="`&help`\nCette commande permet de vérifier l'usage des autres commandes\n\nPermission requises : Envoyer des messages",
                color=self.hexcolor,
                timestamp=datetime.datetime.now()
            )
            helpembed.set_image(url="https://i.ibb.co/Lh0sXqh/Help-alternative-embed.jpg")
            await ctx.send(embed=helpembed)

        else :
            helpembed = discord.Embed(
                title="Erreur",
                description=f'Vérifie l\'usage de la commande',
                color=discord.Color.from_str("#ff0000"),
                timestamp=datetime.datetime.now()
                )
            await ctx.send(embed=helpembed)