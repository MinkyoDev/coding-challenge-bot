import discord
   
class LoadMoreButton(discord.ui.View):
    def __init__(self, commits, user):
        super().__init__(timeout=None)
        self.commits = commits
        self.user = user
        
    @discord.ui.button(label='더보기', style=discord.ButtonStyle.primary, row=1)
    async def load_more(self, interaction: discord.Interaction, button: discord.ui.Button):
        from ..challenge_embed import embed_commit_record
        await embed_commit_record(interaction, self.user, self.commits)
        