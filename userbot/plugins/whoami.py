from telethon import events

import asyncio

from userbot.utils import admin_cmd

@borg.on(admin_cmd("whoami"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    #input_str = event.pattern_match.group(1)
   # if input_str == "Read This Telegraph Whole info here":
    await event.edit("Hello ")
    animation_chars = [
            "I",
            "I am",
            "I am [Abir Hasan](http://t.me/AbirHasan2005).\nSkills:\n[1] Bash/Shell\n[2] Python\n[3] HTML\n[4] PHP\n[5] Git\n\nI use Ubuntu, Kali, Android and Windows OS.\n\nTelegram Group: [Linux Repositories](http://t.me/linux_repo)\nLearn Coding, Programming & Hacking. Feedback for my GitHub Repositories. Report Bugs and More there. Also get Updates in group.\n\nFollow on:\n[GitHub Profile](https://github.com/AbirHasan2005)\n[Twitter Profile](https://twitter.com/AbirHasan2005)\n[Facebook Profile](https://facebook.com/AbirHasan2005)[Instagram Profile](https://instagram.com/AbirHasan2005)\n"
         ]
            

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])