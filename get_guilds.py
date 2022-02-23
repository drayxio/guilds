from requests import get

open("guilds.txt", mode="w")
file = open(file="guilds.txt", mode="a", encoding="UTF-8")

account_type = input("account type (bot, user) > ")
token = input("token > ")


print("Les infomations sont entrain d'être récolté patientez...")

if account_type == "bot":
    auth = {"authorization": "Bot "+token}
elif account_type == "user":
    auth = {"authorization": token}
else:
    exit()

url = "https://discord.com/api"

me = get(f"{url}/users/@me", headers=auth).json()

with_invite = ""
no_invite = ""
with_perm = ""

servers = get(f"{url}/users/@me/guilds", headers=auth).json()

for server in servers:

    members = get(f"{url}/guilds/{server.get('id')}?with_counts=true", headers=auth).json().get("approximate_member_count")

    try: with_invite = with_invite + "  " + get(f"{url}/guilds/{server.get('id')}/invites", headers=auth).json()[0].get("code") + " : " + server.get("id") + " - " + server.get("name") + " - " + str(members) + "members" + "\n"
    except: no_invite = no_invite + "   nothing" + " : " + server.get("id") + " - " + server.get("name") + " - " + str(members) + " members " + "\n"

file.write("Serveur avec invitation : \n" + with_invite)
file.write("------\n")
file.write("Serveur sans invitation : \n" + no_invite)
file.write("------\n")

file.close()

input("Fini !")