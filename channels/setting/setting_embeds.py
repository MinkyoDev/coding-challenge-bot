from discord import Interaction, Embed, Color

from utils.message_auto_delete import send_message_auto_delete


async def embed_emty_user(interaction: Interaction):
    embed = Embed(
        title="❌ 사용자를 찾을 수 없습니다.",
        description=f"{interaction.user.global_name}님의 정보를 확인할 수 없습니다. 먼저 사용자를 등록하여 주세요.",
        color=Color.red()
    )
    embed.set_footer(text="지속해서 문제가 있다면 관리자에게 문의해 주세요.")

    await send_message_auto_delete(interaction, embed=embed)