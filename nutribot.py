# Importa o cliente de inferência da Hugging Face
from huggingface_hub import InferenceClient

# Inicializa o cliente com o modelo LLaMA 3 8B Instruct via API
client = InferenceClient(
    model="meta-llama/Meta-Llama-3-8B-Instruct",
    token="SeuToken"  # Substitua aqui pelo seu token real
)

# Função para carregar os alimentos disponíveis de um arquivo
def carregar_alimentos():
    try:
        with open("alimentos.txt", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        # Se o arquivo não existir, retorna alimentos padrão
        return "banana, arroz, aveia, lentilha, tofu, espinafre, abacate"

# Cria as mensagens no formato usado por modelos de chat (chat template)
def criar_mensagem(pergunta_usuario):
    alimentos = carregar_alimentos()
    return [
        {
            "role": "system",
            "content": "Você é um nutricionista virtual que ajuda pessoas veganas a planejar refeições."
        },
        {
            "role": "user",
            "content": (
                f"Crie um plano alimentar de acordo com o que for pedido pelo usuário.\n"
                f"Use apenas os alimentos disponíveis: {alimentos}.\n"
                f"Inclua café da manhã, almoço, lanche da tarde e jantar.\n"
                f"Mostre as calorias que vão ser consumidas em cada refeição.\n"
                f"Evite repetir refeições. Use alimentos mais simples e baratos."
            )
        }
    ]

# Função principal que envia a pergunta ao modelo e retorna a resposta
def conversar(pergunta_usuario):
    mensagens = criar_mensagem(pergunta_usuario)
    print("NutriBot está pensando...")
    try:
        # Chama a API do modelo como se fosse um chat (formato openAI-like)
        resposta = client.chat_completion(messages=mensagens)
        return resposta.choices[0].message["content"]
    except Exception as e:
        return f"Erro ao gerar resposta: {e}"

# Loop principal da aplicação
if __name__ == "__main__":
    print("Olá! Sou o NutriBot. Como posso te ajudar com sua alimentação hoje?")
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            print("NutriBot: Até mais! 💚")
            break
        resposta = conversar(pergunta)
        print("\nNutriBot:", resposta)
