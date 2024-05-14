import streamlit as st
import Utils as ut

def Create_Home():  
    with st.container(): 
        ut.Divisor('Supermercado', 'cart4','rgb(20,80,90)', 'Home01')
        st.write('\n \n')
        col1, col2, col3 = st.columns([1, 6, 1])

        with col1:
            st.write('          ')

        with col2:
            st.image('https://s3-sa-east-1.amazonaws.com/projetos-artes/fullsize%2F2011%2F11%2F26%2F20%2FWDL-Logo-9014_7543_041931082_419724885.jpg', width=300, use_column_width='auto') 
            st.write("""5 - Um supermercado está precisando de um sistema capaz de listar todos os produtos a partir de uma busca simples,
                     o usuário deve ser capaz de procurar um produto pelo nome, parcial ou completo. Segue uma lista de exemplo: \n 
produtos = [    
    "Camiseta", "Calça jeans", "Tênis", "Mochila", "Notebook", "Fones de ouvido","Smartphone", "Relógio", "Óculos de sol", "Garrafa de água", "Câmera", 
    "Console de jogos", "Livros", "Mesa", "Cadeira", "Luminária de mesa",  "Caderno", "Estojo", "Marcadores", "Pincéis de pintura", "Tela de pintura", 
    "Violão", "Teclado", "Microfone", "Drone", "Barraca de camping", "Saco de dormir", 
    "Botas de caminhada", "Bússola", "Lanterna", "Bicicleta", "Capacete", "Skate", 
    "Patins", "Bola de basquete", "Bola de futebol", "Taco de beisebol", 
    "Tacos de golfe", "Vara de pescar", "Raquete de tênis", "Roupa de banho", 
    "Protetor solar", "Toalha de praia", "Cesta de piquenique", "Churrasqueira", 
    "Cooler", "Jogos de tabuleiro", "Relógio de parede", "Ferro de passar roupa", 
    "Aspirador de pó", "Vaso de flores", "Chaleira", "Panela de pressão"
]  \n 
Ex: Se o usuário digitar apenas 'c' todos os produtos que possuem a letra c devem ser listados, começando pelos que inciam pela letra procurada seguidos daqueles produtos que apenas possuem a letra c \n

Caso o usuário digite uma palavra pela metade, por exemplo, "Cha" devem ser listados todos os produtos que se iniciem com esses caracteres primeiro e todos os que possuem essa sequência de caracteres em seguida.""")
        
        with col3:
            st.write('')
        
        st.write('\n \n')
        ut.Divisor('Copyright (c) 2024', '', 'rgb(20,80,90)', 'Home02')
