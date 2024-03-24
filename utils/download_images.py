import aiohttp
from pathlib import Path

async def download_image(message, save_directory="static/images/temp"):
    for attachment in message.attachments:
        if any(attachment.filename.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif']):
            save_directory = Path(save_directory)
            save_directory.mkdir(exist_ok=True)

            file_path = save_directory / attachment.filename

            async with aiohttp.ClientSession() as session:
                async with session.get(attachment.url) as resp:
                    if resp.status == 200:
                        with open(file_path, 'wb') as f:
                            while True:
                                chunk = await resp.content.read(1024)
                                if not chunk:
                                    break
                                f.write(chunk)
            return file_path