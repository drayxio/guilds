from requests import get, post

account_type = input("account type (bot, user) > ")
token = input("token > ")
guild_id = input("guild id > ")


print("L'invitation est entrain de se générer...")

if account_type == "bot":
    auth = {"authorization": "Bot "+token}
elif account_type == "user":
    auth = {"authorization": token}
else:
    exit()

url = "https://discord.com/api"

try: invite = get(f"{url}/guilds/{guild_id}/invites", headers=auth).json()[0].get("code")
except:

    for channel in get(f"{url}/guilds/{guild_id}/channels", headers=auth).json():
        try:
            invite = post(f"{url}/channels/{channel.get('id')}/invites", headers=auth, json={}).json().get("code")
            try:
                " " + invite
                break
            except:
                invite = None
        except:
            invite = None

    if invite:

        input("Invite code generated - " + str(invite))
    else:
        input("Can't have an invite code :'(")
