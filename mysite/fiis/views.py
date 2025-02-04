from django.shortcuts import render

import requests
from bs4 import BeautifulSoup

def get_valor_em_caixa(codigo_fundo):
    """
    Dada uma string com o código do fundo, retorna o valor em caixa extraído do site.
    """
    url = f"https://fiis.com.br/{codigo_fundo.lower()}/"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/90.0.4430.93 Safari/537.36"
        )
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Erro ao acessar a URL: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    label = soup.find(lambda tag: tag.name in ["span", "div", "li"] and "Valor em caixa" in tag.get_text())
    
    if not label:
        return None

    valor_elemento = label.find_next(string=True)
    if valor_elemento:
        return valor_elemento.strip()
    
    texto_completo = label.get_text(separator=" ").strip()
    partes = texto_completo.split("Valor em caixa")
    if len(partes) > 1:
        return partes[1].strip()

    return None

from django.shortcuts import render
from .models import FundoImobiliario

def home(request):
    query = request.GET.get('q', '').strip()
    fundo = None
    if query:
        fundo = FundoImobiliario.objects.filter(codigo__iexact=query).first() or \
                FundoImobiliario.objects.filter(codigo__icontains=query).first()

    context = {
        'query': query,
        'fundo': fundo,
    }
    return render(request, 'fiis/home.html', context)

