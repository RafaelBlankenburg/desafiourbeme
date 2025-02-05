# desafiourbeme
Para resolver o problema proposto eu optei por utilizar o framework de python Django em conjunto dele mais duas bibliotecas a beautifulsoup4 e a requests. Se você não possuir elas instaladas basta utilizar os comandos (para windows):

 py -m ensurepip --upgrade (instala o pip)
 pip install requests beautifulsoup4 (instala as duas bibliotecas necessárias)

Com a stack escolhida agora é possível partir para a solução. Para pesquisar se um código de fundo existe mesmo eu preferi criar um pequeno banco de dados, assim era possível o usuário conseguir o resultado desejado sem se preocupar em precisar escrever o código completo do fundo. Ainda assim a única informação guardada nesse banco seriam os códigos existentes, outros indicadores, como o valor em caixa são muito variáveis, então eu pego eles do site apenas na hora da consulta.
Para fazer a varredura de códigos é preciso executar esse comando no terminal:

 python scrape_fundos.py

Só será necessário executar a varredura novamente quando novos fundos forem adicionados, ou houver atualizações de códigos.

Sabendo quais são os fundos existentes é só fazer uma varredura no site após a pesquisa do usuário. Os parâmetros mostrados são: Valor em Caixa, Liquidez média diária, Val. Patrimonial p/Cota, e N° de Cotistas.

Para executar o programa basta rodar o comando: 
 python manage.py runserver

Entrar na url disponiblizada no terminal e então adicionar o termo de pesquisa.