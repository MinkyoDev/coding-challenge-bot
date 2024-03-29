from discord import Interaction, Embed, Color

from db.models import User
from utils.message_auto_delete import send_message_auto_delete


async def embed_complite(interaction: Interaction, user: User, type: str):
    if type == "Registration":
        embed = Embed(
            title="✅ 등록 완료!", 
            description=f"{user.global_name} 님이 성공적으로 추가되었습니다.",
            color=Color.blue()
        )
    elif type == "Modification":
        embed = Embed(
            title="✅ 수정 완료!", 
            description=f"{user.global_name} 님의 정보가 성공적으로 수정되었습니다.",
            color=Color.green()
        )
    embed.set_thumbnail(url=f"https://avatars.githubusercontent.com/{user.git_username}")
    embed.add_field(name="Github username", value=user.git_username, inline=False)
    embed.add_field(name="Repository name", value=user.repository_name, inline=False)

    await send_message_auto_delete(interaction, embed)
    
async def embed_emty_user(interaction: Interaction):
    embed = Embed(
        title="❌ 사용자를 찾을 수 없습니다.",
        description=f"{interaction.user.global_name}님의 정보를 확인할 수 없습니다. 먼저 사용자를 등록하여 주세요.",
        color=Color.red()
    )
    embed.set_footer(text="지속해서 문제가 있다면 관리자에게 문의해 주세요.")

    await send_message_auto_delete(interaction, embed)

async def embed_already_registered(interaction: Interaction):
    embed = Embed(
        title="❎ 이미 등록된 사용자입니다.",
        description="귀하의 사용자 정보는 이미 시스템에 등록되어 있습니다.",
        color=Color.blue()
    )
    embed.add_field(name="정보 수정하기", value="정보를 업데이트하거나 변경하고 싶으신 경우, 수정 기능를 이용해 주세요.", inline=False)
    embed.set_footer(text="🔎 더 많은 도움이 필요하신 경우, 관리자에게 문의해 주세요.")

    await send_message_auto_delete(interaction, embed)
    
async def embed_invalid_info(interaction: Interaction):
    embed = Embed(
        title="❌ GitHub 정보를 확인할 수 없습니다.",
        description="입력하신 GitHub 사용자 이름이나 레포지토리를 찾을 수 없습니다. 사용자 이름과 레포지토리 이름이 정확한지 확인하고, 대소문자를 올바르게 입력했는지 확인해주세요.",
        color=Color.orange()
    )
    embed.set_footer(text="🔎 더 많은 도움이 필요하신 경우, 관리자에게 문의해 주세요.")

    await send_message_auto_delete(interaction, embed)
    
async def embed_deactivate_complite(interaction: Interaction, user: User):
    embed = Embed(
        title="✅ 비활성화 완료!",
        description=f"{user.global_name} 님이 성공적으로 비활성화되었습니다.",
        color=Color.red()
    )
    embed.add_field(name="기능 활성화", value="해당 기능을 다시 활성화하려면, 등록을 한번 더 진행해 주세요.", inline=False)
    await send_message_auto_delete(interaction, embed)
    
async def embed_incorrect_keyword(interaction: Interaction):
    embed = Embed(
        title="❌ 비활성화 명령어를 확인할 수 없습니다.",
        description="기능을 비활성화하기 위해서는 '비활성화'라고 정확하게 입력해야 합니다. 입력하신 내용을 확인하고, 올바른 키워드로 다시 시도해주세요.",
        color=Color.red()
    )
    embed.set_footer(text="🔎 더 많은 도움이 필요하신 경우, 관리자에게 문의해 주세요.")

    await send_message_auto_delete(interaction, embed)
    
async def embed_already_deactivated(interaction: Interaction):
    embed = Embed(
        title="❎ 이미 비활성화 중입니다.",
        description="요청하신 기능은 이미 비활성화 상태입니다. 해당 기능을 다시 활성화하고 싶으시거나 다른 조치가 필요한 경우, 아래 안내를 참고해 주세요.",
        color=Color.greyple()
    )
    embed.add_field(name="기능 활성화", value="해당 기능을 다시 활성화하려면, 등록을 한번 더 진행해 주세요.", inline=False)
    embed.set_footer(text="🔎 더 많은 도움이 필요하신 경우, 관리자에게 문의해 주세요.")

    await send_message_auto_delete(interaction, embed)
    
async def embed_cannot_edit_while_deactivated(interaction: Interaction):
    embed = Embed(
        title="❌ 현재 정보 수정이 불가능합니다.",
        description="요청하신 기능이 현재 비활성화 상태에 있습니다. 기능이 비활성화된 상태에서는 정보 수정이 불가능합니다.",
        color=Color.red()
    )
    embed.add_field(name="기능 활성화하기", value="기능을 활성화하고 정보를 수정하고 싶으시면, 등록을 한번 더 진행해 주세요.", inline=False)
    embed.set_footer(text="🔎 더 많은 도움이 필요하신 경우, 관리자에게 문의해 주세요.")

    await send_message_auto_delete(interaction, embed)
    
async def embed_duplicate_git_username(interaction: Interaction, git_username: str):
    # 임베드 생성
    embed = Embed(
        title="❌ 중복된 GitHub 사용자 이름입니다.",
        description=f"`{git_username}`는 이미 사용 중인 GitHub 사용자 이름입니다. 다른 사용자 이름을 선택해주세요.",
        color=Color.orange()
    )
    embed.set_footer(text="🔎 더 많은 도움이 필요하신 경우, 관리자에게 문의해 주세요.")
    

    await send_message_auto_delete(interaction, embed)