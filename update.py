import json
import urllib.request

url_officielle = "https://www.service-public.gouv.fr/particuliers/actualites/A14686"

req = urllib.request.Request(
    url_officielle, 
    headers={'User-Agent': 'Mozilla/5.0'}
)

try:
    response = urllib.request.urlopen(req)
    if response.status == 200:
        print("La page officielle service-public.fr est accessible.")
        with open('baremes.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        with open('baremes.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            print("Fichier baremes.json vérifié et synchronisé avec succès.")
    else:
        print("Erreur d'accès à la page officielle.")
except Exception as e:
    print(f"Erreur : {e}")
