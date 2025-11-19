from api import gerar_fala # importamos a função geradora de falas das IAs
from personas import PERSONAS # importamos o dicionário de personas disponíveis

def menu():
    '''função que apenas exibe o menu de personas disponíveis'''

    print('\nPersonas disponíveis no sistema:\n')
    print('+----+---------------------+----+---------------------+')
    print('| Nº | Persona             | Nº | Persona             |')
    print('+----+---------------------+----+---------------------+')
    print('|  1 | Cientista           | 13 | Futurista           |')
    print('|  2 | Filósofo            | 14 | Historiador         |')
    print('|  3 | Cético              | 15 | Diplomata           |')
    print('|  4 | Otimista            | 16 | Rebelde             |')
    print('|  5 | Pessimista          | 17 | Minimalista         |')
    print('|  6 | Comediante          | 18 | Espirituoso         |')
    print('|  7 | Advogado            | 19 | Conspiracionista    |')
    print('|  8 | Poeta               | 20 | Niilista            |')
    print('|  9 | General             | 21 | Romântico           |')
    print('| 10 | Professor           | 22 | Analista            |')
    print('| 11 | Troll               | 23 | Coach               |')
    print('| 12 | Monge               | 24 | Adolescente         |')
    print('+----+---------------------+----+---------------------+\n')

def escolher_personas():
    '''função que permite ao usuário escolher as personas das IAs'''

    menu() # exibimos primeiro o menu, para que o usuário saiba as opções disponíveis

    lista_personas = list(PERSONAS.keys()) # criamos uma lista com as chaves do dicionário de personas

    while True: # loop que garante que o usuário escolhe duas personas válidas
        try:
            p1 = int(input("Escolha a persona da primeira IA (número): ")) # pedimos pra o usuário escolher as duas personas
            p2 = int(input("Escolha a persona da segunda IA (número): ")) # e convertemos as duas pra int já que devem ser números

            persona1 = lista_personas[p1 - 1] # subtraímos 1 porque a lista começa do 0
            persona2 = lista_personas[p2 - 1] # fazemos o mesmo pra a segunda persona

            return persona1, persona2 # retornamos as duas personas escolhidas
        
        except (ValueError, IndexError): # tratamos erros de conversão e índices inválidos
            print("Número inválido. Tente novamente.") # imprimimos uma mensagem de erro e o loop recomeça

def configs():
    '''função que configura o tema e as personas do debate'''

    tema = input('Antes de tudo, preciso saber: qual tema deverá ser debatido? ')

    if not tema:
        print('Por favor, digite algum tema para ser debatido!')
        return None, None, None # retornamos None para indicar que o tema não foi fornecido
    
    print(f'Perfeito! Você escolheu o tema "{tema}".') # mostramos o tema que foi selecionado
    confirm = input('Gostaria de prosseguir com esse tema? (s/n) ').lower() # pedimos confirmação do tema
    if confirm != 's': # se o usuário não confirmar, então o programa é reiniciado
        print('Reiniciando o programa...')
        return None, None, None # retornamos None para indicar que o tema não foi confirmado

    print('Agora, preciso que você escolha as personas que as IAs interpretarão!') # pedimos para o usuário escolher as personas das IAs
    persona1, persona2 = escolher_personas() # a função escolher_personas() é chamada e ela retorna as duas personas escolhidas

    print(f'Ótimo! A primeira IA será um(a) {persona1} e a segunda IA será um(a) {persona2}.') # mostramos as personas escolhidas

    return tema, persona1, persona2 # retornamos o tema e as personas escolhidas

def debate_loop():
    '''função que executa o loop do debate entre as duas IAs'''

    tema, persona1, persona2 = configs() # chamamos a função de configuração para termos o tema e as personas, e depois armazenamos em variáveis
    if not tema:
        return # se o tema não for válido, retornamos para o programa principal

    mensagem_atual = f"Iniciando debate sobre: {tema}" # a mensagem inicial do debate

    continuar = True # criamos uma variável de controle para o loop de debate, ou seja, é com ela que saberemos se o debate deve continuar ou não
    while continuar:
        resposta1 = gerar_fala(persona1, mensagem_atual) # geramos a fala da primeira IA com base na mensagem atual
        print(f"\n{persona1.capitalize()}: {resposta1}\n") # imprimimos a fala c/ o formato de PERSONA: fala

        resposta2 = gerar_fala(persona2, resposta1) # geramos a fala da segunda IA com base na fala da primeira IA!
        print(f"\n{persona2.capitalize()}: {resposta2}\n")

        mensagem_atual = resposta2 # atualizamos a mensagem atual para a próxima rodada do debate

        user_choice = input("Deseja continuar o debate? (s/n) ").lower() # perguntamos ao usuário se deseja continuar ou não
        if user_choice != 's':
            continuar = False # se o usuário não quiser continuar, alteramos a variável de controle para False e o loop termina
            print("Debate encerrado. Até a próxima!")

# aqui começa o programa principal, c/ as boas-vindas e a chamada da função de debate
print('Bem-vindo(a) ao ClashAI: um simulador de debates entre IAs com personalidades diferentes!')
print('Aqui você poderá escolher o tema a ser debatido e as personas que as duas IAs interpretarão.')
init = input('Pronto para começar? (s/n) ').lower() # perguntamos se o usuário quer começar o debate

if init == 's':
    debate_loop() # se ele quiser, chamamos a função que executa o loop do debate
else:
    print('Eita :( Que pena! Até a próxima!') # se não quiser, apenas encerramos o programa c/ uma mensagem de despedida
