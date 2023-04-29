# meta pic: https://img.icons8.com/stickers/500/000000/code.png
# meta banner: https://mods.hikariatama.ru/badges/carbon.jpg
# meta developer: @jeamoff
# scope: hikka_only
# scope: hikka_min 1.2.10
# requires: urllib requests carbon-api

import io

import requests
from telethon.tl.types import Message

from carbon import Carbon

from .. import loader, utils


@loader.tds
class TextToCode(loader.Module):
    """Create beautiful code images"""

    strings = {
        "name": "txt2code",
        "args": (
            "<emoji document_id=5312526098750252863>🚫</emoji> <b>No args specified</b>"
        ),
        "loading": "<emoji document_id=5213452215527677338>⏳</emoji> <b>Loading...</b>",
    }

    strings_ru = {
        "args": (
            "<emoji document_id=5312526098750252863>🚫</emoji> <b>Не указаны"
            " аргументы</b>"
        ),
        "loading": (
            "<emoji document_id=5213452215527677338>⏳</emoji> <b>Обработка...</b>"
        ),
        "_cls_doc": "Создает симпатичные фотки кода",
        "_cmd_doc_carbon": "<код> - Сделать красивую фотку кода",
    }

    strings_de = {
        "args": (
            "<emoji document_id=5312526098750252863>🚫</emoji> <b>Keine Argumente"
            " angegeben</b>"
        ),
        "loading": "<emoji document_id=5213452215527677338>⏳</emoji> <b>Laden...</b>",
        "_cls_doc": "Erstellt schöne Code-Bilder",
        "_cmd_doc_carbon": "<code> - Erstelle ein schönes Code-Bild",
    }

    strings_hi = {
        "args": (
            "<emoji document_id=5312526098750252863>🚫</emoji> <b>कोई आर्ग्यूमेंट नहीं"
            " दिया गया</b>"
        ),
        "loading": (
            "<emoji document_id=5213452215527677338>⏳</emoji> <b>लोड हो रहा है...</b>"
        ),
        "_cls_doc": "सुंदर कोड छवियां बनाएं",
        "_cmd_doc_carbon": "<कोड> - सुंदर कोड छवि बनाएं",
    }

    strings_uz = {
        "args": (
            "<emoji document_id=5312526098750252863>🚫</emoji> <b>Hech qanday"
            " argumentlar ko'rsatilmadi</b>"
        ),
        "loading": (
            "<emoji document_id=5213452215527677338>⏳</emoji> <b>Yuklanmoqda...</b>"
        ),
        "_cls_doc": "G'ayratli kod rasmlarini yaratish",
        "_cmd_doc_carbon": "<kod> - G'ayratli kod rasmini yaratish",
    }

    strings_tr = {
        "args": (
            "<emoji document_id=5312526098750252863>🚫</emoji> <b>Argümanlar"
            " belirtilmedi</b>"
        ),
        "loading": (
            "<emoji document_id=5213452215527677338>⏳</emoji> <b>Yükleniyor...</b>"
        ),
        "_cls_doc": "Güzel kod resimleri oluşturur",
        "_cmd_doc_carbon": "<kod> - Güzel kod resmi oluşturur",
    }

    client_carbon = Carbon()

    async def texttocodecmd(self, message: Message):
        """<code> - Create beautiful code image"""
        args = utils.get_args_raw(message)



        args = args

        message = await utils.answer(message, self.strings("loading"))

        doc = io.BytesIO(
            (
                await self.client_carbon.create(args)
            ).content
        )
        doc.name = "coded.jpg"

        await self._client.send_message(
            utils.get_chat_id(message),
            file=doc,
            force_document=(len(args.splitlines()) > 50),
            reply_to=getattr(message, "reply_to_msg_id", None),
        )
        await message.delete()