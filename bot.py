import asyncio
import logging
import os
import random
import re
import string
from datetime import datetime
from typing import Pattern

import requests
from telethon import Button, TelegramClient, events
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.sessions import StringSession
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_display_name


from config import API_HASH, API_ID, SESSION


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)


bot = TelegramClient(
    StringSession(SESSION), api_id=API_ID, api_hash=API_HASH, lang_code="tr"
)

# ----------------------ping
@bot.on(events.NewMessage(pattern=".ping"))
async def ping(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("Pong!\n`{}`".format(ms))


# ------------------------------------------link kısaltma
@bot.on(events.NewMessage(pattern="asd (.*) |(.*)"))
async def handler(event):

    aciklama = event.pattern_match.group(1)
    msg = event.text
    link = msg.split(aciklama)

    if aciklama:

        url = f"https://www.pnd.tl/api?api=90edf199f17aa2f2455d8d624cc524a097627291&url={link[-1]}&category=6"

        ksl = requests.get(url).json()
        ksl = ksl["shortenedUrl"]
        await event.edit(
            f"**{aciklama}**\n\n📛 **SESİ AÇ** 'a tıklamayı unutma\n\n𝐋𝐢𝐍𝐊🔗 {ksl}\n\n❗️Link nasıl açılır\n👉 https://t.me/linkk_gecmee"
        )


# ------------------------------------------------------
@bot.on(events.NewMessage(pattern=".post ?(.*)"))
async def post(event):
    yanitlanan_mesaj = await event.get_reply_message()
    count = 0
    await event.edit("`Post gönderiliyor...`")
    try:
        if yanitlanan_mesaj.media:
            await event.client.send_file(
                -1001469818787,
                file=yanitlanan_mesaj.media,
                caption=yanitlanan_mesaj.text,
            )
        else:
            await event.client.send_message(-1001469818787, yanitlanan_mesaj.text)
    except Exception as e:
        grup_kanal = await event.client.get_entity(-1001469818787)
        await event.reply(
            f"Bir kanala post gönderilemedi!\n\n{e}\n\n{grup_kanal.title}"
        )
    else:
        count += 1
    grup_kanal = await event.client.get_entity(-1001469818787)
    await event.edit(f"{grup_kanal.title} `kanalına post gönderildi.`")


# -------------------------------------------------------
@bot.on(events.NewMessage(pattern=".reklam"))
async def reklam(event):
    await event.edit(
        "24 Saat Sabite Alınacak Post 150₺\n12 Saat Sabite Alınacak Post 80₺\n\n24 Saat Duracak Post 100₺\n12 Saat Duracak Post 60₺\n\n__1 Hafta 700₺ 7/24 Sabite Hergün İstediğiniz Saate Reklam Silinip Tekrar Paylaşılacaktır (00.00-01.00) harici__\n\nPost Altı Reklam En Az Alım 1 Hafta 400₺ Uzun Vadeli Anlaşmalarda Fiyat Pazarlığı Yapılır Aylık Anlaşma Söz Konusu İse Her İçeriğimizde Ableminiz Ve Kanalınza Ulaşa Bilcekleri Bağlantılar Paylaşılır\n\n__Her Postun Altında 2. Kanalımız Gibi Abonelere Takdim Edilerek Reklam Yapılır__\n\n**ÖRNEK👇**\n====================\n🌟 Liseli Kuzenini ayakta sikiyor. 🔞\n\n📛 SESİ AÇ 'a tıklamayı unutma\n\n👇DEVAMI LİNKTE👇\n\n**LİNK**🔗 https://pnds.live/ZPPQ0R\n\nYedek Kanalımız 👉 @Reklamınız\n\n❗️Link nasıl açılır\n👉 https://t.me/linkk_gecmee\n====================\n\nReklam Aşağıda Belirtilen Kanalda Yapılacaktır.\n\n👑Kanal Linkimiz👑\nhttps://t.me/joinchat/V5uno4h5L43QKN9o"
    )


# -------------------------------------------------------
@bot.on(events.NewMessage(pattern=".papara"))
async def papara(event):
    await event.edit("**PAPARA Adresim**👇\n1487349446")


# -------------------------------------------------------


@bot.on(events.NewMessage(pattern=".kontrol"))
async def kontrol(event):
    await event.edit("**Çalışıyor**")


@bot.on(events.NewMessage(pattern=".kad"))
async def kad(event):
    await event.edit(
        "Kullanıcı adınızı ana menüdeki sol taraftaki referans bölümünden bulabilirsiniz. Referans linkinizin / işaretinden sonraki sizin kullanıcı adınızdır.\n\nÖrnek:\nwww.pnd. tl/ref/ali    (kullanıcı adı: ali) "
    )


@bot.on(events.NewMessage(pattern=".22cpm"))
async def cpm(event):
    await event.edit(
        "22TL CPM almak için aşşağıdaki kayıt linkinden kaydolup kullanıcı adınızı @admin etiketi ile gruba atmanız gerekmektedir, eğer kaydınız varsa yine aynı şekilde @admin etiketi ile gruba atmanız gerekmektedir. CPM panelinize gün içinde tanımlanır, tanımlanınca bir yönetici sizinle iletişime geçecektir...\n\nKayıt Linki: https://www.pnd.tl/auth/signup"
    )


@bot.on(events.NewMessage(pattern=".kaydol"))
async def kaydol(event):
    await event.edit(
        "1.Adım: www.pnd.tl/ref/Ademko bu linke tıkla.\n2.Adım: Sağ üstteki üç çizgiden 'KAYDOL' yazısına tıkla ve kaydol.\n3.Adım: Kullanıcı adını telegram grubumuza @admin etiketi ile yöneticilere ilet."
    )


@bot.on(events.NewMessage(pattern=".deneme"))
async def deneme(event):
    await event.edit("**Deneme Kısa Linkimiz👇**\nhttps://pnds.live/denemelink")


@bot.on(events.NewMessage(pattern=".ödeme"))
async def odeme(event):
    await event.edit(
        "**PND.TL ÖDEME LİMİTLERİ VE TARİHLERİ**\n\n**Papara** Alt Limit 50TL'dir.\n**Banka ve İninal** Alt Limit 15TL'dir.\n**Bitcoin** Alt Limit 100TL'dir.\n**Dogecoin** Alt Limit 150TL'dir.\n\nPapara: Günlük ödeme.\nBitcoin: Günlük ödeme.\nDogecoin: Günlük ödeme.\nBanka ve İninal: Her Ayın 1-11-21'nde\n\n\n**DİKKAT**👇⚠️\nBanka ve İninal için ayın 1-11-21 inde yapılan çekim talepleri bir sonraki ödeme tarihinde yapılacaktır."
    )


@bot.on(events.NewMessage(pattern=".api"))
async def api(event):
    resim = "https://raw.githubusercontent.com/qhardplayerq/SiriUserBot-1/master/userbot/modules/api.JPG"
    text = "APİ adresimize sol taraftaki menü çubuğundaki **Araçlar** sekmesinden **Geliştirici API** bölümünden yeşil kutunun içinde bulabilirsiniz..."
    await event.client.send_file(event.chat_id, file=resim, caption=text)


id_list = [
    -1001275989066,
    -1001435523233,
    -1001276667828,
    -1001399376603,
    -1001377871517,
    -1001559899893,
    -1001328224261,
    -1001476898506,
    -1001254179689,
    -1001226168546,
    -1001245244239,
    -1001583615217,
    -1001463683383,
    -1001338215425,
    -1001224401851,
    -1001561556131,
    -1001384162511,
    -1001535512195,
]


@bot.on(events.NewMessage(pattern="^.otopnd"))
async def otoreklamm(event):
    global id_list
    text = "PND.TL Olarak Türkiyedeki En yüksek CPM oranı veren site olarak kazancınıza kazanç katıyoruz\n\n**22TL CPM**\n**Eksiksiz Sayım**\n**Temiz IP Havuzu**\n**Bol Kazançlı Etkinlikler**\n**Kolay Reklam Geçişi**\n**Yetkililer İle Kolay İletişim**\n\nSizinde Tek Yapmanız Gereken Bizi Kullanmak\n\nSorularınız ve düşünceleriniz için DM 👇\nİletişim: @BlackkSkyyqq"
    await event.edit("Çalışıyor.")
    while True:
        for x in id_list:
            try:
                await bot.send_file(
                    int(x),
                    "https://raw.githubusercontent.com/qhardplayerq/SiriUserBot-1/master/userbot/modules/pndcpmlogo.png",
                    caption=text,
                )
            except Exception as e:
                print(e)
                await bot.send_message("me", f"{x} idyi kotrol et aq !")
                pass
        await bot.send_message("me", "Gönderildi !")
        await asyncio.sleep(14500)


# ----------------------------------------------------------------------------------


bot.start()
bot.run_until_disconnected()
