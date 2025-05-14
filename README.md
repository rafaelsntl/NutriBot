# NutriBot – Assistente Nutricional para Veganos

**NutriBot** é um assistente virtual de nutrição que gera planos alimentares completos (café da manhã, almoço, lanche da tarde e jantar) para pessoas veganas com base nos alimentos disponíveis. O chatbot utiliza o modelo **Meta-LLaMA 3 8B Instruct** da Hugging Face via API para oferecer sugestões personalizadas de forma leve e eficiente.

## Funcionalidades:

- Sugere planos alimentares completos para o dia
- Utiliza apenas os alimentos fornecidos pelo usuário
- Evita repetir refeições
- Indica as calorias de cada refeição (quando solicitado)
- Usa linguagem simples e direta
- Código leve, replicável e sem necessidade de hardware avançado

## Como usar:

1. Instale as dependências:  `pip install -r requirements.txt`
2.  Crie o arquivo `alimentos.txt` com os alimentos disponíveis (separados por vírgula)
3. Execute:  `python nutribot.py`

## Exemplo de utilização:
Você: Sou vegano e quero ganhar massa
*O NutriBot retorna um cardápio completo usando os alimentos fornecidos.*
