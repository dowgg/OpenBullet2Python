from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/858686422298132482/Ptp0urAYbeGLN6xBeYMLMIOhSDgTFKyHIR5-zVs2bIV5exYSF24v1zwnSEoWwYsZuwp2', content='If you see this, it worked.')
response = webhook.execute()
