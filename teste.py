import streamlit as st

def cadastro_notas():
    st.title("Cadastro de Notas Fiscais")

    st.header("Cadastro Manual")
    numero_nota = st.text_input("Número da Nota")
    valor_total = st.text_input("Valor Total")

    if st.button("Cadastrar Manualmente"):
        st.success(f"Nota cadastrada manualmente:\nNúmero: {numero_nota}\nValor: {valor_total}")

    st.header("Cadastro por XML")
    uploaded_file = st.file_uploader("Selecione um arquivo XML")

    if uploaded_file is not None:
        # Aqui você pode processar o XML
        st.success("Arquivo XML selecionado.")

if __name__ == "__main__":
    cadastro_notas()
