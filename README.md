# 🚀 Portfólio — Gian Henrique | Analista de Dados

Portfólio profissional desenvolvido 100% em Python com Streamlit.  
Deploy gratuito e open source no **Streamlit Community Cloud**.

## ✨ Stack

| Camada | Tecnologia |
|--------|-----------|
| Framework | [Streamlit](https://streamlit.io) |
| Gráficos | [Plotly](https://plotly.com/python/) |
| Dados | [Pandas](https://pandas.pydata.org) |
| Hospedagem | [Streamlit Community Cloud](https://streamlit.io/cloud) |

## 🏃 Como rodar localmente

```bash
# 1. Clone o repositório
git clone https://github.com/<seu-usuario>/portfolio.git
cd portfolio

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute
streamlit run app.py
```

Acesse em: `http://localhost:8501`

## ☁️ Deploy gratuito (Streamlit Community Cloud)

1. Faça push deste repositório para o seu GitHub
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. Clique em **New app**
4. Selecione:
   - **Repository:** `<seu-usuario>/portfolio`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Clique em **Deploy!**

Pronto — URL pública gratuita em segundos. 🎉

## 🗂 Estrutura

```
portfolio/
├── app.py              # Aplicação principal (único arquivo)
├── requirements.txt    # Dependências
├── .streamlit/
│   └── config.toml     # Tema dark customizado
└── README.md
```

## 🎨 Personalização

Edite as variáveis no topo de `app.py`:

- **`PROFILE`** — nome, bio, links
- **`SKILLS`** — categorias e tecnologias
- **`PROJECTS`** — seus projetos com métricas e destaques
- **`EXPERIENCE`** — histórico profissional e acadêmico

Para atualizar o portfólio: edite `app.py` → `git push` → o Streamlit Cloud reconstrói automaticamente.

## 📄 Licença

MIT — use, adapte e redistribua livremente.
