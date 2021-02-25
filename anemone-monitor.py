import subprocess
import discord
from discord.ext import commands

ane = commands.Bot(command_prefix="Ane:")

@ane.command("cpustats")
async def cpustats(ctx):
    stats = subprocess.check_output(['mpstat','-P','ALL'], universal_newlines=True)
    await ctx.send(stats)

@ane.command("status")
async def status(ctx,arg: str):
    service = arg + ".service"
    proc1 = subprocess.Popen(["systemctl","status",service],stdout=subprocess.PIPE)
    await ctx.send(service + ":" + subprocess.check_output(['grep','active'],stdin=proc1.stdout,universal_newlines=True))

@ane.command("uptime")
async def uptime(ctx):
    await ctx.send(subprocess.check_output("uptime",universal_newlines=True))

ane.run()