# IAbout
Repositório para o projeto IAbout, que visa gerar um texto automático para seção "Sobre" do LinkedIn

## Introdução
A seção "Sobre" do LinkedIn é uma das mais importantes no preenchimento do perfil, pois resume o que você é, o que faz, os seus propósitos e como entrar em contato contigo. 
Além disso, esse resumo colabora para a pontuação do atributo "Estabelecer sua marca profissional", do SSI (Social Selling Index). Como nem todo mundo sabe o que escrever nessa seção do perfil, desenvolvi uma maneira de facilitar esse trabalho por meio da IA do Gemini, do Google.
 
> [!TIP]
> Saiba mais sobre [Social Selling Index](https://snov.io/blog/br/social-selling-no-linkedin-um-guia-passo-a-passo/)

## Instalação

Pacote do Google AI para instalar caso queira testar o código about.py

```bash
pip install -q -U google-generativeai
```
## Como gerar sua API Key

+ Acesse o [Google AI Studio](https://aistudio.google.com/app/apikey)
+ Vá em **Create API Key**, caso não tenha criado uma chave ainda

![step1](https://github.com/marioluciofjr/iabout/assets/105465306/b14090b9-04e1-4c52-9e52-ad5a43fd49c1)

+ Vá em **Got it**

![step2](https://github.com/marioluciofjr/iabout/assets/105465306/f66d7392-d5a6-43ac-91a8-8c0ad56f1c8d)

+ Clique em **Create API Key in new project**

![Step3](https://github.com/marioluciofjr/iabout/assets/105465306/6af71fbd-5061-4e6e-ad6d-2b7808c3db83)

+ Sua API Key foi gerada com sucesso! Depois é só apertar **Copy** para copiar a chave e inserir no seu projeto.

> [!CAUTION]
> Lembre-se de não compartilhar sua chave com ninguém!

![Screenshot - 2024-05-15T220248 539](https://github.com/marioluciofjr/iabout/assets/105465306/7d37fe0c-1474-4c7a-b7e0-46727414bdec)

+ A chave fica disponível pra você acessar quando precisar. Basta só clicar na sequência em azul para copiar novamente.

![Screenshot - 2024-05-15T220604 937](https://github.com/marioluciofjr/iabout/assets/105465306/fcbc6d01-049c-4882-9cbd-14febaa43deb)

## Utilização

Para facilitar o uso dessa ferramenta, implantei o repositório numa interface [Streamlit](https://iabout.streamlit.app/)

![Screenshot - 2024-05-15T221743 919](https://github.com/marioluciofjr/iabout/assets/105465306/d44d6ed8-2b2a-4584-ac73-38b32be30fa5)




