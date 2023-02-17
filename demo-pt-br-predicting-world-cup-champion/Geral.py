import numpy as np
import streamlit as st
import pandas as pd

from dataapp import *

favicon_img_link = "https://s3.amazonaws.com/gupy5/production/companies/1286/career/2122/images/2022-01-05_13-07_logo.png"
page_title = "Dadosfera Data App"
DataApp.update_page_config(page_title, favicon_img_link)
DataApp.update_visibility()
DataApp.add_logo()
st.title("Copa do Mundo 2022")
st.header("Prevendo a fase final com a Dadosfera")

st.markdown('**Se interessou pelo modelo de previsão da Copa?** Então não deixe de conferir o [webinar gratuito](https://mkthb.dadosfera.ai/pt-br/prevendo-campeao-copa-com-dadosfera) sobre ele! Lá explicamos todos os detalhes sobre como construímos o modelo preditivo que indicou esse resultado.')

with st.sidebar:
    with st.expander("ℹ️ - Simulação da Copa do Mundo", expanded=True):
            st.write("""     
        -   Ao lado temos uma simulação dos jogos da Copa do Mundo de 2022. Para cada jogo, temos um vencedor e a probabilidade de vitória deste time.
        
        - A probabilidade foi calculada com base em um modelo de Gradient Boosting, utilizando dados do [ranking da Fifa](https://www.kaggle.com/datasets/cashncarry/fifaworldranking) e [histórico de jogos anteriores (fonte extraoficial)](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017). Você pode conferir o projeto que serviu de inspiração para a criação do modelo no [Kaggle](https://www.kaggle.com/code/sslp23/predicting-fifa-2022-world-cup-with-ml).
            """)
            
def space(skipped_lines):
    for i in range(skipped_lines): st.markdown('')
    
flags = {'Brasil':':flag-br:','Alemanha':':flag-de:','Holanda':':flag-nl:','Argentina':':flag-ar:','Espanha':':flag-es:','Equador':':flag-ec:','Mexico':':flag-mx:','Suíça':':flag-ch:','Estados Unidos':':flag-us:','Dinamarca':'','Croácia':':flag-hr:','Uruguai':':flag-uy:','Inglaterra':':flag-england:','França':':flag-fr:','Bélgica':':flag-be:','Portugal':':flag-pt:','Dinamarca':':flag-dk:'}
         
    
st.markdown("""---""")    

col0, col1, col2, col3, col4, col5, col6, col7,col8  = st.columns(9)  
with col0:
    st.write(flags['Holanda']+' Holanda')
    st.markdown("""---""")
    st.write(flags['Estados Unidos']+' Estados Unidos')
    space(2)
    st.write(flags['Argentina']+' Argentina')
    st.markdown("""---""")
    st.write(flags['Dinamarca']+' Dinamarca')
    space(2)
    st.write(flags['Espanha']+' Espanha')
    st.markdown("""---""")
    st.write(flags['Croácia']+' Croácia')
    space(2)
    st.write(flags['Brasil']+' Brasil')
    st.markdown("""---""")
    st.write(flags['Uruguai']+' Uruguai')
    
with col1:
    st.write(flags['Holanda']+' Holanda')
    st.markdown("""<sub><sup>61% de prob</sub></sup>""",unsafe_allow_html=True)
    space(1)
    st.markdown("""---""")
    space(1)
    st.write(flags['Argentina']+' Argentina')
    st.markdown("""<sub><sup>60% de prob</sub></sup>""",unsafe_allow_html=True)
    space(5)
    st.write(flags['Espanha']+' Espanha')
    st.markdown("""<sub><sup>59% de prob</sub></sup>""",unsafe_allow_html=True)
    space(1)
    st.markdown("""---""")
    space(1)
    st.write(flags['Brasil']+' Brasil')
    st.markdown("""<sub><sup>69% de prob</sub></sup>""",unsafe_allow_html=True)
    
with col2:
    st.write(flags['Argentina']+' Argentina')
    st.markdown("""<sub><sup>50% de prob</sub></sup>""",unsafe_allow_html=True)
    space(5)
    st.markdown("""---""")
    space(8)
    st.write(flags['Brasil']+' Brasil')
    st.markdown("""<sub><sup>64% de prob</sub></sup>""",unsafe_allow_html=True)  
    
with col3:
    st.write(flags['Brasil']+' Brasil')
    st.markdown("""<sub><sup>60% de prob</sub></sup>""",unsafe_allow_html=True)
    
with col4:
    st.header(flags['Brasil']+' Brasil')
    st.markdown("""<sub><sup>67% de prob</sub></sup>""",unsafe_allow_html=True)

with col5:
    st.write(flags['Alemanha']+' Alemanha')
    st.markdown("""<sub><sup>51% de prob</sub></sup>""",unsafe_allow_html=True)
    
with col6:
    st.write(flags['França']+' França')
    st.markdown("""<sub><sup>55% de prob</sub></sup>""",unsafe_allow_html=True)
    space(5)
    st.markdown("""---""")
    space(8)
    st.write(flags['Alemanha']+' Alemanha')
    st.markdown("""<sub><sup>50% de prob</sub></sup>""", unsafe_allow_html=True)
    
with col7:
    st.write(flags['Inglaterra']+' Inglaterra')
    st.markdown("""<sub><sup>74% de prob</sub></sup>""",unsafe_allow_html=True)
    space(1)
    st.markdown("""---""")
    space(1)
    st.write(flags['França']+' França')
    st.markdown("""<sub><sup>63% de prob</sub></sup>""",unsafe_allow_html=True)
    space(6)
    st.write(flags['Alemanha']+' Alemanha')
    st.markdown("""<sub><sup>62% de prob</sub></sup>""",unsafe_allow_html=True)
    space(1)
    st.markdown("""---""")
    space(1)
    st.write(flags['Portugal']+' Portugal')
    st.markdown("""<sub><sup>68% de prob</sub></sup>""",unsafe_allow_html=True)

with col8:
    st.write(flags['Equador']+' Equador')
    st.markdown("""---""")
    st.write(flags['Inglaterra']+' Inglaterra')
    space(2)
    st.write(flags['Mexico']+' México')
    st.markdown("""---""")
    st.write(flags['França']+' França')
    space(2)
    st.write(flags['Alemanha']+' Alemanha')
    st.markdown("""---""")
    st.write(flags['Bélgica']+' Bélgica')
    space(2)
    st.write(flags['Suíça']+' Suíça')
    st.markdown("""---""")
    st.write(flags['Portugal']+' Portugal')
    
st.markdown("""---""")  

st.markdown("""
            <style>
                [data-testid="column"] {
                    margin: auto;
                    text-align: center;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )


# TABELA
# st.header("Oitavas de final")

# d = {'Time 1': ['Holanda', 'Argentina','Espanha','Brasil','Equador','Mexico','Alemanha','Suíça'], 'Time 2': ['Estados Unidos', 'Dinamarca', 'Croácia', 'Uruguai','Inglaterra','França','Bélgica','Portugal'], 'Vencedor': ['Holanda', 'Argentina','Espanha','Brasil','Inglaterra','França','Alemanha','Portugal'], 'Probabilidade':[0.61, 0.60, 0.59, 0.69, 0.74, 0.63, 0.62, 0.68]}
# df = pd.DataFrame(data=d)
# st.table(df)

# st.header("Quartas de final")

# d = {'Time 1': ['Holanda','Espanha','Inglaterra','Alemanha'], 'Time 2': ['Argentina', 'Brasil','França','Portugal'], 'Vencedor': ['Argentina', 'Brasil','França','Alemanha'], 'Probabilidade':[0.50, 0.64, 0.55, 0.50]}
# df = pd.DataFrame(data=d)

# st.table(df)

# st.header("Semi-final")

# d = {'Time 1': ['Argentina','França'], 'Time 2': ['Brasil', 'Alemanha'], 'Vencedor': ['Brasil', 'Alemanha'], 'Probabilidade':[0.60, 0.51]}
# df = pd.DataFrame(data=d)

# st.table(df)

# st.header("Final")

# d = {'Time 1': ['Brasil'], 'Time 2': ['Alemanha'], 'Vencedor': ['Brasil'], 'Probabilidade':[0.67]}
# df = pd.DataFrame(data=d)

# st.table(df)