import os
import django
import requests
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')  
django.setup()

from fiis.models import FundoImobiliario

def scrape_fundos():
    url = "https://fiis.com.br/lista-de-fundos-imobiliarios/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        titulos = soup.find_all('div', class_='tickerBox__title')
        
        if titulos:
            for titulo in titulos:
                codigo = titulo.text.strip()
                if not FundoImobiliario.objects.filter(codigo=codigo).exists():
                    FundoImobiliario.objects.create(codigo=codigo)
                    print(f"Adicionado: {codigo}")
        else:
            print("Tabela não encontrada.")
    else:
        print(f"Erro ao acessar o site: {response.status_code}")

if __name__ == "__main__":
    scrape_fundos()