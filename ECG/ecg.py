import tkinter as tk
import random
import time

# Configurações iniciais do ECG
width = 1000
height = 500
heartbeat_max = 100
heartbeat_min = 30

# Frequência e tempo de exibição
display_duration = 10000  # duração em milissegundos
is_running = False
start_time = None

# Inicializa a posição do ECG
initial_position = (0, height / 2)

# Classe para representar um ponto do ECG
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Classe para o ECG
class Electrocardiogram:
    def __init__(self, canvas):
        self.canvas = canvas
        self.points = []
        self.current_point_index = 0
        self.create_points()

    def create_points(self):
        # Gerar pontos aleatórios para o ECG
        self.points = [Point(initial_position[0], initial_position[1])]
        x = initial_position[0]
        for i in range(1, int(width / 10)):
            prev_point = self.points[i - 1]
            if i % 20 == 0:
                random_bottom = random.randint(prev_point.y - heartbeat_max, prev_point.y - heartbeat_min)
                random_top = random.randint(prev_point.y + heartbeat_min, prev_point.y + heartbeat_max)
                bottom_point = Point(prev_point.x + 10, random_bottom)
                self.points.append(bottom_point)
                top_point = Point(bottom_point.x + 10, random_top)
                self.points.append(top_point)
            else:
                self.points.append(Point(prev_point.x + 10, initial_position[1]))

    def reset(self):
        self.points = []
        self.create_points()
        self.current_point_index = 0

    def show_points(self):
        # Desenha os pontos do ECG no canvas
        if self.current_point_index < len(self.points):
            for i in range(self.current_point_index, len(self.points)):
                p1 = self.points[i - 1]
                p2 = self.points[i]
                self.canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill="green", width=1)
            self.current_point_index += 1
        else:
            self.reset()  # Reset o ECG quando atingir o final

# Função para iniciar o ECG
def start_ecg():
    global display_duration, is_running, start_time
    input_duration = entry_duration.get()
    display_duration = int(input_duration) * 1000  # Converte para milissegundos
    start_time = time.time()
    is_running = True
    run_ecg()

# Função para rodar o ECG no loop
def run_ecg():
    global is_running  # Declare is_running como global aqui
    if is_running:
        canvas.delete("all")  # Limpa a tela
        electrocardiogram.show_points()
        if (time.time() - start_time) * 1000 >= display_duration:
            is_running = False
            electrocardiogram.reset()
    root.after(50, run_ecg)  # Chama novamente após 50ms (ajustado para uma animação mais visível)

# Criar a janela Tkinter
root = tk.Tk()
root.title("ECG com Tkinter")
root.geometry(f"{width}x{height}")

# Criar o Canvas para desenhar o ECG
canvas = tk.Canvas(root, width=width, height=height, bg="black")
canvas.pack()

# Entradas e Botão
label_duration = tk.Label(root, text="Duração (segundos):", fg="white", bg="black")
label_duration.pack(pady=10)
entry_duration = tk.Entry(root)
entry_duration.pack(pady=10)
entry_duration.insert(0, "10")  # Valor inicial da duração

button_start = tk.Button(root, text="Iniciar ECG", command=start_ecg)
button_start.pack(pady=20)

# Instancia a classe do ECG
electrocardiogram = Electrocardiogram(canvas)

root.mainloop()
