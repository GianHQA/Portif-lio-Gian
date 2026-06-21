import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# ─────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────
st.set_page_config(
    page_title="Gian Henrique | Analista de Dados",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────
# CSS GLOBAL
# ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* Reset e base */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Esconde o menu padrão do Streamlit */
#MainMenu, footer, header { visibility: hidden; }

/* Fundo principal */
.stApp {
    background: #0F0F1A;
}

/* Remove padding padrão do Streamlit */
.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    max-width: 1200px;
}

/* ── HERO ── */
.hero-section {
    background: linear-gradient(135deg, #0F0F1A 0%, #1A1A2E 50%, #16213E 100%);
    padding: 80px 40px 60px;
    border-bottom: 1px solid #2D2D4E;
    position: relative;
    overflow: hidden;
}

.hero-section::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(99,102,241,0.12) 0%, transparent 70%);
    border-radius: 50%;
    pointer-events: none;
}

.hero-grid {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 40px;
    align-items: center;
    max-width: 1120px;
    margin: 0 auto;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(99,102,241,0.15);
    border: 1px solid rgba(99,102,241,0.35);
    border-radius: 50px;
    padding: 6px 16px;
    font-size: 13px;
    color: #818CF8;
    font-weight: 500;
    margin-bottom: 20px;
}

.hero-badge-dot {
    width: 7px;
    height: 7px;
    background: #22C55E;
    border-radius: 50%;
    animation: pulse-green 2s infinite;
}

@keyframes pulse-green {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(1.3); }
}

.hero-name {
    font-size: 52px;
    font-weight: 700;
    color: #F1F5F9;
    line-height: 1.1;
    margin: 0 0 12px;
    letter-spacing: -1.5px;
}

.hero-name span {
    background: linear-gradient(135deg, #6366F1, #A78BFA);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-title {
    font-size: 20px;
    color: #94A3B8;
    font-weight: 400;
    margin: 0 0 24px;
}

.hero-bio {
    font-size: 16px;
    color: #CBD5E1;
    line-height: 1.75;
    max-width: 620px;
    margin-bottom: 36px;
}

.hero-links {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
}

.btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #6366F1;
    color: white !important;
    padding: 12px 24px;
    border-radius: 10px;
    text-decoration: none !important;
    font-weight: 600;
    font-size: 14px;
    transition: all 0.2s;
    border: none;
}

.btn-primary:hover {
    background: #4F46E5;
    transform: translateY(-1px);
    box-shadow: 0 8px 24px rgba(99,102,241,0.35);
}

.btn-outline {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: transparent;
    color: #94A3B8 !important;
    padding: 12px 24px;
    border-radius: 10px;
    text-decoration: none !important;
    font-weight: 500;
    font-size: 14px;
    border: 1px solid #334155;
    transition: all 0.2s;
}

.btn-outline:hover {
    border-color: #6366F1;
    color: #818CF8 !important;
    background: rgba(99,102,241,0.08);
}

.hero-avatar {
    width: 180px;
    height: 180px;
    border-radius: 24px;
    border: 3px solid rgba(99,102,241,0.4);
    box-shadow: 0 0 40px rgba(99,102,241,0.2);
    object-fit: cover;
}

/* ── NAV PILLS ── */
.nav-container {
    background: #1A1A2E;
    border-bottom: 1px solid #2D2D4E;
    padding: 0 40px;
    position: sticky;
    top: 0;
    z-index: 100;
}

.nav-pills {
    display: flex;
    gap: 0;
    max-width: 1120px;
    margin: 0 auto;
}

.nav-pill {
    padding: 16px 20px;
    color: #64748B;
    text-decoration: none;
    font-size: 14px;
    font-weight: 500;
    border-bottom: 2px solid transparent;
    transition: all 0.2s;
    cursor: pointer;
}

.nav-pill:hover, .nav-pill.active {
    color: #818CF8;
    border-bottom-color: #6366F1;
}

/* ── SECTIONS ── */
.section {
    padding: 72px 40px;
    max-width: 1200px;
    margin: 0 auto;
}

.section-alt {
    background: #131320;
    padding: 72px 40px;
}

.section-inner {
    max-width: 1120px;
    margin: 0 auto;
}

.section-label {
    font-size: 13px;
    font-weight: 600;
    color: #6366F1;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

.section-title {
    font-size: 36px;
    font-weight: 700;
    color: #F1F5F9;
    margin: 0 0 12px;
    letter-spacing: -0.5px;
}

.section-subtitle {
    font-size: 16px;
    color: #64748B;
    margin-bottom: 48px;
}

/* ── STATS ── */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 64px;
}

.stat-card {
    background: #1A1A2E;
    border: 1px solid #2D2D4E;
    border-radius: 16px;
    padding: 28px 24px;
    text-align: center;
    transition: all 0.2s;
}

.stat-card:hover {
    border-color: rgba(99,102,241,0.4);
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
}

.stat-number {
    font-size: 36px;
    font-weight: 700;
    color: #818CF8;
    display: block;
    letter-spacing: -1px;
}

.stat-label {
    font-size: 13px;
    color: #64748B;
    margin-top: 4px;
}

/* ── SKILL CARDS ── */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 40px;
}

.skill-category {
    background: #1A1A2E;
    border: 1px solid #2D2D4E;
    border-radius: 16px;
    padding: 28px;
    transition: border-color 0.2s;
}

.skill-category:hover {
    border-color: rgba(99,102,241,0.35);
}

.skill-cat-icon {
    font-size: 28px;
    margin-bottom: 12px;
    display: block;
}

.skill-cat-title {
    font-size: 16px;
    font-weight: 600;
    color: #E2E8F0;
    margin-bottom: 16px;
}

.skill-tag {
    display: inline-block;
    background: rgba(99,102,241,0.12);
    border: 1px solid rgba(99,102,241,0.25);
    color: #A5B4FC;
    border-radius: 6px;
    padding: 4px 10px;
    font-size: 12px;
    font-weight: 500;
    margin: 3px;
    font-family: 'JetBrains Mono', monospace;
}

/* ── PROJECT CARDS ── */
.project-card {
    background: #1A1A2E;
    border: 1px solid #2D2D4E;
    border-radius: 20px;
    overflow: hidden;
    transition: all 0.25s;
}

.project-card:hover {
    border-color: rgba(99,102,241,0.45);
    transform: translateY(-4px);
    box-shadow: 0 16px 48px rgba(0,0,0,0.4);
}

.project-header {
    background: linear-gradient(135deg, #1E1E3F, #252545);
    padding: 28px;
    border-bottom: 1px solid #2D2D4E;
}

.project-badge {
    display: inline-block;
    background: rgba(34,197,94,0.15);
    border: 1px solid rgba(34,197,94,0.3);
    color: #4ADE80;
    border-radius: 50px;
    padding: 3px 12px;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 14px;
}

.project-name {
    font-size: 22px;
    font-weight: 700;
    color: #F1F5F9;
    margin-bottom: 8px;
}

.project-desc {
    font-size: 14px;
    color: #94A3B8;
    line-height: 1.6;
}

.project-body {
    padding: 28px;
}

.project-metrics {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-bottom: 20px;
}

.metric-box {
    background: #111124;
    border-radius: 10px;
    padding: 14px;
    text-align: center;
}

.metric-value {
    font-size: 20px;
    font-weight: 700;
    color: #818CF8;
    font-family: 'JetBrains Mono', monospace;
}

.metric-label {
    font-size: 11px;
    color: #475569;
    margin-top: 2px;
}

.project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 20px;
}

.tech-tag {
    background: #111124;
    border: 1px solid #2D2D4E;
    color: #94A3B8;
    border-radius: 6px;
    padding: 4px 10px;
    font-size: 12px;
    font-family: 'JetBrains Mono', monospace;
}

.project-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: #818CF8 !important;
    text-decoration: none !important;
    font-size: 13px;
    font-weight: 500;
    margin-top: 20px;
    transition: gap 0.2s;
}

.project-link:hover { gap: 10px; }

/* ── EXPERIENCE ── */
.timeline {
    position: relative;
    padding-left: 28px;
}

.timeline::before {
    content: '';
    position: absolute;
    left: 0;
    top: 8px;
    bottom: 8px;
    width: 2px;
    background: linear-gradient(to bottom, #6366F1, transparent);
}

.timeline-item {
    position: relative;
    padding: 0 0 40px 32px;
}

.timeline-item::before {
    content: '';
    position: absolute;
    left: -6px;
    top: 6px;
    width: 14px;
    height: 14px;
    border-radius: 50%;
    background: #6366F1;
    border: 3px solid #0F0F1A;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.25);
}

.timeline-date {
    font-size: 12px;
    color: #6366F1;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 6px;
}

.timeline-role {
    font-size: 18px;
    font-weight: 600;
    color: #E2E8F0;
    margin-bottom: 4px;
}

.timeline-org {
    font-size: 14px;
    color: #64748B;
    margin-bottom: 12px;
}

.timeline-desc {
    font-size: 14px;
    color: #94A3B8;
    line-height: 1.7;
}

/* ── CONTACT ── */
.contact-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    margin-top: 40px;
}

.contact-card {
    display: flex;
    align-items: center;
    gap: 16px;
    background: #1A1A2E;
    border: 1px solid #2D2D4E;
    border-radius: 14px;
    padding: 20px 24px;
    text-decoration: none !important;
    transition: all 0.2s;
}

.contact-card:hover {
    border-color: rgba(99,102,241,0.4);
    background: rgba(99,102,241,0.06);
    transform: translateX(4px);
}

.contact-icon {
    font-size: 24px;
    width: 48px;
    height: 48px;
    background: rgba(99,102,241,0.12);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.contact-label {
    font-size: 12px;
    color: #64748B;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.contact-value {
    font-size: 15px;
    color: #E2E8F0;
    font-weight: 500;
    margin-top: 2px;
}

/* ── FOOTER ── */
.footer {
    background: #0A0A14;
    border-top: 1px solid #1E1E32;
    padding: 32px 40px;
    text-align: center;
}

.footer-text {
    color: #334155;
    font-size: 14px;
}

.footer-text span {
    color: #6366F1;
}

/* ── DIVIDER ── */
.section-divider {
    height: 1px;
    background: linear-gradient(to right, transparent, #2D2D4E, transparent);
    margin: 0 40px;
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# DADOS DO PERFIL
# ─────────────────────────────────────────
PROFILE = {
    "name": "Gian Henrique",
    "title": "Analista de Dados • Python • SQL • BI",
    "avatar": "https://avatars.githubusercontent.com/u/135023573?v=4",
    "bio": (
        "Analista de Dados apaixonado por transformar grandes volumes de dados em decisões "
        "estratégicas de alto impacto. Especializado em pipelines ETL, dashboards interativos e "
        "análise exploratória com Python — do dado bruto à narrativa que orienta negócios. "
        "Construo soluções que aliam performance técnica à clareza visual, sempre com foco em "
        "gerar valor real para stakeholders."
    ),
    "github": "https://github.com/GianHQA",
    "linkedin": "https://www.linkedin.com/in/gian-henrique/",
    "email": "g.henriquequeiroz2003@gmail.com",
}

SKILLS = {
    "🐍  Python & Análise": ["Python", "Pandas", "NumPy", "Plotly", "Streamlit", "Jupyter"],
    "🗄️  Banco de Dados": ["SQL", "PostgreSQL", "DuckDB", "SQLite", "Parquet"],
    "📊  Visualização & BI": ["Power BI", "Plotly", "Matplotlib", "Seaborn", "Streamlit"],
    "⚙️  Engenharia de Dados": ["ETL / ELT", "Parquet", "Data Modeling", "Git / GitHub"],
    "☁️  Cloud & Deploy": ["Streamlit Cloud", "GitHub Actions", "Linux"],
    "🧠  Análise & Estatística": ["Análise Exploratória", "K-Means", "Séries Temporais", "KPIs"],
}

PROJECTS = [
    {
        "title": "Dashboard Executivo — Acidentes de Trânsito (PRF)",
        "status": "Em produção",
        "desc": (
            "Dashboard interativo completo para análise de acidentes em rodovias federais "
            "brasileiras (2022–2025). Pipeline ETL que processa ~350 MB de CSVs da PRF para "
            "~26 MB em Parquet, com 6 módulos analíticos: Visão Executiva, Operacional, "
            "Geográfica, Temporal, Fatores de Risco e Insights automáticos em linguagem natural."
        ),
        "metrics": [
            {"v": "271k+", "l": "Acidentes"},
            {"v": "726k+", "l": "Pessoas"},
            {"v": "6", "l": "Módulos"},
        ],
        "tech": ["Python", "Streamlit", "Plotly", "Pandas", "Parquet", "K-Means", "ETL"],
        "url": "https://github.com/GianHQA/Acidentes",
        "highlights": [
            "ETL automatizado com limpeza e qualidade de dados (lat/long, encoding, duplicatas)",
            "Modelo estrela otimizado: fact_acidentes + fact_pessoas + dim_uf",
            "Filtros globais sincronizados via st.session_state em todas as páginas",
            "Narrativa automática recalculada dinamicamente sobre os filtros ativos",
            "Exportação para Excel/PDF e captura de gráficos em PNG",
        ],
    },
]

EXPERIENCE = [
    {
        "date": "2022 – Presente",
        "role": "Analista de Dados (Projetos Independentes)",
        "org": "Portfólio Próprio",
        "desc": (
            "Desenvolvimento de dashboards analíticos end-to-end usando Python, Streamlit e Plotly. "
            "Foco em pipelines ETL com dados públicos abertos, modelagem dimensional e storytelling "
            "com dados para tomada de decisão baseada em evidências."
        ),
    },
    {
        "date": "2022 – Presente",
        "role": "Estudante de Análise e Desenvolvimento de Sistemas / TI",
        "org": "Formação Técnica e Superior",
        "desc": (
            "Formação com ênfase em banco de dados, algoritmos, estrutura de dados e desenvolvimento "
            "de software. Aplicação prática dos conceitos em projetos reais de análise de dados com "
            "impacto mensurável."
        ),
    },
]


# ─────────────────────────────────────────
# HERO SECTION
# ─────────────────────────────────────────
st.markdown(f"""
<section class="hero-section" id="sobre">
  <div class="hero-grid">
    <div>
      <div class="hero-badge">
        <span class="hero-badge-dot"></span>
        Disponível para oportunidades
      </div>
      <h1 class="hero-name">Gian <span>Henrique</span></h1>
      <p class="hero-title">{PROFILE['title']}</p>
      <p class="hero-bio">{PROFILE['bio']}</p>
      <div class="hero-links">
        <a href="{PROFILE['linkedin']}" target="_blank" class="btn-primary">
          🔗 LinkedIn
        </a>
        <a href="{PROFILE['github']}" target="_blank" class="btn-outline">
          💻 GitHub
        </a>
        <a href="mailto:{PROFILE['email']}" class="btn-outline">
          ✉️ Contato
        </a>
      </div>
    </div>
    <div>
      <img src="{PROFILE['avatar']}" class="hero-avatar" alt="Gian Henrique" />
    </div>
  </div>
</section>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# NAV PILLS
# ─────────────────────────────────────────
st.markdown("""
<nav class="nav-container">
  <div class="nav-pills">
    <a class="nav-pill active" href="#sobre">Sobre</a>
    <a class="nav-pill" href="#habilidades">Habilidades</a>
    <a class="nav-pill" href="#projetos">Projetos</a>
    <a class="nav-pill" href="#experiencia">Experiência</a>
    <a class="nav-pill" href="#contato">Contato</a>
  </div>
</nav>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# STATS (números de impacto)
# ─────────────────────────────────────────
st.markdown("""
<div class="section">
  <div class="stats-grid">
    <div class="stat-card">
      <span class="stat-number">1M+</span>
      <div class="stat-label">Registros processados</div>
    </div>
    <div class="stat-card">
      <span class="stat-number">6</span>
      <div class="stat-label">Módulos analíticos entregues</div>
    </div>
    <div class="stat-card">
      <span class="stat-number">100%</span>
      <div class="stat-label">Python open source</div>
    </div>
    <div class="stat-card">
      <span class="stat-number">26 MB</span>
      <div class="stat-label">de 350 MB (otimização ETL)</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)


# ─────────────────────────────────────────
# HABILIDADES
# ─────────────────────────────────────────
st.markdown('<div id="habilidades"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section-alt">
  <div class="section-inner">
    <div class="section-label">Stack Técnico</div>
    <h2 class="section-title">Habilidades & Tecnologias</h2>
    <p class="section-subtitle">Ferramentas que uso para transformar dados em decisões.</p>
  </div>
</div>
""", unsafe_allow_html=True)

# Radar chart de habilidades
col_chart, col_tags = st.columns([1, 1], gap="large")

with col_chart:
    categories = ["Python", "SQL", "ETL", "BI / Viz", "Estatística", "Git"]
    values = [90, 80, 85, 88, 75, 82]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill="toself",
        fillcolor="rgba(99,102,241,0.18)",
        line=dict(color="#6366F1", width=2.5),
        name="Nível",
        hovertemplate="%{theta}: %{r}%<extra></extra>",
    ))

    fig.update_layout(
        polar=dict(
            bgcolor="rgba(26,26,46,0.8)",
            radialaxis=dict(
                visible=True, range=[0, 100],
                gridcolor="#2D2D4E",
                tickcolor="#2D2D4E",
                tickfont=dict(color="#64748B", size=10),
                tickvals=[25, 50, 75, 100],
            ),
            angularaxis=dict(
                gridcolor="#2D2D4E",
                tickfont=dict(color="#94A3B8", size=13),
            ),
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        margin=dict(l=40, r=40, t=40, b=40),
        height=360,
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

with col_tags:
    skills_html = '<div class="skills-grid" style="grid-template-columns: repeat(2,1fr); margin-top:0">'
    for cat, tags in SKILLS.items():
        tags_html = "".join(f'<span class="skill-tag">{t}</span>' for t in tags)
        skills_html += f"""
        <div class="skill-category">
          <span class="skill-cat-icon">{cat.split()[0]}</span>
          <div class="skill-cat-title">{" ".join(cat.split()[1:])}</div>
          {tags_html}
        </div>
        """
    skills_html += "</div>"
    st.markdown(skills_html, unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)


# ─────────────────────────────────────────
# PROJETOS
# ─────────────────────────────────────────
st.markdown('<div id="projetos"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
  <div class="section-label">Portfólio</div>
  <h2 class="section-title">Projetos em Destaque</h2>
  <p class="section-subtitle">Soluções end-to-end: da engenharia de dados ao storytelling visual.</p>
</div>
""", unsafe_allow_html=True)

for proj in PROJECTS:
    metrics_html = "".join(
        f'<div class="metric-box"><div class="metric-value">{m["v"]}</div><div class="metric-label">{m["l"]}</div></div>'
        for m in proj["metrics"]
    )
    tech_html = "".join(f'<span class="tech-tag">{t}</span>' for t in proj["tech"])
    hl_html = "".join(f'<li style="color:#94A3B8;font-size:14px;margin-bottom:6px;line-height:1.6">{h}</li>' for h in proj["highlights"])

    st.markdown(f"""
    <div class="section" style="padding-top:0; padding-bottom:48px;">
      <div class="project-card">
        <div class="project-header">
          <div class="project-badge">{proj['status']}</div>
          <div class="project-name">{proj['title']}</div>
          <div class="project-desc">{proj['desc']}</div>
        </div>
        <div class="project-body">
          <div class="project-metrics">{metrics_html}</div>
          <div style="margin-top:20px">
            <div style="font-size:13px;color:#64748B;font-weight:600;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px">Destaques técnicos</div>
            <ul style="padding-left:18px;margin:0">{hl_html}</ul>
          </div>
          <div class="project-tech">{tech_html}</div>
          <a href="{proj['url']}" target="_blank" class="project-link">Ver no GitHub →</a>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# Gráfico demo do projeto (dados simulados tipo PRF)
st.markdown("""
<div class="section-alt">
  <div class="section-inner">
    <div class="section-label">Projeto em Ação</div>
    <h3 style="color:#F1F5F9;font-size:22px;font-weight:600;margin-bottom:4px">Prévia: Acidentes PRF 2022–2025</h3>
    <p style="color:#64748B;font-size:14px;margin-bottom:24px">Visualizações representativas do dashboard executivo.</p>
  </div>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    anos = [2022, 2023, 2024, 2025]
    acidentes = [64_312, 67_891, 71_204, 68_003]
    mortos = [5_760, 5_982, 6_140, 5_831]

    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=anos, y=acidentes, name="Acidentes",
        marker_color="#6366F1",
        hovertemplate="%{x}: %{y:,.0f} acidentes<extra></extra>",
    ))
    fig2.add_trace(go.Scatter(
        x=anos, y=mortos, name="Óbitos",
        yaxis="y2", mode="lines+markers",
        line=dict(color="#F43F5E", width=3),
        marker=dict(size=8),
        hovertemplate="%{x}: %{y:,.0f} óbitos<extra></extra>",
    ))
    fig2.update_layout(
        title=dict(text="Evolução Anual — Acidentes e Óbitos", font=dict(color="#E2E8F0", size=15)),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(26,26,46,0.6)",
        xaxis=dict(gridcolor="#2D2D4E", tickfont=dict(color="#64748B")),
        yaxis=dict(gridcolor="#2D2D4E", tickfont=dict(color="#64748B"), title="Acidentes"),
        yaxis2=dict(overlaying="y", side="right", tickfont=dict(color="#F43F5E"), title="Óbitos"),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="#94A3B8")),
        margin=dict(l=10, r=10, t=48, b=10),
        height=320,
    )
    st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})

with col2:
    causas = ["Falta de atenção", "Velocidade incompatível", "Desobediência", "Ultrapassagem", "Dormindo"]
    valores = [31.4, 19.8, 12.3, 8.7, 6.1]

    fig3 = go.Figure(go.Bar(
        x=valores, y=causas, orientation="h",
        marker=dict(
            color=valores,
            colorscale=[[0, "#2D2D4E"], [1, "#6366F1"]],
        ),
        hovertemplate="%{y}: %{x}%<extra></extra>",
        text=[f"{v}%" for v in valores],
        textposition="outside",
        textfont=dict(color="#94A3B8", size=12),
    ))
    fig3.update_layout(
        title=dict(text="Top 5 Causas de Acidentes (%)", font=dict(color="#E2E8F0", size=15)),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(26,26,46,0.6)",
        xaxis=dict(gridcolor="#2D2D4E", tickfont=dict(color="#64748B"), showticklabels=False),
        yaxis=dict(gridcolor="#2D2D4E", tickfont=dict(color="#94A3B8")),
        margin=dict(l=10, r=60, t=48, b=10),
        height=320,
    )
    st.plotly_chart(fig3, use_container_width=True, config={"displayModeBar": False})

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)


# ─────────────────────────────────────────
# EXPERIÊNCIA
# ─────────────────────────────────────────
st.markdown('<div id="experiencia"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section">
  <div class="section-label">Trajetória</div>
  <h2 class="section-title">Experiência & Formação</h2>
  <p class="section-subtitle">Construindo expertise através de projetos reais e formação técnica sólida.</p>
  <div class="timeline">
""", unsafe_allow_html=True)

for exp in EXPERIENCE:
    st.markdown(f"""
    <div class="timeline-item">
      <div class="timeline-date">{exp['date']}</div>
      <div class="timeline-role">{exp['role']}</div>
      <div class="timeline-org">{exp['org']}</div>
      <div class="timeline-desc">{exp['desc']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div></div>', unsafe_allow_html=True)
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)


# ─────────────────────────────────────────
# CONTATO
# ─────────────────────────────────────────
st.markdown('<div id="contato"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="section-alt">
  <div class="section-inner">
    <div class="section-label">Vamos conversar</div>
    <h2 class="section-title">Entre em Contato</h2>
    <p class="section-subtitle">Aberto a oportunidades de analista de dados, BI e engenharia de dados.</p>
    <div class="contact-grid">
      <a href="mailto:{PROFILE['email']}" class="contact-card">
        <div class="contact-icon">✉️</div>
        <div>
          <div class="contact-label">E-mail</div>
          <div class="contact-value">{PROFILE['email']}</div>
        </div>
      </a>
      <a href="{PROFILE['linkedin']}" target="_blank" class="contact-card">
        <div class="contact-icon">🔗</div>
        <div>
          <div class="contact-label">LinkedIn</div>
          <div class="contact-value">linkedin.com/in/gian-henrique</div>
        </div>
      </a>
      <a href="{PROFILE['github']}" target="_blank" class="contact-card">
        <div class="contact-icon">💻</div>
        <div>
          <div class="contact-label">GitHub</div>
          <div class="contact-value">github.com/GianHQA</div>
        </div>
      </a>
      <a href="https://wa.me/55" class="contact-card">
        <div class="contact-icon">📱</div>
        <div>
          <div class="contact-label">WhatsApp / Localização</div>
          <div class="contact-value">Brasil 🇧🇷</div>
        </div>
      </a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# FOOTER
# ─────────────────────────────────────────
st.markdown("""
<div class="footer">
  <p class="footer-text">
    Feito com <span>♥</span> em Python + Streamlit &nbsp;·&nbsp;
    Open source no <span>GitHub</span> &nbsp;·&nbsp;
    Hospedado no <span>Streamlit Community Cloud</span>
  </p>
</div>
""", unsafe_allow_html=True)
