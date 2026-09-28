import streamlit as st
import pandas as pd
#criar titulo do aplicativo
st.title("biblioteca de livros")

import pandas as pd

#quero montar tres dataframes: livros, estudantes e emprestimos. estes datraframes são
#necessaris para uma biblioteca
#o dataframe livros deve ter as seguintes colunas: ISBN, titulo, autor, ano publicado, genero
#estudantes deve conter as seguintes colunas: id_emprestimo, matricula_estudante, data_emprestimo, data_devolução

livros = pd.DataFrame(columns=['ISBN', 'titulo', 'autor', 'ano_publicado', 'genero'])
estudantes = pd.DataFrame(columns=['id_emprestimo', 'matricula_estudante', 'data_emprestimo', 'data_devolução'])
emprestimos = pd.DataFrame(columns=['id_emprestimo', 'matricula_estudante', 'ISBN', 'data_emprestimo', 'data_devolução'])



novos_livros = pd.DataFrame([
    {'ISBN' : '978 -3 - 16 - 148410-0', 'titulo': 'Livro A' , 'autor': 'autor A', 'ano_publicado': 2020, 'genero': 'genero A'},
    {'ISBN' : '978 -3 - 16 - 148410-1', 'titulo': 'Livro B' , 'autor': 'autor B', 'ano_publicado': 2021, 'genero': 'genero B'}
])

estudantes = pd.DataFrame([
    {'id_emprestimo': '0025', 'matricula_estudante': '2025.001-1', 'data_emprestimo': '15/09/2026', 'data_devolução': '15/10/2026'},
    {'id_emprestimo': '0026', 'matricula_estudante': '2025.002-2', 'data_emprestimo': '16/09/2026', 'data_devolução': '05/10/2026'}
])

emprestimos = pd.DataFrame([
    {'id_emprestimo': '0025' , 'matricula_estudante': '2025.001-1', 'ISBN': '978 -3 - 16 - 148410-0', 'data_emprestimo': '15/09/2026', 'data_devolução': '15/10/2026'},
    {'id_emprestimo': '0026' , 'matricula_estudante': '2025.002-2', 'ISBN': '978 -3 - 16 - 148410-1', 'data_emprestimo': '16/09/2026', 'data_devolução': '05/10/2026'}
])


#quero ter um sidebar com as opções de menu para o usuario escolher entre "livros", "estudantes", "emprestimos"

menu = st.sidebar.selectbox("selecione uma opção", ["livros", "estudantes", "emprestimos"])
if menu == "livros":
    st.subheader("lista de livros")
    st.dataframe(novos_livros)
elif menu == "estudantes":
    st.subheader("Lista de Estudantes")
    st.dataframe(estudantes)
elif menu == "emprestimos":
    st.subheader("emprestimos")
    st.dataframe(emprestimos)
    
    

