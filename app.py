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

.tela {
    width: 100%;
    text-align: center;
    animation: aparecer 0.8s ease;
}

.cadeado {
    font-size: 70px;
    margin-bottom: 20px;
}

.titulo {
    font-size: 28px;
    font-weight: bold;
    color: white;
    margin-bottom: 15px;
}

.descricao {
    color: #cccccc;
    font-size: 16px;
    line-height: 1.6;
    margin-bottom: 20px;
}

.imagem {
    width: 100%;
    max-height: 400px;
    object-fit: cover;
    border-radius: 18px;
    margin-bottom: 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    animation: imagem 1.2s ease;
}

.mensagem {
    color: #eeeeee;
    font-size: 17px;
    line-height: 1.7;
    text-align: center;
    animation: mensagem 1.5s ease;
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

@keyframes aparecer {
    from {
        opacity: 0;
        transform: scale(0.85);
    }

    to {
        opacity: 1;
        transform: scale(1);
    }
}

@keyframes imagem {
    from {
        opacity: 0;
        transform: scale(0.9);
    }

    to {
        opacity: 1;
        transform: scale(1);
    }
}

@keyframes mensagem {
    from {
        opacity: 0;
        transform: translateY(15px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
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

    st.markdown("""
    <div class="tela">

        <div class="cadeado">🔒</div>

        <div class="titulo">
            Conteúdo bloqueado
        </div>

        <div class="descricao">
            Digite a senha para desbloquear este conteúdo.
        </div>

    </div>
    """, unsafe_allow_html=True)

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

    st.markdown("""
    <div class="tela">
    """, unsafe_allow_html=True)

    if imagem:

        st.markdown(
            f"""
            <img
                src="data:image/jpeg;base64,{imagem}"
                class="imagem"
            >
            """,
            unsafe_allow_html=True
        )

    else:

        st.warning(
            "A imagem não foi encontrada. "
            "Coloque 'imagem.jpg' na mesma pasta do app.py."
        )

    st.markdown("""
        <div class="mensagem">

            Meu amor, hoje a gente completa 3 meses juntas.

            <br><br>

            Nesse tempo, você se tornou uma pessoa muito especial na minha
            vida, alguém que eu amo ter por perto e com quem eu quero
            continuar vivendo muitos momentos.

            <br><br>

            Obrigada por cada conversa, cada risada, cada carinho e por todos
            os momentos que a gente já compartilhou. Eu amo poder chamar você
            de minha namorada.

            <br><br>

            Feliz 3 meses para nós. Eu te amo muito, meu amor💖

        </div>

    </div>
    """, unsafe_allow_html=True)
