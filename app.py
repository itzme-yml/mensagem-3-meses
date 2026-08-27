import streamlit as st
import base64

st.set_page_config(
    page_title="Para você",
    page_icon="🔒",
    layout="centered"
)

SENHA_CORRETA = "260526"


# =========================
# CARREGAR IMAGEM
# =========================

def imagem_base64(caminho):
    with open(caminho, "rb") as arquivo:
        return base64.b64encode(arquivo.read()).decode()


try:
    imagem = imagem_base64("imagem.jpg")
except FileNotFoundError:
    imagem = None


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

    if imagem:
        st.image(f"data:image/jpeg;base64,{imagem}")
    else:
        st.warning(
            "A imagem não foi encontrada. "
            "Coloque 'IMG_20260526_172208_239.jpg' na mesma pasta do app.py."
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
