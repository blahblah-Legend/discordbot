import discord
import random
from discord.ext import commands

intents = discord.Intents.default() // 권한 초기화
intents.message_content = True // 메시지 권한 활성
TOKEN = '' //개인 토큰 만들어서 넣기

bot = commands.Bot(command_prefix='#', intents=intents) // 접두사 설정 및 권한 넣기



@bot.event
async def on_ready(): // 봇 시작
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def 안녕(ctx): //인사 함수
    await ctx.send('안녕하세요! 명령어가 궁금하시면 [도움] 명령어를 입력해주세요!')


@bot.command()
async def 주사위(ctx): // 랜덤을 이용한 주사위 함수
    await ctx.send(random.randrange(1, 7))

@bot.command()
async def 도움(ctx): // 도움 함수
    await ctx.send('아직 [안녕], [주사위], [기분] 기능밖에 없어요 ㅈㅅ ㅎㅎ')

@bot.command()
async def 기분(ctx):  // 이모티콘 보내기
    a = random.randrange(1, 4)
    if(a == 1):
        emoji_name = "laughing"
        await ctx.send(f"기분 최고에요!! :{emoji_name}:")
    elif (a==2):
        emoji_name = "sob"
        await ctx.send(f"많이 슬퍼요 ㅠㅠ :{emoji_name}:")
    else:
        emoji_name = "angry"
        await ctx.send(f"건들지 마세요... :{emoji_name}:")

bot.run(TOKEN) // 봇 실행
