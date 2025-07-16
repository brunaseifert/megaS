# Gerador Inteligente de números aleatórios de aposta

Esse projeto é um gerador de números aleatórios que geralmente mais saem e menos saem em apostas como na mega sena. Com inteligência estatística, utilizando dados reais de frequência dos números sorteados. A lógica mistura números mais (quentes) e menos (frios) com pesos personalizados, gerando apostas estratégicas com números aleatórios

## Funcionalidades

- Geração de apostas aleatórias sem repetições
- Baseada em estatísticas da Mega-Sena
- Mistura inteligente de números mais e menos sorteados
- Saída ordenada e legível no terminal
- Versão executável .exe 

## Tecnologias

- **Python 3**
- Módulo `random`

## Como usar

1. Clone o repositório:
    ```bash
    git clone https://github.com/brunaseifery/megaS-generator.git
    cd megaS-generator
    ```

2. Execute o script:
    ```bash
    python megaS.py
    ```

3. Veja as apostas geradas.

## Como fazer em .exe

1. Instale o pyinstaller no bash: pip install pyinstaller

2. Gere o .exe: pyinstaller --onefile --windowed megaS.py

3. O .exe estará na pasta dist.

## Estatísticas usadas

- **Mais**: 10, 53, 5, 34, 37, 33, 38, 17, 32, 43
- **Menos**: 26, 21, 55
- Pesos aplicados conforme frequência real de sorteios

## Licença

Código aberto para fins educacionais e recreativos. Contribuições são bem-vindas!

Projeto desenvolvido por **Bruna Seifert**
