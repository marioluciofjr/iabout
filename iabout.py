import streamlit as st
import google.generativeai as genai
import textwrap
from IPython.display import Markdown

st.title("IAbout: gerador de texto para a seção 'Sobre' do LinkedIn")

# Configuração da API Key
api_key = st.text_input("Insira sua API Key | Para gerar uma API Key, confira o read.me do repositório no GitHub", type="password")

# Configuração do modelo
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name='gemini-1.5-flash-latest',
                                      generation_config={
                                          "candidate_count": 1,
                                          "temperature": 0.75,
                                          "top_k": 40,
                                          "top_p": 0.95
                                      },
                                      safety_settings={
                                          'HATE': 'BLOCK_NONE',
                                          'HARASSMENT': 'BLOCK_NONE',
                                          'SEXUAL': 'BLOCK_NONE',
                                          'DANGEROUS': 'BLOCK_NONE'
                                      },
                                      system_instruction="Você atuará como uma pessoa especialista em recrutamento e seleção, bem como configuração de perfis no LinkedIn.")
    
    # Input para a formação
    formacao = st.text_input("Qual é sua formação acadêmica? # graduação, pós ou cursos complementares que quiser citar")

    # Input para o trabalho
    trabalho = st.text_input("O que você faz profissionalmente? # conte sobre o eu trabalho ou realizações profissionais")

    # Input para os propósitos
    propositos = {
        1: "Construir uma marca pessoal forte",
        2: "Expandir a minha rede de contatos",
        3: "Encontrar oportunidades de trabalho",
        4: "Aprender sobre novas tendências",
        5: "Estabelecer-me como uma pessoa especialista na minha área",
        6: "Gerar leads para o meu negócio",
        7: "Recrutar candidatos para uma ou mais vagas",
        8: "Promover minha empresa",
        9: "Encontrar mentorias",
        10: "Compartilhar ensinamentos"
    }

    propositos_selecionados = st.multiselect("Selecione três propósitos de estar no LinkedIn", list(propositos.values()), max_selections=3)

    # Input para os hobbies
    hobbies = st.text_input("Quais são os seus hobbies? # essa parte é para humanizar o seu texto")

    # Input para o orgulho
    orgulho = st.text_input("Qual é o seu orgulho pessoal ou profissional? # é algo que pode ressaltar seus valores pessoais, algo que te marcou/marca")

    # Input para o contato
    contatos = st.text_input("Qual é o seu contato? # para a pessoa querer te conhecer melhor")

    # Input para as palavras-chave
    palavras_chave = st.text_input("Quais são as palavras-chave que você quer utilizar no texto?")

    # Botão para gerar o texto
    if st.button("Gerar Texto"):
        # Obtem os números dos propósitos selecionados
        lista_propositos = [list(propositos.keys())[list(propositos.values()).index(p)] for p in propositos_selecionados]

        # Imprime os propósitos selecionados
        propositos_str = ", ".join(propositos_selecionados)

        response = model.generate_content(f"""Com base nos inputs, siga os seguintes passos:
        Faça um parágrafo de três linhas sobre a minha formação em {formacao} e como eu trabalho com {trabalho}, sendo que a intenção desse parágrafo é gerar impacto e conseguir capturar a atenção a trajetória profissional.
        Faça um parágrafo de duas linhas sobre os meus principais objetivos no LinkedIn {propositos_str}, sendo que a intenção também é gerar impacto.
        Faça um parágrafo de duas linhas e meia sobre como meus hobbies {hobbies} geraram repertório e do que me orgulho em {orgulho}, tendo como intenção gerar empatia ao evidenciar um estilo de vida e valores que se destacam.
        Faça um parágrafo de duas linhas sobre como entrar em contato por meio do {contatos}, cuja intenção é gerar engajamento para a pessoa tomar uma decisão.
        REGRAS:
        O tom de voz é profissional, didático e objetivo.
        O texto é em primeira pessoa para colocar na seção 'Sobre' do LinkedIn
        As palavras-chave que deve utilizar durante o texto são: {palavras_chave}""")

        def to_markdown(text):
          text = text.replace('•', '  *')
          return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

        st.markdown(f'{response.text}')
