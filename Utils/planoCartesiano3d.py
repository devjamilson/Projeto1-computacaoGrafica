import customtkinter as ctk

class CartesianPlane3D(ctk.CTkCanvas):
    def __init__(self, parent, width=500, height=500):
        super().__init__(parent, width=width, height=height)
        self.width = width
        self.height = height
        self.grid_size = 20  # Tamanho da grade
        self.inclination_offset = 50  # Deslocamento para inclinar o eixo Z
        self.scale_factor = 0.5  # Fator de escala para simular profundidade (Z)
        self.create_background()
        self.create_axes()

    def create_background(self):
        """Cria o fundo do plano cartesiano (grade)"""
        for x in range(0, self.width, self.grid_size):
            self.create_line(x, 0, x, self.height, fill="lightgray", dash=(2, 2))  # Linhas verticais
        for y in range(0, self.height, self.grid_size):
            self.create_line(0, y, self.width, y, fill="lightgray", dash=(2, 2))  # Linhas horizontais

    def create_axes(self):
        """Cria os eixos X, Y e Z"""
        # Eixo Y (vertical, positivo do topo ao centro)
        self.create_line(self.width // 2, 0, self.width // 2, self.height, fill="blue", width=2)
        # Eixo X (horizontal, positivo do centro para a direita)
        self.create_line(0, self.height // 2, self.width, self.height // 2, fill="green", width=2)
        # Eixo Z positivo (do centro para o canto inferior direito)
        self.create_line(
            self.width // 2, self.height // 2,  # Centro
            self.width, self.height,  # Canto inferior direito
            fill="red", width=2
        )
        # Eixo Z negativo (do centro para o canto superior esquerdo)
        self.create_line(
            self.width // 2, self.height // 2,  # Centro
            0, 0,  # Canto superior esquerdo
            fill="red", width=2  # Linha tracejada para diferenciar parte negativa
        )

    def project_point(self, x, y, z):
        """Aplica uma projeção simples para simular 3D no plano 2D"""
        # Ajusta projeção considerando os eixos positivos definidos:
        # Y positivo para cima (invertendo no canvas)
        # X positivo para a direita
        # Z positivo para o canto inferior direito
        projected_x = self.width // 2 + x + z * self.scale_factor
        projected_y = self.height // 2 - y + z * self.scale_factor
        return projected_x, projected_y

    def draw_line(self, x1, y1, z1, x2, y2, z2, color="blue"):
        """Desenha uma linha entre dois pontos no espaço 3D"""
        px1, py1 = self.project_point(x1, y1, z1)
        px2, py2 = self.project_point(x2, y2, z2)
        self.create_line(px1, py1, px2, py2, fill=color, width=2)

    def draw_cube(self, x, y, z, lado, color="yellow"):
        """Desenha um cubo em 3D no plano cartesiano"""
        # Calcula os vértices do cubo
        P1 = (x, y, z)  # Vértice inicial
        P2 = (x + lado, y, z)  # Direção X
        P3 = (x + lado, y + lado, z)  # Direção X, Y
        P4 = (x, y + lado, z)  # Direção Y
        P5 = (x, y, z + lado)  # Direção Z
        P6 = (x + lado, y, z + lado)  # Direção X, Z
        P7 = (x + lado, y + lado, z + lado)  # Direção X, Y, Z
        P8 = (x, y + lado, z + lado)  # Direção Y, Z

        # Desenha as arestas do cubo
        # Frente
        self.draw_line(*P1, *P2, color)  # P1 -> P2
        self.draw_line(*P2, *P3, color)  # P2 -> P3
        self.draw_line(*P3, *P4, color)  # P3 -> P4
        self.draw_line(*P4, *P1, color)  # P4 -> P1

        # Fundo
        self.draw_line(*P5, *P6, color)  # P5 -> P6
        self.draw_line(*P6, *P7, color)  # P6 -> P7
        self.draw_line(*P7, *P8, color)  # P7 -> P8
        self.draw_line(*P8, *P5, color)  # P8 -> P5

        # Ligações frente-fundo
        self.draw_line(*P1, *P5, color)  # P1 -> P5
        self.draw_line(*P2, *P6, color)  # P2 -> P6
        self.draw_line(*P3, *P7, color)  # P3 -> P7
        self.draw_line(*P4, *P8, color)  # P4 -> P8
