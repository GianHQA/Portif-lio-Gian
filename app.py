import base64
from pathlib import Path

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
# PALETA DE CORES (preto + vermelho pastel + neutros quentes)
# Fonte única de verdade para CSS e para os gráficos Plotly.
# ─────────────────────────────────────────
COLORS = {
    "bg": "#0A0908",
    "bg_alt": "#100E0D",
    "surface": "#141210",
    "surface_2": "#1A1714",
    "border": "#2A2624",
    "border_strong": "#3A3432",
    "accent": "#E8867D",
    "accent_light": "#F2A7A0",
    "accent_lighter": "#F4B8B0",
    "accent_dark": "#C96860",
    "accent_soft": "rgba(232,134,125,0.14)",
    "accent_soft_strong": "rgba(232,134,125,0.30)",
    "text_1": "#FAF8F6",
    "text_2": "#A8A29E",
    "text_3": "#7A7370",
    "neutral_bar": "#4A4440",
}

# ─────────────────────────────────────────
# CSS GLOBAL
# ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --bg: #0A0908;
    --bg-alt: #100E0D;
    --surface: #141210;
    --surface-2: #1A1714;
    --border: #2A2624;
    --border-strong: #3A3432;
    --accent: #E8867D;
    --accent-light: #F2A7A0;
    --accent-lighter: #F4B8B0;
    --accent-dark: #C96860;
    --accent-soft: rgba(232,134,125,0.14);
    --accent-soft-strong: rgba(232,134,125,0.30);
    --text-1: #FAF8F6;
    --text-2: #A8A29E;
    --text-3: #7A7370;
    --radius-sm: 10px;
    --radius-md: 16px;
    --radius-lg: 22px;
    --ease: cubic-bezier(.2,.7,.2,1);
}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

*, *::before, *::after {
    box-sizing: border-box;
}

html { scroll-behavior: smooth; }

img { max-width: 100%; height: auto; }

::selection { background: var(--accent-soft-strong); color: var(--text-1); }

:focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 2px;
    border-radius: 4px;
}

/* ── ANIMAÇÃO DE ENTRADA ── */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(18px); }
    to { opacity: 1; transform: translateY(0); }
}

.hero-section, .section-title {
    animation: fadeInUp 0.7s var(--ease) both;
}

@media (prefers-reduced-motion: reduce) {
    .hero-section, .section-title {
        animation: none;
    }
}

/* Esconde o menu padrão do Streamlit */
#MainMenu, footer, header { visibility: hidden; }

/* Fundo principal */
.stApp {
    background: var(--bg);
    overflow-x: hidden;
}

/* Remove padding padrão do Streamlit */
.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    max-width: 1200px;
    overflow-x: hidden;
}

/* ── HERO ── */
.hero-section {
    background:
        radial-gradient(circle at 85% 0%, rgba(232,134,125,0.10) 0%, transparent 55%),
        linear-gradient(160deg, #0A0908 0%, #120F0D 55%, #18130F 100%);
    padding: 96px 40px 64px;
    border-bottom: 1px solid var(--border);
    position: relative;
    overflow: hidden;
}

.hero-section::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
    background-size: 56px 56px;
    mask-image: radial-gradient(ellipse 70% 60% at 50% 0%, black 0%, transparent 70%);
    pointer-events: none;
}

.hero-grid {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 48px;
    align-items: center;
    max-width: 1120px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 9px;
    background: var(--accent-soft);
    border: 1px solid var(--accent-soft-strong);
    border-radius: 50px;
    padding: 7px 16px;
    font-size: 13px;
    color: var(--accent-light);
    font-weight: 500;
    margin-bottom: 22px;
}

.hero-badge-dot {
    width: 7px;
    height: 7px;
    background: var(--accent);
    border-radius: 50%;
    animation: pulse-accent 2s infinite;
}

@keyframes pulse-accent {
    0%, 100% { opacity: 1; transform: scale(1); box-shadow: 0 0 0 0 rgba(232,134,125,0.5); }
    50% { opacity: 0.7; transform: scale(1.25); box-shadow: 0 0 0 4px rgba(232,134,125,0); }
}

.hero-name {
    font-size: 56px;
    font-weight: 800;
    color: var(--text-1);
    line-height: 1.08;
    margin: 0 0 14px;
    letter-spacing: -1.8px;
}

.hero-name span {
    background: linear-gradient(135deg, var(--accent), var(--accent-lighter));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-title {
    font-size: 20px;
    color: var(--text-2);
    font-weight: 400;
    margin: 0 0 24px;
}

.hero-bio {
    font-size: 16px;
    color: #C9C2BD;
    line-height: 1.8;
    max-width: 620px;
    margin-bottom: 36px;
}

.hero-links {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
}

.btn-ico {
    width: 16px;
    height: 16px;
    display: inline-flex;
    flex-shrink: 0;
}

.btn-ico svg { width: 100%; height: 100%; }

.btn-primary {
    display: inline-flex;
    align-items: center;
    gap: 9px;
    background: var(--accent);
    color: #1A0E0C !important;
    padding: 13px 24px;
    border-radius: var(--radius-sm);
    text-decoration: none !important;
    font-weight: 600;
    font-size: 14px;
    transition: all 0.2s var(--ease);
    border: none;
}

.btn-primary:hover {
    background: var(--accent-light);
    transform: translateY(-2px);
    box-shadow: 0 10px 28px rgba(232,134,125,0.30);
}

.btn-outline {
    display: inline-flex;
    align-items: center;
    gap: 9px;
    background: transparent;
    color: var(--text-2) !important;
    padding: 13px 24px;
    border-radius: var(--radius-sm);
    text-decoration: none !important;
    font-weight: 500;
    font-size: 14px;
    border: 1px solid var(--border-strong);
    transition: all 0.2s var(--ease);
}

.btn-outline:hover {
    border-color: var(--accent);
    color: var(--accent-light) !important;
    background: var(--accent-soft);
    transform: translateY(-2px);
}

.hero-avatar-wrap {
    position: relative;
    width: 188px;
    height: 188px;
}

.hero-avatar-wrap::before {
    content: '';
    position: absolute;
    inset: -10px;
    border-radius: 28px;
    background: linear-gradient(135deg, var(--accent), transparent 70%);
    opacity: 0.35;
    filter: blur(18px);
    z-index: 0;
}

.hero-avatar {
    width: 188px;
    height: 188px;
    border-radius: 24px;
    border: 2px solid var(--border-strong);
    object-fit: cover;
    position: relative;
    z-index: 1;
    display: block;
}

/* ── NAV PILLS ── */
.nav-container {
    background: rgba(10,9,8,0.78);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-bottom: 1px solid var(--border);
    padding: 0 40px;
    position: sticky;
    top: 0;
    z-index: 100;
}

.nav-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 1120px;
    margin: 0 auto;
}

.nav-pills {
    display: flex;
    gap: 4px;
}

.nav-pill {
    padding: 18px 18px;
    color: var(--text-3) !important;
    text-decoration: none !important;
    font-size: 14px;
    font-weight: 500;
    border-bottom: 2px solid transparent;
    transition: all 0.2s var(--ease);
    cursor: pointer;
}

.nav-pill:hover, .nav-pill.active {
    color: var(--accent-light) !important;
    border-bottom-color: var(--accent);
}

/* Toggle hambúrguer — escondido no desktop, CSS-only (sem JS) */
.nav-toggle-input { display: none; }

.nav-toggle-btn {
    display: none;
    flex-direction: column;
    justify-content: center;
    gap: 5px;
    width: 32px;
    height: 32px;
    cursor: pointer;
}

.nav-toggle-btn span {
    display: block;
    height: 2px;
    width: 100%;
    background: var(--text-2);
    border-radius: 2px;
    transition: all 0.25s var(--ease);
}

.nav-toggle-input:checked ~ .nav-bar .nav-toggle-btn span:nth-child(1) {
    transform: translateY(7px) rotate(45deg);
}
.nav-toggle-input:checked ~ .nav-bar .nav-toggle-btn span:nth-child(2) {
    opacity: 0;
}
.nav-toggle-input:checked ~ .nav-bar .nav-toggle-btn span:nth-child(3) {
    transform: translateY(-7px) rotate(-45deg);
}

/* ── SECTIONS ── */
.section {
    padding: 80px 40px;
    max-width: 1200px;
    margin: 0 auto;
}

.section-alt {
    background: var(--bg-alt);
    padding: 80px 40px;
}

.section-inner {
    max-width: 1120px;
    margin: 0 auto;
}

.section-label {
    font-size: 13px;
    font-weight: 600;
    color: var(--accent);
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.section-title {
    font-size: 38px;
    font-weight: 800;
    color: var(--text-1);
    margin: 0 0 12px;
    letter-spacing: -0.7px;
}

.section-subtitle {
    font-size: 16px;
    color: var(--text-3);
    margin-bottom: 52px;
}

/* ── STATS ── */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 68px;
}

.stat-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 26px 22px;
    transition: all 0.25s var(--ease);
}

.stat-card:hover {
    border-color: var(--accent-soft-strong);
    transform: translateY(-3px);
    box-shadow: 0 14px 36px rgba(0,0,0,0.45);
}

.stat-icon {
    width: 22px;
    height: 22px;
    color: var(--accent);
    margin-bottom: 14px;
}

.stat-icon svg { width: 100%; height: 100%; }

.stat-number {
    font-size: 34px;
    font-weight: 800;
    color: var(--text-1);
    display: block;
    letter-spacing: -1px;
    font-family: 'JetBrains Mono', monospace;
}

.stat-label {
    font-size: 13px;
    color: var(--text-3);
    margin-top: 6px;
}

/* ── SKILL CARDS ── */
.skills-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    margin-top: 40px;
}

.skill-category {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 28px;
    transition: all 0.25s var(--ease);
}

.skill-category:hover {
    border-color: var(--accent-soft-strong);
    transform: translateY(-3px);
    box-shadow: 0 14px 36px rgba(0,0,0,0.45);
}

.skill-cat-icon {
    width: 28px;
    height: 28px;
    margin-bottom: 14px;
    display: block;
    color: var(--accent);
}

.skill-cat-icon svg {
    width: 100%;
    height: 100%;
}

.skill-cat-title {
    font-size: 16px;
    font-weight: 600;
    color: var(--text-1);
    margin-bottom: 16px;
}

.skill-tag {
    display: inline-block;
    background: var(--accent-soft);
    border: 1px solid var(--accent-soft-strong);
    color: var(--accent-light);
    border-radius: 6px;
    padding: 4px 10px;
    font-size: 12px;
    font-weight: 500;
    margin: 3px;
    font-family: 'Inter', sans-serif;
}

/* ── PRINCIPAIS COMPETÊNCIAS ── */
.highlight-strip {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 28px;
}

.highlight-chip {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 50px;
    padding: 10px 18px;
    color: var(--text-1);
    font-size: 14px;
    font-weight: 500;
    transition: all 0.2s var(--ease);
}

.highlight-chip:hover {
    border-color: var(--accent-soft-strong);
    background: var(--accent-soft);
    transform: translateY(-2px);
}

.highlight-chip-icon {
    width: 18px;
    height: 18px;
    color: var(--accent);
    flex-shrink: 0;
}

.highlight-chip-icon svg {
    width: 100%;
    height: 100%;
}

/* ── LINKEDIN / POWER BI HIGHLIGHTS ── */
.linkedin-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    margin-top: 24px;
}

.linkedin-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 24px;
    transition: all 0.25s var(--ease);
    display: flex;
    flex-direction: column;
    max-width: 100%;
    overflow-wrap: break-word;
    word-break: break-word;
}

.linkedin-card:hover {
    border-color: var(--accent-soft-strong);
    transform: translateY(-3px);
    box-shadow: 0 14px 36px rgba(0,0,0,0.45);
}

.linkedin-card-title {
    font-size: 15px;
    font-weight: 600;
    color: var(--text-1);
    margin-bottom: 8px;
    line-height: 1.4;
}

.linkedin-card-desc {
    font-size: 13px;
    color: var(--text-2);
    line-height: 1.6;
    margin-bottom: 14px;
    flex-grow: 1;
}

.linkedin-card-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-bottom: 14px;
}

.linkedin-card-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    align-self: flex-start;
    background: var(--accent-soft);
    border: 1px solid var(--accent-soft-strong);
    color: var(--accent-light) !important;
    text-decoration: none !important;
    font-size: 13px;
    font-weight: 600;
    padding: 8px 16px;
    border-radius: 50px;
    transition: all 0.2s var(--ease);
}

.linkedin-card-link:hover {
    background: var(--accent-soft-strong);
    border-color: var(--accent);
    transform: translateY(-2px);
}

.linkedin-card-link-disabled {
    background: transparent;
    border-color: var(--border);
    color: var(--text-3) !important;
    cursor: default;
}

.linkedin-card-link-disabled:hover {
    background: transparent;
    transform: none;
}

.linkedin-card-link-icon {
    width: 14px;
    height: 14px;
    flex-shrink: 0;
}

.linkedin-card-link-icon svg {
    width: 100%;
    height: 100%;
}

/* ── PROJECT CARDS ── */
.project-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    overflow: hidden;
    transition: all 0.3s var(--ease);
}

.project-card:hover {
    border-color: var(--accent-soft-strong);
    transform: translateY(-5px);
    box-shadow: 0 22px 56px rgba(0,0,0,0.5);
}

.project-header {
    background: linear-gradient(135deg, #161210, #1C1714);
    padding: 30px;
    border-bottom: 1px solid var(--border);
}

.project-badge {
    display: inline-block;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.14);
    color: #C9C2BD;
    border-radius: 50px;
    padding: 3px 12px;
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 14px;
}

.project-badge.finalizado {
    background: var(--accent-soft);
    border: 1px solid var(--accent-soft-strong);
    color: var(--accent-light);
}

.project-name {
    font-size: 23px;
    font-weight: 700;
    color: var(--text-1);
    margin-bottom: 8px;
    letter-spacing: -0.3px;
}

.project-desc {
    font-size: 14px;
    color: var(--text-2);
    line-height: 1.65;
}

.ver-mais-input { display: none; }
.ver-mais-label { display: none; }

.project-body {
    padding: 30px;
}

.project-metrics {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-bottom: 22px;
}

.metric-box {
    background: var(--bg-alt);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px;
    text-align: center;
}

.metric-value {
    font-size: 20px;
    font-weight: 700;
    color: var(--accent-light);
    font-family: 'JetBrains Mono', monospace;
}

.metric-label {
    font-size: 11px;
    color: var(--text-3);
    margin-top: 2px;
}

.project-tech {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
    margin-top: 22px;
}

.tech-tag {
    background: var(--bg-alt);
    border: 1px solid var(--border);
    color: var(--text-2);
    border-radius: 6px;
    padding: 4px 10px;
    font-size: 12px;
    font-weight: 500;
    font-family: 'Inter', sans-serif;
}

.project-link {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: var(--accent-light) !important;
    text-decoration: none !important;
    font-size: 13px;
    font-weight: 600;
    margin-top: 22px;
    transition: gap 0.2s var(--ease);
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
    background: linear-gradient(to bottom, var(--accent), transparent);
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
    background: var(--accent);
    border: 3px solid var(--bg);
    box-shadow: 0 0 0 3px var(--accent-soft-strong);
}

.timeline-date {
    font-size: 12px;
    color: var(--accent-light);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 6px;
}

.timeline-role {
    font-size: 18px;
    font-weight: 600;
    color: var(--text-1);
    margin-bottom: 4px;
}

.timeline-org {
    font-size: 14px;
    color: var(--text-3);
    margin-bottom: 12px;
}

.timeline-desc {
    font-size: 14px;
    color: var(--text-2);
    line-height: 1.75;
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
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 20px 24px;
    text-decoration: none !important;
    transition: all 0.2s var(--ease);
}

.contact-card:hover {
    border-color: var(--accent-soft-strong);
    background: var(--accent-soft);
    transform: translateX(5px);
}

.contact-icon {
    width: 48px;
    height: 48px;
    background: var(--accent-soft);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    color: var(--accent);
}

.contact-icon svg { width: 22px; height: 22px; }

.contact-label {
    font-size: 12px;
    color: var(--text-3);
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.contact-value {
    font-size: 15px;
    color: var(--text-1);
    font-weight: 500;
    margin-top: 2px;
}

/* ── FOOTER ── */
.footer {
    background: #060504;
    border-top: 1px solid #211D1B;
    padding: 32px 40px;
    text-align: center;
}

.footer-text {
    color: var(--text-3);
    font-size: 14px;
}

.footer-text span {
    color: var(--accent);
}

/* ── DIVIDER ── */
.section-divider {
    height: 1px;
    background: linear-gradient(to right, transparent, var(--border), transparent);
    margin: 0 40px;
}

/* ── RESPONSIVE: TABLET ── */
@media (max-width: 900px) {
    .hero-section { padding: 60px 24px 44px; }
    .hero-grid { grid-template-columns: 1fr; gap: 32px; text-align: center; }
    .hero-grid > div:first-child { order: 2; }
    .hero-grid > div:last-child { order: 1; display: flex; justify-content: center; }
    .hero-links { justify-content: center; }
    .hero-bio { margin: 0 auto 36px; }
    .hero-name { font-size: 42px; }
    .hero-avatar, .hero-avatar-wrap { width: 148px; height: 148px; }

    .nav-container { padding: 0 16px; overflow-x: visible; }
    .nav-bar { position: relative; }
    .nav-toggle-btn { display: flex; }

    .nav-pills {
        max-height: 0;
        overflow: hidden;
        position: absolute;
        top: 100%;
        left: 0;
        right: 0;
        flex-direction: column;
        gap: 0;
        background: rgba(10,9,8,0.97);
        backdrop-filter: blur(14px);
        border-bottom: 1px solid var(--border);
        box-shadow: 0 16px 32px rgba(0,0,0,0.5);
        transition: max-height 0.3s var(--ease);
    }

    .nav-toggle-input:checked ~ .nav-bar .nav-pills {
        max-height: 70vh;
    }

    .nav-pill {
        padding: 14px 20px;
        min-height: 44px;
        display: flex;
        align-items: center;
        width: 100%;
        border-bottom: 1px solid var(--border);
        border-left: 2px solid transparent;
        font-size: 14px;
    }

    .nav-pill:hover, .nav-pill.active {
        border-bottom-color: var(--border);
        border-left-color: var(--accent);
        background: var(--accent-soft);
    }

    .section, .section-alt { padding: 52px 24px; }
    .section-title { font-size: 30px; }

    .stats-grid { grid-template-columns: repeat(2, 1fr) !important; }
    .skills-grid { grid-template-columns: 1fr !important; }
    .linkedin-grid { grid-template-columns: 1fr !important; }
    .project-metrics { grid-template-columns: repeat(3, 1fr); gap: 8px; }
    .contact-grid { grid-template-columns: 1fr !important; }
}

/* ── RESPONSIVE: MOBILE ── */
@media (max-width: 600px) {
    .hero-section::before { opacity: 0.5; }
    .hero-section { padding: 44px 16px 36px; }
    .hero-name { font-size: 33px; }
    .hero-title { font-size: 16px; }
    .hero-bio { font-size: 14px; }
    .hero-avatar, .hero-avatar-wrap { width: 116px; height: 116px; border-radius: 18px; }
    .btn-primary, .btn-outline { padding: 11px 18px; font-size: 13px; flex: 1; justify-content: center; }
    .hero-links { width: 100%; }

    .nav-pill { padding: 14px 20px; font-size: 13px; }

    .section, .section-alt { padding: 40px 16px; }
    .section-title { font-size: 25px; }
    .section-subtitle { font-size: 14px; margin-bottom: 34px; }

    .stats-grid { grid-template-columns: repeat(2, 1fr) !important; gap: 10px; margin-bottom: 42px; }
    .stat-number { font-size: 26px; }
    .stat-card { padding: 18px 14px; }

    .project-metrics { grid-template-columns: 1fr 1fr; }
    .metric-value { font-size: 16px; }
    .project-header, .project-body { padding: 22px; }
    .project-name { font-size: 19px; }

    .project-desc.truncate {
        display: -webkit-box;
        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;
        overflow: hidden;
    }
    .ver-mais-label {
        display: inline-block;
        color: var(--accent-light);
        font-size: 13px;
        font-weight: 600;
        margin-top: 10px;
        cursor: pointer;
    }
    .ver-mais-input:checked ~ .project-header .project-desc.truncate {
        -webkit-line-clamp: unset;
        display: block;
        overflow: visible;
    }
    .ver-mais-input:checked ~ .project-header .ver-mais-label {
        display: none;
    }

    .linkedin-card { padding: 18px; }
    .linkedin-card-title { font-size: 14px; }
    .linkedin-card-desc { font-size: 12px; }

    .timeline { padding-left: 20px; }
    .timeline-item { padding: 0 0 32px 24px; }
    .timeline-role { font-size: 16px; }

    .contact-card { padding: 16px 18px; }
    .section-divider { margin: 0 16px; }
    .footer { padding: 24px 16px; }
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# DADOS DO PERFIL
# ─────────────────────────────────────────
def _load_local_avatar():
    assets_dir = Path(__file__).parent / "assets"
    for name in ("avatar.jpg", "avatar.jpeg", "avatar.png"):
        path = assets_dir / name
        if path.exists():
            mime = "jpeg" if path.suffix in (".jpg", ".jpeg") else "png"
            encoded = base64.b64encode(path.read_bytes()).decode()
            return f"data:image/{mime};base64,{encoded}"
    return None


PROFILE = {
    "name": "Gian Henrique",
    "title": "Analista de Dados • Python • SQL • BI",
    "avatar": _load_local_avatar() or "https://avatars.githubusercontent.com/u/135023573?v=4",
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

# Ícones em SVG puro — evita depender de fonte de emoji do sistema/navegador,
# que pode renderizar como glifo quebrado ("código solto") em alguns ambientes.
ICONS = {
    "code": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="8 6 2 12 8 18"/><polyline points="16 6 22 12 16 18"/></svg>',
    "database": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v6c0 1.7 3.6 3 8 3s8-1.3 8-3V5"/><path d="M4 11v6c0 1.7 3.6 3 8 3s8-1.3 8-3v-6"/></svg>',
    "gear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 13a7.97 7.97 0 0 0 0-2l2-1.5-2-3.4-2.4 1a8 8 0 0 0-1.7-1L15 3h-4l-.3 2.6a8 8 0 0 0-1.7 1l-2.4-1-2 3.4 2 1.5a8 8 0 0 0 0 2l-2 1.5 2 3.4 2.4-1a8 8 0 0 0 1.7 1L11 21h4l.3-2.6a8 8 0 0 0 1.7-1l2.4 1 2-3.4-2-1.5Z"/></svg>',
    "cloud": '<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M6.5 19a4.5 4.5 0 0 1 0-9 6 6 0 0 1 11.6-1.6A4 4 0 0 1 17.5 16H6.5Z"/></svg>',
    "pulse": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 12 8 12 11 19 14 5 17 12 21 12"/></svg>',
    "trending-up": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 17 9 11 13 15 21 7"/><polyline points="14 7 21 7 21 14"/></svg>',
    "brain": '<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M9 2.5a3.5 3.5 0 0 0-3.4 4.3A3.5 3.5 0 0 0 4 10c0 1.1.5 2 1.3 2.7A3 3 0 0 0 5 14c0 1.5 1.1 2.7 2.5 2.9V19a2.5 2.5 0 0 0 5 0V5.5A3 3 0 0 0 9 2.5Z"/><path d="M15 2.5a3.5 3.5 0 0 1 3.4 4.3A3.5 3.5 0 0 1 20 10c0 1.1-.5 2-1.3 2.7.2.4.3.8.3 1.3 0 1.5-1.1 2.7-2.5 2.9V19a2.5 2.5 0 0 1-5 0V5.5A3 3 0 0 1 15 2.5Z"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M20.8 8.6c0 4-8.8 9.4-8.8 9.4S3.2 12.6 3.2 8.6A4.6 4.6 0 0 1 12 6a4.6 4.6 0 0 1 8.8 2.6Z"/></svg>',
    "map-pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s7-5.5 7-11a7 7 0 1 0-14 0c0 5.5 7 11 7 11Z"/><circle cx="12" cy="11" r="2.5"/></svg>',
    "palette": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3a9 9 0 1 0 0 18c.6 0 1-.4 1-1 0-.3-.1-.5-.3-.7-.2-.2-.3-.5-.3-.8 0-.6.4-1 1-1h1.6A4.7 4.7 0 0 0 20 12.7 9 9 0 0 0 12 3Z"/><circle cx="7.5" cy="10.5" r="1.1" fill="currentColor"/><circle cx="11" cy="7.5" r="1.1" fill="currentColor"/><circle cx="15" cy="8.5" r="1.1" fill="currentColor"/><circle cx="16.5" cy="12.5" r="1.1" fill="currentColor"/></svg>',
    "bot": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="9" width="14" height="10" rx="2"/><circle cx="9" cy="14" r="1" fill="currentColor" stroke="none"/><circle cx="15" cy="14" r="1" fill="currentColor" stroke="none"/><path d="M12 9V5"/><circle cx="12" cy="3.5" r="1.3" fill="currentColor" stroke="none"/><path d="M3 13h2"/><path d="M19 13h2"/></svg>',
    "zap": '<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M4.5 3.5A2.5 2.5 0 1 0 4.5 8.5 2.5 2.5 0 0 0 4.5 3.5Z"/><rect x="2.5" y="9.5" width="4" height="12"/><path d="M10.5 9.5h4v2c.9-1.5 2.4-2.4 4.2-2.4 3.5 0 4.8 2.4 4.8 6V21.5h-4v-5.4c0-1.5-.5-2.6-1.9-2.6-1.1 0-1.8.8-2.1 1.5-.1.3-.1.6-.1 1v5.5h-4Z"/></svg>',
    "github": '<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M12 2C6.48 2 2 6.58 2 12.25c0 4.49 2.87 8.3 6.84 9.64.5.1.68-.22.68-.49 0-.24-.01-1.05-.01-1.9-2.78.62-3.37-1.22-3.37-1.22-.46-1.18-1.11-1.5-1.11-1.5-.91-.63.07-.62.07-.62 1 .07 1.53 1.04 1.53 1.04.89 1.55 2.34 1.1 2.91.84.09-.65.35-1.1.63-1.35-2.22-.26-4.56-1.13-4.56-5.02 0-1.11.39-2.02 1.03-2.73-.1-.26-.45-1.3.1-2.7 0 0 .84-.27 2.75 1.04a9.4 9.4 0 0 1 5 0c1.91-1.31 2.75-1.04 2.75-1.04.55 1.4.2 2.44.1 2.7.64.71 1.03 1.62 1.03 2.73 0 3.9-2.35 4.76-4.58 5.01.36.32.68.94.68 1.9 0 1.37-.01 2.48-.01 2.82 0 .27.18.6.69.49A10.02 10.02 0 0 0 22 12.25C22 6.58 17.52 2 12 2Z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 8.3 6a1.5 1.5 0 0 0 1.7 0L21 7"/></svg>',
    "whatsapp": '<svg viewBox="0 0 24 24" fill="currentColor" stroke="none"><path d="M19.05 4.91A9.82 9.82 0 0 0 12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2 22l5.25-1.38a9.87 9.87 0 0 0 4.78 1.22h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.02ZM12.04 20.15h-.01a8.2 8.2 0 0 1-4.18-1.14l-.3-.18-3.12.82.83-3.04-.2-.31a8.18 8.18 0 0 1-1.26-4.39c0-4.54 3.7-8.24 8.25-8.24a8.2 8.2 0 0 1 5.83 2.42 8.18 8.18 0 0 1 2.41 5.83c0 4.55-3.7 8.23-8.25 8.23Zm4.52-6.16c-.25-.12-1.47-.72-1.69-.81-.23-.08-.39-.12-.56.13-.17.25-.64.81-.78.97-.14.17-.29.18-.53.06-.25-.12-1.04-.38-1.98-1.22-.73-.65-1.23-1.46-1.37-1.7-.14-.25-.02-.39.11-.51.12-.12.25-.31.37-.46.12-.16.16-.27.25-.45.08-.18.04-.33-.04-.46-.08-.12-.55-1.33-.76-1.82-.2-.48-.41-.42-.56-.42-.14-.01-.31-.01-.47-.01-.17 0-.43.06-.66.31-.23.25-.88.86-.88 2.09 0 1.24.9 2.44 1.03 2.6.12.17 1.71 2.61 4.15 3.56 2.43.95 2.43.63 2.87.6.43-.04 1.47-.6 1.68-1.18.2-.58.2-1.07.14-1.18-.06-.1-.23-.16-.48-.28Z"/></svg>',
}

SKILLS = [
    {"icon": "code", "title": "Python & Análise", "tags": ["Python", "Pandas", "NumPy", "Plotly", "Streamlit", "Jupyter"]},
    {"icon": "database", "title": "Banco de Dados", "tags": ["SQL", "PostgreSQL", "DuckDB", "SQLite", "Parquet"]},
    {"icon": "gear", "title": "Engenharia de Dados", "tags": ["ETL / ELT", "Parquet", "Data Modeling", "Git / GitHub"]},
    {"icon": "cloud", "title": "Cloud & Deploy", "tags": ["Streamlit Cloud", "GitHub Actions", "Linux"]},
    {"icon": "pulse", "title": "Análise & Estatística", "tags": ["Análise Exploratória", "K-Means", "Séries Temporais", "KPIs"]},
    {"icon": "trending-up", "title": "Business Intelligence", "tags": ["Data Storytelling", "Geração de Insights", "Modelagem de Dados", "ETL e ELT", "Power BI", "DAX", "Power Query", "SQL", "Dashboards Executivos", "KPIs", "Análise Exploratória de Dados", "Governança de Dados", "Visualização de Dados"]},
    {"icon": "brain", "title": "Inteligência Artificial", "tags": ["RAG (Retrieval-Augmented Generation)", "Automação com IA", "Fine-Tuning de Modelos", "Engenharia de Prompt", "Agentes de IA", "IA Generativa", "LLMs", "Chatbots Inteligentes", "Processamento de Documentos com IA", "RPA + IA", "IA Aplicada à Análise de Dados"]},
]

POWERBI_HIGHLIGHTS = [
    {
        "icon": "heart",
        "title": "Arquitetura de Dados em Nuvem para Saúde Pública (SUS)",
        "desc": (
            "Projeto acadêmico em equipe utilizando Microsoft Fabric para todo o processo de ETL "
            "e análise de dados, com dashboards em Power BI para apoiar políticas públicas a partir "
            "de tendências de mortalidade, internações e atendimentos ambulatoriais."
        ),
        "steps": [],
        "tags": ["Power BI", "Microsoft Fabric", "ETL", "PUC Minas"],
        "url": "https://www.linkedin.com/posts/gian-henrique_pucminas-powerbi-etl-ugcPost-7382929412842835968-U43x/",
    },
    {
        "icon": "map-pin",
        "title": "Cálculo de Cidades Dentro de um Raio com Python para o Power BI",
        "desc": (
            "Em um projeto, precisei desenhar um raio no Power BI e não encontrei uma opção nativa "
            "que atendesse — então resolvi com Python orientado por IA. Solução para calcular cidades "
            "dentro de um raio (neste exemplo, 600 km) a partir de um ponto de referência, útil para "
            "logística, marketing geográfico ou planejamento urbano."
        ),
        "steps": [
            "Definir as coordenadas do ponto de referência (Manaus, no exemplo)",
            "Carregar um dataset de cidades com latitude e longitude",
            "Calcular a distância com a função geodesic da biblioteca Geopy",
            "Filtrar as cidades dentro do raio de 600 km",
            "Exportar o resultado para Excel e visualizar o raio no mapa do Power BI",
        ],
        "tags": ["Python", "Geopy", "Pandas", "OpenPyXL", "Power BI"],
        "url": "https://www.linkedin.com/posts/gian-henrique_ol%C3%A1-provavelmente-voc%C3%AA-deve-estar-se-perguntando-ugcPost-7239805669359386625-gBvh/",
    },
    {
        "icon": "palette",
        "title": "Dashboard Comparativo: Auxílio Brasil x Bolsa Família",
        "desc": (
            "Reformulação em equipe de um dashboard comparativo entre os programas Auxílio Brasil e "
            "Bolsa Família. Refizemos o layout utilizando o Figma e acrescentamos dicas de ferramenta "
            "(tooltips) no Power BI para aprofundar a análise de distribuição de parcelas, "
            "benefícios e total de pessoas por região e UF."
        ),
        "steps": [],
        "tags": ["Power BI", "Figma", "UX para Dados"],
        "url": "https://www.linkedin.com/posts/gian-henrique_bom-gente-est%C3%A1-ai-o-resultado-final-neste-ugcPost-7137973119444594688-DHkf/",
    },
    {
        "icon": "bot",
        "title": "Automação de Planilhas Excel com Inteligência Artificial",
        "desc": (
            "Uso de IA generativa para acelerar rotinas em Excel — criação assistida de fórmulas, "
            "scripts e macros (VBA/Office Scripts), reduzindo o tempo manual em relatórios "
            "recorrentes e aumentando a confiabilidade das planilhas."
        ),
        "steps": [],
        "tags": ["Excel", "VBA", "IA Generativa", "Automação"],
        "url": None,
    },
]

PROJECTS = [
    {
        "title": "Dashboard Executivo — Acidentes de Trânsito (PRF)",
        "status": "Finalizado",
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
    {
        "title": "Envelhecimento Populacional e Impactos no SUS",
        "status": "Finalizado",
        "desc": (
            "Projeto acadêmico em grupo (PUC Minas) para construção de uma arquitetura de dados "
            "em nuvem voltada à análise dos impactos do envelhecimento populacional brasileiro no "
            "Sistema Único de Saúde (SUS). Integração de projeções demográficas do IBGE com dados "
            "públicos de saúde para identificar tendências de mortalidade, internações e atendimentos "
            "ambulatoriais, apoiando previsões de demanda futura por serviços de saúde."
        ),
        "metrics": [
            {"v": "6", "l": "Fases do projeto"},
            {"v": "2", "l": "Fontes integradas (IBGE + SUS)"},
            {"v": "6", "l": "Integrantes + orientador"},
        ],
        "tech": ["Python", "Jupyter Notebook", "Machine Learning", "Cloud", "SQL", "ETL"],
        "url": "https://github.com/Tecnologia-em-Banco-de-Dados-PUC-Minas/eixo5_grupo1_20252",
        "highlights": [
            "Arquitetura de dados em nuvem para análise de saúde pública",
            "Documentação de contexto, coleta e pré-processamento de dados estruturados",
            "Modelos de Machine Learning para identificar tendências de mortalidade e internações",
            "Análise de resultados e otimização do pipeline em equipe multidisciplinar",
            "Trabalho colaborativo com 6 integrantes e orientação acadêmica",
        ],
    },
]

EXPERIENCE = [
    {
        "date": "Dez 2025 – o momento · 7 meses",
        "role": "Analista Administrativo Pleno",
        "org": "TORA · Tempo integral · Contagem, MG",
        "desc": (
            "Atuo no desenvolvimento de soluções analíticas em Power BI que suportam a tomada de "
            "decisão operacional e estratégica da empresa.<br><br>"
            "→ Desenvolvimento de dashboards interativos com KPIs críticos para gestão, utilizando "
            "DAX avançado e modelagem dimensional.<br>"
            "→ Implementação de pipelines de automação de dados que eliminam processos manuais "
            "repetitivos, aumentando a eficiência das equipes.<br>"
            "→ Integração de múltiplas fontes de dados em ambiente Microsoft com aplicação de boas "
            "práticas de ETL e governança.<br>"
            "→ Atuação como ponte entre as áreas de negócio e TI, traduzindo demandas em soluções "
            "escaláveis e de baixa manutenção.<br><br>"
            "Stack: Power BI · DAX · Power Automate · Excel · Automação de Processos"
        ),
    },
    {
        "date": "Jan 2025 – Dez 2025 · 1 ano",
        "role": "Analista Administrativo Jr.",
        "org": "Grupo SADA · Tempo integral · Betim, MG",
        "desc": (
            "Primeira experiência profissional com análise de dados aplicada ao ambiente corporativo, "
            "desenvolvendo habilidades analíticas e de estruturação de informações.<br><br>"
            "→ Geração de relatórios gerenciais e controles em Excel para acompanhamento de "
            "indicadores administrativos e operacionais.<br>"
            "→ Organização e tratamento de bases de dados para alimentar processos de tomada de "
            "decisão interna.<br>"
            "→ Automação de tarefas recorrentes, reduzindo o tempo operacional da equipe.<br>"
            "→ Atuação no suporte analítico às áreas administrativas com foco em eficiência e "
            "qualidade das informações.<br><br>"
            "Stack: Excel Avançado · SQL · Análise de Dados · Processos Administrativos"
        ),
    },
]

EDUCATION = [
    {
        "date": "Mai 2026 – Mai 2027",
        "role": "Pós-graduação Lato Sensu — MBA, IA, Data Science e Big Data para Negócios",
        "org": "Ibmec",
        "desc": "Especialização em Inteligência Artificial, Data Science e Big Data aplicados a negócios, com foco em bancos de dados relacionais.",
    },
    {
        "date": "Ago 2023 – Dez 2025",
        "role": "Curso Superior de Tecnologia (CST), Banco de Dados",
        "org": "PUC Minas",
        "desc": "Formação superior com foco em banco de dados, resolução de problemas e documentação, somando mais de 20 competências desenvolvidas em projetos reais.",
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
          <span class="btn-ico">{ICONS['linkedin']}</span>LinkedIn
        </a>
        <a href="{PROFILE['github']}" target="_blank" class="btn-outline">
          <span class="btn-ico">{ICONS['github']}</span>GitHub
        </a>
        <a href="mailto:{PROFILE['email']}" class="btn-outline">
          <span class="btn-ico">{ICONS['mail']}</span>Contato
        </a>
      </div>
    </div>
    <div>
      <div class="hero-avatar-wrap">
        <img src="{PROFILE['avatar']}" class="hero-avatar" alt="Gian Henrique" loading="lazy" />
      </div>
    </div>
  </div>
</section>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# NAV PILLS
# ─────────────────────────────────────────
st.markdown("""
<nav class="nav-container">
  <input type="checkbox" id="nav-toggle" class="nav-toggle-input">
  <div class="nav-bar">
    <label for="nav-toggle" class="nav-toggle-btn" aria-label="Abrir menu">
      <span></span><span></span><span></span>
    </label>
    <div class="nav-pills">
      <a class="nav-pill active" href="#sobre">Sobre</a>
      <a class="nav-pill" href="#habilidades">Habilidades</a>
      <a class="nav-pill" href="#projetos">Projetos</a>
      <a class="nav-pill" href="#experiencia">Experiência</a>
      <a class="nav-pill" href="#contato">Contato</a>
    </div>
  </div>
</nav>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────
# STATS (números de impacto)
# ─────────────────────────────────────────
STATS = [
    {"icon": "database", "number": "1M+", "label": "Registros processados"},
    {"icon": "gear", "number": "6", "label": "Módulos analíticos entregues"},
    {"icon": "code", "number": "100%", "label": "Python open source"},
    {"icon": "zap", "number": "26 MB", "label": "de 350 MB (otimização ETL)"},
]

stats_html = '<div class="section"><div class="stats-grid">'
for s in STATS:
    stats_html += f"""
<div class="stat-card">
  <span class="stat-icon">{ICONS[s['icon']]}</span>
  <span class="stat-number">{s['number']}</span>
  <div class="stat-label">{s['label']}</div>
</div>
""".strip()
stats_html += "</div></div>"
st.markdown(stats_html, unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)


# ─────────────────────────────────────────
# PRINCIPAIS COMPETÊNCIAS
# ─────────────────────────────────────────
TOP_SKILLS = [
    ("trending-up", "Power BI"),
    ("code", "Python"),
    ("database", "SQL"),
    ("gear", "ETL / ELT"),
    ("brain", "Machine Learning"),
    ("zap", "IA Generativa"),
    ("pulse", "Dashboards Executivos"),
    ("bot", "Automação de Processos"),
]

top_skills_html = '<div class="section" style="padding-bottom:0"><div class="section-label">Resumo Rápido</div><h2 class="section-title">Principais Competências</h2><div class="highlight-strip">'
for icon_key, label in TOP_SKILLS:
    top_skills_html += f'<span class="highlight-chip"><span class="highlight-chip-icon">{ICONS[icon_key]}</span>{label}</span>'
top_skills_html += "</div></div>"
st.markdown(top_skills_html, unsafe_allow_html=True)

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
    values = [70, 85, 85, 95, 75, 70]

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],
        theta=categories + [categories[0]],
        fill="toself",
        fillcolor="rgba(232,134,125,0.18)",
        line=dict(color=COLORS["accent"], width=2.5),
        name="Nível",
        hovertemplate="%{theta}: %{r}%<extra></extra>",
    ))

    fig.update_layout(
        polar=dict(
            bgcolor="rgba(20,18,16,0.8)",
            radialaxis=dict(
                visible=True, range=[0, 100],
                gridcolor=COLORS["border"],
                tickcolor=COLORS["border"],
                tickfont=dict(color=COLORS["text_3"], size=10),
                tickvals=[25, 50, 75, 100],
            ),
            angularaxis=dict(
                gridcolor=COLORS["border"],
                tickfont=dict(color=COLORS["text_2"], size=13),
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
    for cat in SKILLS:
        tags_html = "".join(f'<span class="skill-tag">{t}</span>' for t in cat["tags"])
        skills_html += f"""
<div class="skill-category">
  <span class="skill-cat-icon">{ICONS[cat['icon']]}</span>
  <div class="skill-cat-title">{cat['title']}</div>
  {tags_html}
</div>
""".strip()
    skills_html += "</div>"
    st.markdown(skills_html, unsafe_allow_html=True)

# Power BI na prática — experiências compartilhadas no LinkedIn
# IMPORTANTE: todo o bloco (cabeçalho + cards) é montado em UMA única string e
# enviado em UMA única chamada st.markdown(). Cada chamada a st.markdown() é
# inserida como um nó de DOM independente — abrir uma div numa chamada e
# fechá-la só numa chamada seguinte não funciona (as divs órfãs de uma
# chamada não “casam” com fechamentos de outra), o que fazia o HTML aparecer
# como texto bruto na tela.
cards_html = f"""
<div class="section-alt" style="padding-top:0">
  <div class="section-inner">
    <h3 style="color:{COLORS['text_1']};font-size:18px;font-weight:600;margin:8px 0 4px">Power BI na Prática</h3>
    <p style="color:{COLORS['text_3']};font-size:14px;margin-bottom:0">Experiências reais compartilhadas no LinkedIn.</p>
    <div class="linkedin-grid">
"""
for item in POWERBI_HIGHLIGHTS:
    tags_html = "".join(f'<span class="skill-tag">{t}</span>' for t in item["tags"])
    steps_html = (
        f'<ol style="padding-left:18px;margin:0 0 14px;color:{COLORS["text_2"]};font-size:12px;line-height:1.7">'
        + "".join(f"<li>{s}</li>" for s in item["steps"])
        + "</ol>"
        if item["steps"] else ""
    )
    link_html = (
        f'<a href="{item["url"]}" target="_blank" class="linkedin-card-link">'
        f'<span class="linkedin-card-link-icon">{ICONS["linkedin"]}</span>Ver Projeto</a>'
        if item["url"] else
        '<span class="linkedin-card-link linkedin-card-link-disabled">'
        f'<span class="linkedin-card-link-icon">{ICONS["bot"]}</span>Aplicação prática contínua</span>'
    )
    cards_html += f"""
<div class="linkedin-card">
  <span class="skill-cat-icon">{ICONS[item['icon']]}</span>
  <div class="linkedin-card-title">{item['title']}</div>
  <div class="linkedin-card-desc">{item['desc']}</div>
  {steps_html}
  <div class="linkedin-card-tags">{tags_html}</div>
  {link_html}
</div>
""".strip()
cards_html += "</div></div></div>"
st.markdown(cards_html, unsafe_allow_html=True)

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

for proj_idx, proj in enumerate(PROJECTS):
    metrics_html = "".join(
        f'<div class="metric-box"><div class="metric-value">{m["v"]}</div><div class="metric-label">{m["l"]}</div></div>'
        for m in proj["metrics"]
    )
    tech_html = "".join(f'<span class="tech-tag">{t}</span>' for t in proj["tech"])
    hl_html = "".join(f'<li style="color:{COLORS["text_2"]};font-size:14px;margin-bottom:6px;line-height:1.6">{h}</li>' for h in proj["highlights"])
    badge_class = "project-badge finalizado" if proj["status"].lower() == "finalizado" else "project-badge"
    toggle_id = f"ver-mais-{proj_idx}"

    st.markdown(f"""
    <div class="section" style="padding-top:0; padding-bottom:48px;">
      <div class="project-card">
        <input type="checkbox" id="{toggle_id}" class="ver-mais-input">
        <div class="project-header">
          <div class="{badge_class}">{proj['status']}</div>
          <div class="project-name">{proj['title']}</div>
          <div class="project-desc truncate">{proj['desc']}</div>
          <label for="{toggle_id}" class="ver-mais-label">Ver mais ▾</label>
        </div>
        <div class="project-body">
          <div class="project-metrics">{metrics_html}</div>
          <div style="margin-top:20px">
            <div style="font-size:13px;color:{COLORS['text_3']};font-weight:600;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px">Destaques técnicos</div>
            <ul style="padding-left:18px;margin:0">{hl_html}</ul>
          </div>
          <div class="project-tech">{tech_html}</div>
          <a href="{proj['url']}" target="_blank" class="project-link">Ver no GitHub →</a>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

# Gráfico demo do projeto (dados simulados tipo PRF)
st.markdown(f"""
<div class="section-alt">
  <div class="section-inner">
    <div class="section-label">Projeto em Ação</div>
    <h3 style="color:{COLORS['text_1']};font-size:22px;font-weight:600;margin-bottom:4px">Prévia: Acidentes PRF 2022–2025</h3>
    <p style="color:{COLORS['text_3']};font-size:14px;margin-bottom:24px">Visualizações representativas do dashboard executivo.</p>
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
        marker_color=COLORS["neutral_bar"],
        hovertemplate="%{x}: %{y:,.0f} acidentes<extra></extra>",
    ))
    fig2.add_trace(go.Scatter(
        x=anos, y=mortos, name="Óbitos",
        yaxis="y2", mode="lines+markers",
        line=dict(color=COLORS["accent"], width=3),
        marker=dict(size=8),
        hovertemplate="%{x}: %{y:,.0f} óbitos<extra></extra>",
    ))
    fig2.update_layout(
        title=dict(text="Evolução Anual — Acidentes e Óbitos", font=dict(color=COLORS["text_1"], size=15)),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(20,18,16,0.6)",
        xaxis=dict(gridcolor=COLORS["border"], tickfont=dict(color=COLORS["text_3"])),
        yaxis=dict(gridcolor=COLORS["border"], tickfont=dict(color=COLORS["text_3"]), title="Acidentes"),
        yaxis2=dict(overlaying="y", side="right", tickfont=dict(color=COLORS["accent_light"]), title="Óbitos"),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color=COLORS["text_2"])),
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
            colorscale=[[0, COLORS["border"]], [1, COLORS["accent"]]],
        ),
        hovertemplate="%{y}: %{x}%<extra></extra>",
        text=[f"{v}%" for v in valores],
        textposition="outside",
        textfont=dict(color=COLORS["text_2"], size=12),
    ))
    fig3.update_layout(
        title=dict(text="Top 5 Causas de Acidentes (%)", font=dict(color=COLORS["text_1"], size=15)),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(20,18,16,0.6)",
        xaxis=dict(gridcolor=COLORS["border"], tickfont=dict(color=COLORS["text_3"]), showticklabels=False),
        yaxis=dict(gridcolor=COLORS["border"], tickfont=dict(color=COLORS["text_2"])),
        margin=dict(l=10, r=60, t=48, b=10),
        height=320,
    )
    st.plotly_chart(fig3, use_container_width=True, config={"displayModeBar": False})

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Resultado do projeto SUS — ilustração baseada na documentação (etapas 5 e 6 do projeto)
st.markdown(f"""
<div class="section-alt">
  <div class="section-inner">
    <div class="section-label">Projeto em Ação</div>
    <h3 style="color:{COLORS['text_1']};font-size:22px;font-weight:600;margin-bottom:4px">Resultado: Envelhecimento Populacional e Impactos no SUS</h3>
    <p style="color:{COLORS['text_3']};font-size:14px;margin-bottom:24px">Ilustração baseada nas etapas de Análise dos Resultados e Otimização documentadas no projeto — valores representativos da metodologia aplicada.</p>
  </div>
</div>
""", unsafe_allow_html=True)

col_sus1, col_sus2 = st.columns(2, gap="medium")

with col_sus1:
    faixas = ["60–69 anos", "70–79 anos", "80+ anos"]
    proporcao = [38, 34, 28]

    fig4 = go.Figure(go.Bar(
        x=faixas, y=proporcao,
        marker_color=COLORS["accent"],
        hovertemplate="%{x}: %{y}% dos óbitos<extra></extra>",
        text=[f"{v}%" for v in proporcao],
        textposition="outside",
        textfont=dict(color=COLORS["text_2"], size=12),
    ))
    fig4.update_layout(
        title=dict(text="Distribuição de Óbitos por Faixa Etária 60+ (%)", font=dict(color=COLORS["text_1"], size=14)),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(20,18,16,0.6)",
        xaxis=dict(gridcolor=COLORS["border"], tickfont=dict(color=COLORS["text_2"])),
        yaxis=dict(gridcolor=COLORS["border"], tickfont=dict(color=COLORS["text_3"]), showticklabels=False),
        margin=dict(l=10, r=10, t=48, b=10),
        height=320,
    )
    st.plotly_chart(fig4, use_container_width=True, config={"displayModeBar": False})

with col_sus2:
    bases = ["Mortalidade (Faixa Etária + CID-10)", "Ambulatorial (Município)", "Internações (Município)"]
    relevancia = [82, 76, 54]

    fig5 = go.Figure(go.Bar(
        x=relevancia, y=bases, orientation="h",
        marker=dict(color=relevancia, colorscale=[[0, COLORS["border"]], [1, COLORS["accent"]]]),
        hovertemplate="%{y}: relevância %{x}<extra></extra>",
        text=[f"{v}" for v in relevancia],
        textposition="outside",
        textfont=dict(color=COLORS["text_2"], size=12),
    ))
    fig5.update_layout(
        title=dict(text="Principal Determinante por Base de Dados", font=dict(color=COLORS["text_1"], size=14)),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(20,18,16,0.6)",
        xaxis=dict(gridcolor=COLORS["border"], tickfont=dict(color=COLORS["text_3"]), showticklabels=False),
        yaxis=dict(gridcolor=COLORS["border"], tickfont=dict(color=COLORS["text_2"], size=11), automargin=True),
        margin=dict(l=10, r=50, t=48, b=10),
        height=320,
    )
    st.plotly_chart(fig5, use_container_width=True, config={"displayModeBar": False})

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)


# ─────────────────────────────────────────
# EXPERIÊNCIA
# ─────────────────────────────────────────
st.markdown('<div id="experiencia"></div>', unsafe_allow_html=True)
st.markdown(f"""
<div class="section">
  <div class="section-label">Trajetória</div>
  <h2 class="section-title">Experiência & Formação</h2>
  <p class="section-subtitle">Construindo expertise através de cargos administrativos com foco em dados e formação acadêmica sólida.</p>
  <h3 style="color:{COLORS['text_1']};font-size:18px;font-weight:600;margin-bottom:20px">Experiência Profissional</h3>
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

st.markdown(f"""
  </div>
  <h3 style="color:{COLORS['text_1']};font-size:18px;font-weight:600;margin:16px 0 20px">Formação Acadêmica</h3>
  <div class="timeline">
""", unsafe_allow_html=True)

for edu in EDUCATION:
    st.markdown(f"""
    <div class="timeline-item">
      <div class="timeline-date">{edu['date']}</div>
      <div class="timeline-role">{edu['role']}</div>
      <div class="timeline-org">{edu['org']}</div>
      <div class="timeline-desc">{edu['desc']}</div>
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
        <div class="contact-icon">{ICONS['mail']}</div>
        <div>
          <div class="contact-label">E-mail</div>
          <div class="contact-value">{PROFILE['email']}</div>
        </div>
      </a>
      <a href="{PROFILE['linkedin']}" target="_blank" class="contact-card">
        <div class="contact-icon">{ICONS['linkedin']}</div>
        <div>
          <div class="contact-label">LinkedIn</div>
          <div class="contact-value">linkedin.com/in/gian-henrique</div>
        </div>
      </a>
      <a href="{PROFILE['github']}" target="_blank" class="contact-card">
        <div class="contact-icon">{ICONS['github']}</div>
        <div>
          <div class="contact-label">GitHub</div>
          <div class="contact-value">github.com/GianHQA</div>
        </div>
      </a>
      <a href="https://wa.me/5531995560604" class="contact-card">
        <div class="contact-icon">{ICONS['whatsapp']}</div>
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
