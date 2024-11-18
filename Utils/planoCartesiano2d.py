import customtkinter as ctk

class CartesianPlane(ctk.CTkCanvas):
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
