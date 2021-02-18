import langdetect
from googletrans import Translator
import time
translator = Translator()

async def determine_language(message):
    try:
        lang = translator.detect(message.content)
        # print("[LANGUAGE] ", lang)
        if lang.lang == "es" or lang.lang == "de":
            print("[LANGUAGE] ["+time.strftime('%Y-%m-%d %H:%M:%S')+"]", message.author.name+" to ", lang.lang)
            translation = translator.translate(message.content).text
            print(str(translation).lower().replace(" ", ""))
            if str(translation).lower().replace(" ", "") != message.content and \
                    str(translation).lower() != message.content:
                await message.reply("**Translation:  **"+translation, mention_author=False)
    except Exception as e:
        print("[ERROR] [LANGUAGE] ["+time.strftime('%Y-%m-%d %H:%M:%S')+"]" + str(e))