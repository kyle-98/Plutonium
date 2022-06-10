import requests
import re

url = "https://plutonium.pw/api/servers"
response = requests.get(url)
data = response.json()

serverList = []
for d in data:
    if d["game"] == "iw5mp" and len(d["players"]) >= 10:
        sN = d['hostname']
        playersList = []
        newSN = re.sub('\^[0-9]{1}', '', sN)
        for i in range(len(d['players'])):
            playersList.append({d['players'][i]['username']})
        server = []
        server.append(newSN)
        server.append(len(d['players']))
        server.append(playersList)
        
        serverList.append(server) 

for s in serverList:
    print(f"""Server Name: {s[0]}
    Player Count: {s[1]}
    Players:""")
    for i in range(len(s[2])):
        namesList = list(s[2][i])
        for j in range(len(namesList)):
            print(f"\t{namesList[j]}")
    print("\n")