from discord import Interaction, Embed, Color

from db.models import User
from utils.message_auto_delete import send_message_auto_delete
from schemas.commit_schema import CommitSchema
from .buttons.loadmore_button import LoadMoreButton


async def embed_emty_user(interaction: Interaction):
    embed = Embed(
        title="❌ 사용자를 찾을 수 없습니다.",
        description=f"{interaction.user.global_name}님의 정보를 확인할 수 없습니다. 먼저 사용자를 등록하여 주세요.",
        color=Color.red()
    )
    embed.set_footer(text="지속해서 문제가 있다면 관리자에게 문의해 주세요.")

    await send_message_auto_delete(interaction, embed)
    
async def embed_cannot_edit_while_deactivated(interaction: Interaction):
    embed = Embed(
        title="❌ 사용자가 비활성화 중입니다.",
        description=f"`{interaction.user.global_name}` 님은 현재 비활성화 상태에 있습니다. 비활성화 상태에서는 이용이 불가능합니다.",
        color=Color.red()
    )
    embed.add_field(name="기능 활성화하기", value="기능을 활성화하고 정보를 수정하고 싶으시면, 등록을 한번 더 진행해 주세요.", inline=False)
    embed.set_footer(text="🔎 더 많은 도움이 필요하신 경우, 관리자에게 문의해 주세요.")

    await send_message_auto_delete(interaction, embed)
    
async def embed_invalid_info(interaction: Interaction, user: User):
    embed = Embed(
        title="❌ GitHub 정보를 확인할 수 없습니다.",
        description="GitHub 사용자 이름이나 레포지토리를 찾을 수 없습니다. 사용자 이름과 레포지토리 이름이 정확한지 확인하고, 대소문자를 올바르게 입력했는지 확인해주세요.",
        color=Color.orange()
    )
    embed.add_field(name="사용자 정보", 
                    value=f"```user name:  {user.git_username}\nrepository name:  {user.repository_name}```",
                    inline=False)
    embed.set_footer(text="🔎 더 많은 도움이 필요하신 경우, 관리자에게 문의해 주세요.")

    await send_message_auto_delete(interaction, embed)
    
async def embed_no_commit_history(interaction: Interaction, user: User):
    embed = Embed(
        title="❌ 커밋 기록이 없습니다.",
        description="해당 GitHub 레포지토리에 커밋 기록이 없습니다. 레포지토리가 비어있는지 확인해주세요. 또한, 레포지토리 이름과 사용자 이름이 정확한지 다시 한 번 확인해주시기 바랍니다.",
        color=Color.orange()
    )
    embed.add_field(name="레포지토리 정보", 
                    value=f"```GitHub 사용자 이름:  {user.git_username}\n레포지토리 이름:  {user.repository_name}```",
                    inline=False)
    embed.set_footer(text="🔎 문제가 지속될 경우, 관리자에게 문의해 주세요.")

    await send_message_auto_delete(interaction, embed)
    
async def embed_commit_record(interaction: Interaction, user: User, commits: list[CommitSchema]):
    embeds = []
    for commit in commits[:10]:
        embed = Embed(
            title=f"{commit.message}",
            url=commit.url,
            description=f"작성자: `{commit.author}`\n"
                        f"날짜: `{commit.commit_date}`",
            color=Color.blue()
        )
        embed.set_author(name=user.git_username, url=f"https://github.com/{user.git_username}", icon_url=f"https://avatars.githubusercontent.com/{user.git_username}")
        embeds.append(embed)
    if len(commits) > 10:
        await send_message_auto_delete(interaction, embeds, view=LoadMoreButton(commits[10:], user))
    else:
        await send_message_auto_delete(interaction, embeds)
