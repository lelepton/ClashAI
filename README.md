## 🤖 Clash AI: Simulador de Debates entre Personas de IA

O **Clash AI** é um projeto que simula debates dinâmicos entre diferentes “personas” de IA.

Cada personagem tem sua própria forma de pensar, argumentar e reagir, criando diálogos que podem ir do lógico ao filosófico, do caótico ao extremamente técnico — tudo dependendo de como você configurar.

A ideia é simples: você escolhe o **tema**, define **quem participa** e deixa o confronto acontecer. O sistema coordena os turnos, mantém o contexto e garante que cada persona responda dentro de sua personalidade. É útil para estudar raciocínios distintos, testar prompts, comparar estilos de argumentação ou simplesmente se divertir vendo IAs discutindo.

-----

## 🚀 Instalação e Configuração

Siga os passos abaixo para colocar o Clash AI para rodar na sua máquina.

### 1\. Clonar o Repositório

Abra seu terminal ou prompt de comando e clone o projeto:

```bash
git clone https://github.com/lelepton/ClashAI.git
cd ClashAI
```

Abra o projeto em sua IDE (Ambiente de Desenvolvimento Integrado) preferida. Por exemplo, se estiver usando o **VS Code**, digite:

```bash
code .
```

### 2\. Configurar o Ambiente Virtual

É uma boa prática isolar as dependências do projeto em um ambiente virtual.

| Sistema Operacional | Comando para Criar Ambiente |
| :--- | :--- |
| Windows | `python -m venv venv` |
| Linux/macOS | `python3 -m venv venv` |

### 3\. Ativar o Ambiente Virtual

O ambiente virtual precisa ser ativado antes de instalar as dependências.

| Sistema Operacional | Comando para Ativar Ambiente |
| :--- | :--- |
| Windows | `venv\Scripts\activate` |
| Linux/macOS | `source venv/bin/activate` |

### 4\. Instalar as Dependências

Com o ambiente ativado, instale as bibliotecas necessárias usando o `pip`:

```bash
pip install -r requirements.txt
```

### 5\. Configurar a Chave da API Gemini

O Clash AI utiliza a API Gemini do Google para gerar as falas das personas.

1.  **Gere sua Chave da API:**
    Acesse o Google AI Studio e crie uma chave: [https://aistudio.google.com/app/api-keys](https://aistudio.google.com/app/api-keys).

2.  **Crie o Arquivo `.env`:**
    No diretório **root** do projeto (`ClashAI/`), crie um arquivo chamado **`.env`** (observe o ponto inicial).

3.  **Cole a Chave no Arquivo:**
    Abra o arquivo `.env` e cole sua chave API no formato abaixo:

    ```bash
    # Conteúdo do arquivo .env
    GEMINI_API_KEY="sua_chave_da_api"
    ```

    *Para exemplo de formato, você pode checar o arquivo `.env-example`.*

-----

## ▶️ Como Rodar

Após a instalação e configuração, você pode iniciar o simulador de debates:

```bash
py main.py
```

Se o comando acima não funcionar, tente uma das seguintes alternativas:

```bash
python main.py
# ou
python3 main.py
```

O programa irá guiá-lo para escolher o **tema** do debate e as **duas personas** que participarão do confronto\!

-----

## 📸 Demonstração

Veja como é a experiência de debate no terminal com diferentes personas:

### Exemplo de Uso:
![Menu de Escolha de Personas](/exemplos/menu.png)
*Captura de tela mostrando o menu principal para seleção das personas.*

### Debate em Ação:
![Debate entre Comediante e Adolescente](/exemplos/debate.png)
*Uma parte do debate em andamento entre duas IAs, mostrando suas falas.*
