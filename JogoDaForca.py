from random import choice
from unidecode import unidecode

vidas = 7

with open('palavras.txt', 'r') as arquivo:
    conteudoPalavras = arquivo.read()
    palavras = conteudoPalavras.split(',')

palavra = choice(palavras)
palavra = palavra.strip()
tamanhoPalavra = len(palavra)
formatoForca = "_" * tamanhoPalavra
nomePalavra = palavra
palavra = unidecode(palavra)
letrasErradas = set()

while vidas > -1:
    letraInput = input('Escolha uma letra: ')

    if len(letraInput) > 1:
        print('Escolha APENAS uma letra. ')
    else: 
        if letraInput in palavra or letraInput.upper() in palavra:
            print('Acertou')

            for indicePalavra, caracterePalavra in enumerate(palavra):
                if caracterePalavra == letraInput or caracterePalavra == letraInput.upper():
                    formatoForca = formatoForca[:indicePalavra] + nomePalavra[indicePalavra] + formatoForca[indicePalavra + 1:]

            if formatoForca[0] == letraInput.lower():
                formatoForca = formatoForca[:0] + letraInput.upper() + formatoForca[0 +1:]
                print(formatoForca)
            else:
                print(formatoForca)
        else:
            vidas = vidas - 1
            print(f'Errou! {vidas} vidas restantes')
            print(formatoForca)

            if letraInput not in palavra:
                letrasErradas.add(letraInput)
                print( "Já foram: " + ', '.join(letrasErradas))

        if formatoForca == nomePalavra:
            print('Você ganhou!')
            break

        if vidas == 0:
            print('Acabaram suas vidas. Você perdeu!')
            print(f'A palavra era: {nomePalavra}')
            break
