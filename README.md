# Sentiment-Analysis
 
Manual de Uso do Código de Análise de Sentimento
Requisitos Prévios

    Certifique-se de que você tem o Python instalado em seu sistema. Você pode baixar o Python em python.org.

Passos para Executar o Código

    Baixe o código: Faça o download do código Python para análise de sentimentos, ou copie-o diretamente do nosso chat.

    Instale as Bibliotecas Necessárias:

    Abra um terminal ou prompt de comando e execute o seguinte comando para instalar as bibliotecas necessárias (NLTK e Matplotlib):

    bash

    pip install nltk matplotlib

    Execute o Código:
        Abra um terminal ou prompt de comando.
        Navegue até o diretório onde você salvou o código.
        Execute o código com o comando python nome_do_arquivo.py (substitua nome_do_arquivo.py pelo nome do arquivo onde você salvou o código).

    Forneça um Texto para Análise:

    O programa solicitará que você insira o texto que deseja analisar. Você pode simplesmente copiar e colar um texto de sua escolha ou pressionar Enter para usar o texto de exemplo fornecido.

    Visualização dos Resultados:

        O código exibirá os resultados da análise de sentimentos, incluindo a pontuação de sentimento, palavras-chave principais e um resumo das primeiras duas frases.

        Você será perguntado se deseja mostrar um gráfico de barras que representa a distribuição do sentimento no texto. Digite "sim" para ver o gráfico ou "não" para ignorar.

    Armazenamento Opcional de Resultados:
        Os resultados da análise (pontuação de sentimento, palavras-chave e resumo) serão armazenados em um banco de dados SQLite chamado "analysis_results.db" no mesmo diretório do código. Você pode acessar esses resultados posteriormente.

    Fim da Execução:

    Após a exibição dos resultados, o programa terminará.

Visualização dos Resultados

    Após a execução do código, você verá a pontuação de sentimento (negativa, neutra, positiva e composta) do texto fornecido.

    As palavras-chave principais (top 5) identificadas no texto serão exibidas.

    Um resumo automático das duas primeiras frases do texto também será apresentado.

    Se você optar por mostrar o gráfico de barras, um gráfico será exibido com a distribuição do sentimento no texto. O gráfico terá quatro barras representando sentimentos negativos, neutros, positivos e uma pontuação composta.

    Os resultados da análise de sentimentos e outros dados, como palavras-chave e resumo, serão armazenados em um banco de dados SQLite chamado "analysis_results.db" no mesmo diretório do código. Você pode acessar e consultar esses resultados posteriormente.
