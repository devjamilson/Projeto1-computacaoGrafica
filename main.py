import customtkinter as ctk
from PIL import Image
from PIL import ImageTk
import numpy as np
import os


from Utils.planoCartesiano2d import CartesianPlane
from Utils.planoCartesiano3d import CartesianPlane3D

from CohenSuterland.cohenSuterland import CohenSutherland

#====================================================================================================================
# Cria a janela
#====================================================================================================================
janela = ctk.CTk()
# Configurando a estrutura da janela
janela.title('Projeto de Processamento de Imagens')
janela.geometry('1370x700+0+0')  # Coloca a janela no canto superior esquerdo
janela.maxsize(width=1370, height=700)
janela.minsize(width=1370, height=700)
#====================================================================================================================
# Abas
#====================================================================================================================
tabview = ctk.CTkTabview(janela, width=1370, height=700, fg_color="#f2f2f2")
tabview.pack(pady=20, padx=20, fill="both", expand=True)
# Adicionando as abas
tabview.add("Primitivas")
tabview.add("ECG")
tabview.add("Cohen-Sutherland")
tabview.add("2D")
tabview.add("3D")
tabview.add("Operadores com Imagem")




#====================================================================================================================
# Primitivas
#====================================================================================================================

#HEADER
container_primitivas = ctk.CTkFrame(tabview.tab("Primitivas"))
container_primitivas.pack(padx=10, pady=10, fill="x")

primitiva_selecionada = None

def plotar_primitiva():
    global primitiva_selecionada

    # Verifica a primitiva selecionada e a plota
    if primitiva_selecionada == "Reta - DDA":
        cartesian_plane.plot_line(-50, -50, 100, 100, color="blue")
    elif primitiva_selecionada == "Reta - Ponto Médio":
        cartesian_plane.plot_line(-100, 0, 100, 0, color="red")
    elif primitiva_selecionada == "Círculo - Ponto Médio":
        cartesian_plane.plot_circle(0, 0, 50, color="red")
    elif primitiva_selecionada == "Círculo - Equação Explicita":
        cartesian_plane.plot_circle(0, 0, 70, color="red")
    elif primitiva_selecionada == "Círculo - Trigonometrico":
        cartesian_plane.plot_circle(0, 0, 90, color="red")
    elif primitiva_selecionada == "Elipse":
        cartesian_plane.plot_ellipse(0, 0, 80, 40, color="red")
    else:
        print("Selecione uma primitiva para plotar no plano.")
        
def primitiva_selecionada(choice):
    global primitiva_selecionada
    print("Primitiva selecionada:", choice)
    primitiva_selecionada = choice

# Criando o plano cartesiano (será exibido dentro da aba "Primitivas")
cartesian_plane = CartesianPlane(tabview.tab("Primitivas"), width=500, height=500)
cartesian_plane.pack(padx=10, pady=10)

# ComboBox para selecionar a primitiva
primitivas = ctk.CTkComboBox(
    container_primitivas,
    values=["Reta - DDA", "Reta - Ponto Médio", "Círculo - Ponto Médio", "Círculo - Equação Explicita", "Círculo - Trigonometrico", "Elipse"],
    command=primitiva_selecionada,
    width=270,
    font=("Helvetica", 14),
)
primitivas.pack(side="left", padx=10, pady=10)

# Botão para plotar a primitiva
btn_primitiva = ctk.CTkButton(
    container_primitivas,
    text="Plotar Figura",
    command=plotar_primitiva
)
btn_primitiva.pack(side="left", padx=10, pady=10)

#====================================================================================================================
# ECG
#====================================================================================================================

#HEADER
container_ecg = ctk.CTkFrame(tabview.tab("ECG"))
container_ecg.pack(padx=10, pady=10, fill="x")


input_time = ctk.CTkEntry(container_ecg, placeholder_text="Digite o tempo")
input_time.pack(side="left", padx=10, pady=10)

def print_input_value():
    input_value = input_time.get()  # Pega o valor do campo de input
    print(f"Tempo inserido: {input_value}") 

# Botão que pega o valor do input e imprime
button = ctk.CTkButton(container_ecg, text="Gerar ECG", command=print_input_value)
button.pack(side="left", padx=10, pady=10)




#====================================================================================================================
# Cohen-Suterland
#====================================================================================================================
# Função que captura os valores dos inputs, gera os retângulos e desenha a janela

# Configuração da interface com CTk
container_cohen = ctk.CTkFrame(tabview.tab("Cohen-Sutherland"))
container_cohen.pack(padx=10, pady=10, fill="x")


# Campos de entrada para os limites da janela
input_x_min = ctk.CTkEntry(container_cohen, placeholder_text="X min", width=50)
input_x_min.pack(side="left", padx=10, pady=10)

input_y_min = ctk.CTkEntry(container_cohen, placeholder_text="Y min", width=50)
input_y_min.pack(side="left", padx=10, pady=10)

input_x_max = ctk.CTkEntry(container_cohen, placeholder_text="X max", width=50)
input_x_max.pack(side="left", padx=10, pady=10)

input_y_max = ctk.CTkEntry(container_cohen, placeholder_text="Y max", width=50)
input_y_max.pack(side="left", padx=10, pady=10)

def draw_window():
    # Obtendo os valores dos inputs de pontos
    p1_x_min = input_x_min.get()
    p1_y_min = input_y_min.get()

    p2_x_max = input_x_max.get()
    p2_y_max = input_y_max.get()

    # Convertendo as coordenadas de texto para números
    try:
        p1 = (int(p1_x_min), int(p1_y_min))
        p2 = (int(p2_x_max), int(p2_y_max))

        # Desenhando o quadrado no plano cartesiano
        cartesian_plane_cohen.draw_window(p1, p2)

    except ValueError:
       
        print("Por favor, insira as coordenadas no formato (x,y).")

cartesian_plane_cohen = CohenSutherland(tabview.tab("Cohen-Sutherland"), width=500, height=500)
cartesian_plane_cohen.pack(side="left", padx=100, pady=10)




# Botão para gerar a janela com base nos valores de entrada
button = ctk.CTkButton(container_cohen, text="Gerar Janela", command=draw_window)
button.pack(side="left", padx=10, pady=10)


#====================================================================================================================
# Operações com 2D
#====================================================================================================================

#HEADER
container_2d = ctk.CTkFrame(tabview.tab("2D"))
container_2d.pack(padx=10, pady=10, fill="x")

# FIGURA
input_p1 = ctk.CTkEntry(container_2d, placeholder_text="P1 = (x,y)", width=70)
input_p1.pack(side="left", padx=10, pady=10)
input_p2 = ctk.CTkEntry(container_2d, placeholder_text="P2 = (x,y)", width=70)
input_p2.pack(side="left", padx=10, pady=10)

input_p3 = ctk.CTkEntry(container_2d, placeholder_text="P3 = (x,y)", width=70)
input_p3.pack(side="left", padx=10, pady=10)
input_p4 = ctk.CTkEntry(container_2d, placeholder_text="P4 = (x,y)", width=70)
input_p4.pack(side="left", padx=10, pady=10)

# Função para desenhar o quadrado a partir dos pontos
def draw_square():
    # Obtendo os valores dos inputs de pontos
    p1_values = input_p1.get().strip('()').split(',')
    p2_values = input_p2.get().strip('()').split(',')
    p3_values = input_p3.get().strip('()').split(',')
    p4_values = input_p4.get().strip('()').split(',')

    # Convertendo as coordenadas de texto para números
    try:
        p1 = (float(p1_values[0]), float(p1_values[1]))
        p2 = (float(p2_values[0]), float(p2_values[1]))
        p3 = (float(p3_values[0]), float(p3_values[1]))
        p4 = (float(p4_values[0]), float(p4_values[1]))


        print("valor de p2" + p2)
        # Desenhando o quadrado no plano cartesiano
        cartesian_plane_2D_1.draw_square(p1, p2, p3, p4, color="red")
    except ValueError:

        print(p2_values)
       
        print("Por favor, insira as coordenadas no formato (x,y).")

# Botão para gerar o quadrado
button_draw = ctk.CTkButton(container_2d, text="Gerar Quadrado", command=draw_square)
button_draw.pack(side="left", padx=10, pady=10)

# PLANO CARTESIANO
cartesian_plane_2D_1 = CartesianPlane(tabview.tab("2D"), width=500, height=500)
cartesian_plane_2D_1.pack(side="left", padx=100, pady=10)

cartesian_plane_2D_2 = CartesianPlane(tabview.tab("2D"), width=500, height=500)
cartesian_plane_2D_2.pack(side="left", padx=10, pady=10)

#====================================================================================================================
# Operações com 3D
#====================================================================================================================

# HEADER
container_3d = ctk.CTkFrame(tabview.tab("3D"))
container_3d.pack(padx=10, pady=10, fill="x")

# PLANOS CARTESIANOS
cartesian_plane_3D_1 = CartesianPlane3D(tabview.tab("3D"), width=500, height=500)
cartesian_plane_3D_1.pack(side="left", padx=100, pady=10)

cartesian_plane_3D_2 = CartesianPlane3D(tabview.tab("3D"), width=500, height=500)
cartesian_plane_3D_2.pack(side="left", padx=10, pady=10)

# Inputs para o ponto inicial (P1) e o lado do cubo
input_p1 = ctk.CTkEntry(container_3d, placeholder_text="P1 = (x,y,z)", width=100)
input_p1.pack(side="left", padx=10, pady=10)

input_lado = ctk.CTkEntry(container_3d, placeholder_text="Lado do Cubo", width=100)
input_lado.pack(side="left", padx=10, pady=10)

# Função para gerar o cubo no plano 3D
def draw_cube():
    # Obtendo os valores do ponto inicial e do lado
    try:
        # Processa o ponto P1 (convertendo string para coordenadas numéricas)
        p1_values = input_p1.get().strip('()').split(',')
        p1 = tuple(map(float, p1_values))

        # Processa o tamanho do lado do cubo
        lado = float(input_lado.get())

        # Desenha o cubo no plano 3D
        cartesian_plane_3D_1.draw_cube(p1[0], p1[1], p1[2], lado, color="black")
        print(f"Cubo desenhado no ponto {p1} com lado {lado}")
    except ValueError:
        print("Erro: Verifique os valores inseridos. P1 deve ser (x,y,z) e lado deve ser um número.")

# Botão para gerar o cubo
button_draw_cube = ctk.CTkButton(container_3d, text="Gerar Cubo", command=draw_cube)
button_draw_cube.pack(side="left", padx=10, pady=10)

#====================================================================================================================
# Operações com Imagem
#====================================================================================================================

#HEADER
container_imagem= ctk.CTkFrame(tabview.tab("Operadores com Imagem"))
container_imagem.pack(padx=10, pady=10, fill="x")




#====================================================================================================================
# Inicia o loop da interface
#====================================================================================================================
janela.mainloop()
