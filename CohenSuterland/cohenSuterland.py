import customtkinter as ctk

class CohenSutherland(ctk.CTkCanvas):
    def __init__(self, parent, width=500, height=500):
        super().__init__(parent, width=width, height=height)
        self.width = width
        self.height = height
        self.grid_size = 20  # Tamanho da grade
        self.create_background()
        self.create_axes()

    def create_background(self):
        """Cria o fundo do plano cartesiano (grade)"""
        for x in range(0, self.width, self.grid_size):
            self.create_line(x, 0, x, self.height, fill="lightgray", dash=(2, 2))  # Linhas verticais
        for y in range(0, self.height, self.grid_size):
            self.create_line(0, y, self.width, y, fill="lightgray", dash=(2, 2))  # Linhas horizontais

    def create_axes(self):
        """Cria os eixos X e Y"""
        # Eixo Y (vertical)
        self.create_line(self.width//2, 0, self.width//2, self.height, fill="blue", width=2)
        # Eixo X (horizontal)
        self.create_line(0, self.height//2, self.width, self.height//2, fill="green", width=2)

    def draw_square(self, p1, p2, p3, p4, color="red"):
        """Desenha um quadrado no plano cartesiano usando os pontos P1, P2, P3, P4"""
        # Desenha as linhas que conectam os pontos
        self.create_line(p1[0], p1[1], p2[0], p2[1], fill=color, width=2)
        self.create_line(p2[0], p2[1], p3[0], p3[1], fill=color, width=2)
        self.create_line(p3[0], p3[1], p4[0], p4[1], fill=color, width=2)
        self.create_line(p4[0], p4[1], p1[0], p1[1], fill=color, width=2)

    def draw_window(self, p1, p2):
        """Desenha uma janela no plano cartesiano com centro na origem e extremos dados pelos pontos p1 e p2"""
        # Cálculo do ponto superior esquerdo e inferior direito da janela
        x1, y1 = p1  # Extremidade inferior esquerda
        x2, y2 = p2  # Extremidade superior direita

        # Transformando para coordenadas relativas à origem
        center_x = self.width // 2
        center_y = self.height // 2

        # Ajustando a posição da janela com centro na origem
        top_left = (center_x + x1, center_y - y2)
        bottom_right = (center_x + x2, center_y - y1)

        # Desenhando o retângulo da janela
        self.create_rectangle(top_left[0], top_left[1], bottom_right[0], bottom_right[1], outline="purple", width=2)

        # Prolongando as linhas horizontais e verticais da janela
        self.extend_lines(top_left, bottom_right)

    def extend_lines(self, top_left, bottom_right):
        """Prolonga as linhas horizontais e verticais da janela até as bordas do plano cartesiano"""
        # Prolongando linha vertical esquerda
        self.create_line(top_left[0], 0, top_left[0], self.height, fill="purple", dash=(2, 2))

        # Prolongando linha vertical direita
        self.create_line(bottom_right[0], 0, bottom_right[0], self.height, fill="purple", dash=(2, 2))

        # Prolongando linha horizontal superior
        self.create_line(0, top_left[1], self.width, top_left[1], fill="purple", dash=(2, 2))

        # Prolongando linha horizontal inferior
        self.create_line(0, bottom_right[1], self.width, bottom_right[1], fill="purple", dash=(2, 2))



