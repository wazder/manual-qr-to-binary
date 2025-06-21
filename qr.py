import tkinter as tk

N = 21      # QR boyutu
CELL = 20   # hücre pikseli

class QREditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Manual QR Editor")
        self.canvas = tk.Canvas(self, width=N*CELL, height=N*CELL, bg='white')
        self.canvas.pack()
        # matris başlangıçta 0 (beyaz)
        self.M = [[0]*N for _ in range(N)]
        # tüm hücreleri çiz
        for i in range(N):
            for j in range(N):
                x0, y0 = j*CELL, i*CELL
                x1, y1 = x0+CELL, y0+CELL
                self.canvas.create_rectangle(x0, y0, x1, y1,
                                             fill='white', outline='gray',
                                             tags=f"cell_{i}_{j}")
        # tıklama olayını yakala
        self.canvas.bind("<Button-1>", self.on_click)
        # bir buton ekleyelim, basınca matrisini yazdıracak
        btn = tk.Button(self, text="Matrix'i yazdır", command=self.print_matrix)
        btn.pack(pady=5)

    def on_click(self, event):
        j = event.x // CELL
        i = event.y // CELL
        if 0 <= i < N and 0 <= j < N:
            # toggle
            self.M[i][j] ^= 1
            color = 'black' if self.M[i][j] else 'white'
            self.canvas.itemconfig(f"cell_{i}_{j}", fill=color)

    def print_matrix(self):
        for row in self.M:
            print(''.join(str(bit) for bit in row))

if __name__ == "__main__":
    app = QREditor()
    app.mainloop()
