"""
    ATENÇÃO – CÓDIGO EDUCACIONAL (NÃO UTILIZAR EM PRODUÇÃO)

    Este código foi desenvolvido exclusivamente para fins didáticos,
    no contexto da disciplina Tecnologias e Programação Integrada.

    O objetivo é demonstrar o uso de LLMs/SLMs com tool calling, permitindo
    que um modelo de linguagem decida qual função Python executar a
    partir de uma entrada em linguagem natural.

    IMPORTANTE:
    - Este código NÃO possui guardrails de segurança.
    - Não há validação robusta de entrada.
    - Não há controle de permissões ou autenticação.
    - Não há proteção contra uso indevido, chamadas indevidas ou escrita não autorizada.
    - NÃO deve ser executado em ambientes de produção.

    Antes de qualquer uso real, seria necessário implementar:
    - Validações de entrada
    - Controle de acesso
    - Limitação de escopo das tools
    - Logs, auditoria e monitoramento
    - Tratamento de erros e exceções
    - Políticas de segurança e compliance

    Autor: Prof. Victor

"""
import os
import numpy as np
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader


load_dotenv()

client = Groq()
modelo = SentenceTransformer("all-MiniLM-L6-v2")


def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# =====================================================
# EXEMPLO 1 — RAG COM DOCUMENTOS NO CÓDIGO
# =====================================================

def exemplo1():

    print("\nEXEMPLO 1 — RAG com dados no código\n")

    documentos = [
        "A devolução pode ser feita em até 7 dias após a compra.",
        "A garantia dos produtos é de 1 ano.",
        "O suporte funciona de segunda a sexta das 8h às 18h."
    ]

    emb_docs = modelo.encode(documentos)
    pergunta = input("Pergunta: ")
    emb_q = modelo.encode(pergunta)
    scores = []

    for i, emb in enumerate(emb_docs):
        s = cosine(emb_q, emb)
        scores.append((s, documentos[i]))

    scores.sort(reverse=True)
    contexto = scores[0][1]
    print("\nDocumento encontrado:\n", contexto)
    prompt = f"""
        Você é um assistente que responde perguntas utilizando exclusivamente o contexto fornecido.

        Regras importantes:
            - Responda apenas com base nas informações presentes no contexto.
            - Não utilize conhecimento externo.
            - Caso a resposta não esteja claramente presente no contexto, responda: "Não encontrei essa informação no contexto fornecido."
            - Seja objetivo e claro na resposta.
            - NÃO mostre seu raciocínio interno.
            - Retorne apenas a resposta final.
        Idioma:
            - Responda obrigatoriamente em português do Brasil (pt-BR).

        Contexto:
        {contexto}

        Pergunta:
        {pergunta}

        Resposta:
    """

    r = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[{"role": "user", "content": prompt}]
    )

    print("\nResposta:\n", r.choices[0].message.content)


# =====================================================
# EXEMPLO 2 — RAG COM TXT
# =====================================================

def exemplo2():

    print("\nEXEMPLO 2 — RAG com arquivos TXT\n")
    docs = []

    for f in os.listdir("docs"):
        if f.endswith(".txt"):
            with open("docs/" + f, encoding="utf-8") as file:
                docs.append(file.read())

    emb_docs = modelo.encode(docs)
    pergunta = input("Pergunta: ")
    emb_q = modelo.encode(pergunta)
    scores = []

    for i, emb in enumerate(emb_docs):
        s = cosine(emb_q, emb)
        scores.append((s, docs[i]))

    scores.sort(reverse=True)
    contexto = scores[0][1]
    print("\nDocumento encontrado:\n", contexto[:300])
    


# =====================================================
# EXEMPLO 3 — RAG COM PDF
# =====================================================

def exemplo3():

    print("\nEXEMPLO 3 — RAG com PDF\n")
    reader = PdfReader("docs/manual.pdf")

    texto = ""
    for page in reader.pages:
        texto += page.extract_text()

    chunks = [texto[i:i+500] for i in range(0, len(texto), 500)]
    emb_docs = modelo.encode(chunks)
    pergunta = input("Pergunta: ")
    emb_q = modelo.encode(pergunta)
    scores = []

    for i, emb in enumerate(emb_docs):
        s = cosine(emb_q, emb)
        scores.append((s, chunks[i]))

    scores.sort(reverse=True)
    contexto = scores[0][1]
    print("\nTrecho encontrado:\n", contexto)



# =====================================================
# MENU
# =====================================================

while True:

    print("\n==============================")
    print("AULA RAG - Exemplos")
    print("==============================")
    print("1 - RAG com dados no código")
    print("2 - RAG com TXT")
    print("3 - RAG com PDF")
    print("0 - Sair")

    op = input("\nEscolha: ")

    if op == "1":
        exemplo1()

    elif op == "2":
        exemplo2()

    elif op == "3":
        exemplo3()

    elif op == "0":
        break