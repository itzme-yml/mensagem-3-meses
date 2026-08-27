import streamlit as st

st.set_page_config(
    page_title="Para você",
    page_icon="🔒",
    layout="centered"
)

SENHA_CORRETA = "260526"
NOME_DA_IMAGEM = "IMG_20260526_172208_239.jpg"


# =========================
# ESTILO
# =========================

st.markdown("""
<style>

.stApp {
    background: #111111;
    color: white;
}

.block-container {
    max-width: 420px;
    min-height: 90vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding-top: 5vh;
}

div[data-testid="stTextInput"] input {
    text-align: center;
    border-radius: 12px;
    padding: 12px;
}

div[data-testid="stButton"] button {
    width: 100%;
    border-radius: 12px;
    font-weight: bold;
    padding: 10px;
}

</style>
""", unsafe_allow_html=True)


# =========================
# CONTROLE DA TELA
# =========================

if "desbloqueado" not in st.session_state:
    st.session_state.desbloqueado = False


# =========================
# TELA DE SENHA
# =========================

if not st.session_state.desbloqueado:

    st.write("🔒")
    st.header("Conteúdo bloqueado")
    st.write("Digite a senha para desbloquear este conteúdo.")

    senha = st.text_input(
        "Senha",
        type="password",
        placeholder="Digite a senha",
        label_visibility="collapsed"
    )

    if st.button("DESBLOQUEAR"):

        if senha == SENHA_CORRETA:

            st.session_state.desbloqueado = True
            st.rerun()

        else:

            st.error("Senha incorreta.")


# =========================
# TELA COM A MENSAGEM
# =========================

else:

    try:
        st.image(NOME_DA_IMAGEM, use_container_width=True)
    except Exception:
        st.warning(
            f"A imagem '{NOME_DA_IMAGEM}' não foi encontrada no repositório."
        )

    st.write("""
    Meu amor, hoje a gente completa 3 meses juntas.

    Nesse tempo, você se tornou uma pessoa muito especial na minha
    vida, alguém que eu amo ter por perto e com quem eu quero
    continuar vivendo muitos momentos.

    Obrigada por cada conversa, cada risada, cada carinho e por todos
    os momentos que a gente já compartilhou. Eu amo poder chamar você
    de minha namorada.

    Feliz 3 meses para nós. Eu te amo muito, meu amor💖
    """)
