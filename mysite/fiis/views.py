from django.shortcuts import render
from fiis.models import FundoImobiliario
import requests
from bs4 import BeautifulSoup

def home(request):
    query = request.GET.get('q', '').strip()
    fundo = None
    if query:
        fundo = FundoImobiliario.objects.filter(codigo__iexact=query).first() or \
                FundoImobiliario.objects.filter(codigo__icontains=query).first()
        url = f"https://fiis.com.br/{fundo.codigo.lower()}/"
        headers = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
           soup = BeautifulSoup(response.text, 'html.parser')

        indicators = soup.find_all('div', class_='indicators__box')


        data = {}

        for indicator in indicators:
            value = indicator.find('b').text.strip()  
            label = indicator.find_all('p')[1].text.strip()  
            data[label] = value  

    context = {
        'query': query,
        'fundo': fundo,
    }
    return render(request, 'fiis/home.html', context)

def result(request):
    query = request.GET.get('q', '').strip()
    fundo = None
    data = {}

    if query:
        fundo = FundoImobiliario.objects.filter(codigo__iexact=query).first() or \
                FundoImobiliario.objects.filter(codigo__icontains=query).first()
        
        if fundo:
            url = f"https://fiis.com.br/{fundo.codigo.lower()}/"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                indicators = soup.find_all('div', class_='indicators__box')

                for indicator in indicators:
                    value = indicator.find('b').text.strip()  
                    label = indicator.find_all('p')[1].text.strip()  
                    data[label] = value  

    context = {
        'query': query,
        'fundo': fundo,
        'valor_em_caixa': data.get('Valor em caixa'),
        'liquidez_media_diaria': data.get('Liquidez média diária'),
        'val_patrimonial_p_cota': data.get('Val. Patrimonial p/Cota'),
        'numero_de_cotistas': data.get('N° de Cotistas'),
    }
    return render(request, 'fiis/result.html', context)
