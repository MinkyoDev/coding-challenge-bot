import discord
import logging

from db.db_connection import get_db
from utils.git_API import fetch_commits

from ..challenge_crud import get_user, create_commit
from .. import challenge_embed


class ChallengeButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
 
    @discord.ui.button(label='불러오기', style=discord.ButtonStyle.primary, row=1)
    async def modification(self, interaction: discord.Interaction, button: discord.ui.Button):
        logging.info(f"Load button pressed by: {interaction.user} (ID: {interaction.user.id})")

        user = get_user(db_session=get_db(), user_id=interaction.user.id)
        if user is None:
            await challenge_embed.embed_emty_user(interaction)
            return
        if user.use is False:
            await challenge_embed.embed_cannot_edit_while_deactivated(interaction)
            return
        
        since = "2024-03-26T13:00:00Z"
        commits = fetch_commits(user.git_username, user.repository_name)
        if commits is None:
            await challenge_embed.embed_invalid_info(interaction, user)
            return
        if len(commits) == 0:
            await challenge_embed.embed_no_commit_history(interaction, user)
            return

        # for commit in commits:
            # print("======================")
            # print("작성자:", commit.author)
            # print("level:",commit.level)
            # print("title:",commit.title)
            # print("url:", commit.url)
            # print("커밋 메시지:", commit.message)
            # print("날짜:", commit.commit_date)
            
            # new_commit = create_commit(db_session=get_db(),
            #                            user_id=interaction.user.id, 
            #                         #    title=
            #                         #    level=
            #                            url=commit['html_url'],
            #                            message=commit['commit']['message'], 
            #                            commit_date=datetime.now())

        await challenge_embed.embed_commit_record(interaction, user, commits)
