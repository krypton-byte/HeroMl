import difflib, requests
getInfoHero = lambda _namaHero:requests.get("https://mapi.mobilelegends.com/hero/detail", params={"id":list(filter(lambda x: x if x.get("name")==nameHerox[0] else None, JsonHero))[0].get("heroid")}).json() if (nameHerox:=difflib.get_close_matches( _namaHero,list(map(lambda x:x.get("name"), (JsonHero:=requests.get("https://mapi.mobilelegends.com/hero/list").json().get("data")))), n=1)) else {}
