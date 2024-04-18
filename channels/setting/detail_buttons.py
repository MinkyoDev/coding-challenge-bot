import discord
import logging

from . import setting_embeds


class DetailButton(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
 
    # @discord.ui.button(label='챌린지 등록', style=discord.ButtonStyle.green, row=1)
    # async def challenge_registration(self, interaction: discord.Interaction, button: discord.ui.Button):
    #     logging.info(f"Register button pressed by: {interaction.user} (ID: {interaction.user.id})")

    #     await setting_embeds.embed_emty_user(interaction)

    # @discord.ui.button(label='정보수정', style=discord.ButtonStyle.secondary, row=1)
    # async def modification(self, interaction: discord.Interaction, button: discord.ui.Button):
    #     logging.info(f"Register button pressed by: {interaction.user} (ID: {interaction.user.id})")

    #     await setting_embeds.embed_emty_user(interaction)

    # @discord.ui.button(label='챌린지 비활성화', style=discord.ButtonStyle.danger, row=1)
    # async def deactivate(self, interaction: discord.Interaction, button: discord.ui.Button):
    #     logging.info(f"Register button pressed by: {interaction.user} (ID: {interaction.user.id})")

    #     await setting_embeds.embed_emty_user(interaction)

    @discord.ui.button(label='챌린지 목표 수정', style=discord.ButtonStyle.primary, row=2)
    async def edit_goal(self, interaction: discord.Interaction, button: discord.ui.Button):
        logging.info(f"Register button pressed by: {interaction.user} (ID: {interaction.user.id})")

        await setting_embeds.embed_emty_user(interaction)

    @discord.ui.button(label='잔디 알림이 활성화', style=discord.ButtonStyle.green, row=3)
    async def grass_notification_activate(self, interaction: discord.Interaction, button: discord.ui.Button):
        logging.info(f"Register button pressed by: {interaction.user} (ID: {interaction.user.id})")

        await setting_embeds.embed_emty_user(interaction)

    @discord.ui.button(label='잔디 알림이 비활성화', style=discord.ButtonStyle.danger, row=3)
    async def grass_notification_deactivate(self, interaction: discord.Interaction, button: discord.ui.Button):
        logging.info(f"Register button pressed by: {interaction.user} (ID: {interaction.user.id})")

        await setting_embeds.embed_emty_user(interaction)

    @discord.ui.button(label='출퇴실 알림이 활성화', style=discord.ButtonStyle.green, row=4)
    async def Check_in_out_notification_activate(self, interaction: discord.Interaction, button: discord.ui.Button):
        logging.info(f"Register button pressed by: {interaction.user} (ID: {interaction.user.id})")

        await setting_embeds.embed_emty_user(interaction)

    @discord.ui.button(label='출퇴실 알림이 비활성화', style=discord.ButtonStyle.danger, row=4)
    async def Check_in_out_notification_deactivate(self, interaction: discord.Interaction, button: discord.ui.Button):
        logging.info(f"Register button pressed by: {interaction.user} (ID: {interaction.user.id})")

        await setting_embeds.embed_emty_user(interaction)