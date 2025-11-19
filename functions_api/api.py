import os # importamos o módulo os para acessar variáveis de ambiente
from functions_api.personas import PERSONAS # importamos o dicionário de personas
from google import genai # importamos a biblioteca genai da Google Gemini
from dotenv import load_dotenv # importamos a função para carregar variáveis de ambiente

load_dotenv() # carrega as variáveis de ambiente do arquivo .env

API_KEY = os.getenv("GEMINI_API_KEY") # carregamos a chave da API a partir do .env

client = genai.Client(api_key=API_KEY) # inicializamos o cliente baseado na chave da API

def gerar_fala(persona, mensagem):
    '''função que gera uma fala baseada na persona escolhida e na mensagem recebida'''

    persona_key = persona.lower() # garante que a chave da persona esteja em minúsculas
    if persona_key not in PERSONAS: # se não tiver no dict de personas, retorna erro
        return f"Persona '{persona}' não encontrada."
    
    system_prompt = PERSONAS[persona_key] # obtém a instrução do sistema baseada na persona escolhida

    config = genai.types.GenerateContentConfig( # cria a configuração de geração de conteúdo
        system_instruction=system_prompt
    )

    contents = mensagem # a mensagem que o usuário enviou

    try:
        response = client.models.generate_content( # chamamos o método de geração de conteúdo aqui
            model="gemini-2.5-flash", # modelo escolhido da Google Gemini
            contents=contents, # passando a mensagem do usuário
            config=config      # passa a instrução do sistema, ou seja, a persona escolhida
        )
        return response.text.strip() # retorna a resposta gerada pela IA, removendo espaços extras
    except Exception as e: # captura todos os erros possíveis e retorna uma mensagem
        return f"Erro ao gerar resposta Gemini: {e}"
    