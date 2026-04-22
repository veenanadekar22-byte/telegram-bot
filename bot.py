import asyncio
import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from config import BOT_TOKEN, ADMIN_ID, CATEGORIES, MOTIVATION_QUOTES, get_youtube_url
from utils import USERS, logger

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome = """
🚀 Welcome to Freelance Skill Hub! 🚀

Learn high-income freelancing skills for FREE and start earning online.

Choose a category:
    """
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎨 Graphic Design", callback_data="category_graphic"), InlineKeyboardButton("💻 Web Development", callback_data="category_webdev")],
        [InlineKeyboardButton("🎬 Video Editing
