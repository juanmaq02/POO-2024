from tkinter import *
from tkinter import Tk, messagebox, ttk
from random import randint
from GestorJugador import GestorJugador
from ClaseObjectEncoder import ObjectEncoder
from ClaseJugador import Jugador
from datetime import datetime
import pygame

class App:
    def __init__(self, lista, jsonF):
        self.__lista = lista
        self.__jsonF = jsonF
        self.__ventana = Tk()
        self.__ventana.geometry('317x490+750+250')
        self.__ventana.title('PySimon - Game')
        self.__ventana.config(bg='#D9D9D9')
        self.__ventana.resizable(0,0)
        self.__nombre = StringVar()
        self.__puntos = IntVar(value=0)
        pygame.mixer.init()
        self.sonido1 = pygame.mixer.Sound('sonidos/simonSound1.wav')
        self.sonido2 = pygame.mixer.Sound('sonidos/simonSound2.wav')
        self.sonido3 = pygame.mixer.Sound('sonidos/simonSound3.wav')
        self.sonido4 = pygame.mixer.Sound('sonidos/simonSound4.wav')
        self.dificultad = StringVar()

        #Menu de puntuaciones
        barraMenu = Menu(self.__ventana)
        menuPuntajes = Menu(barraMenu, tearoff=0)
        menuPuntajes.add_command(label="Ver puntajes", command=self.puntajes)
        menuPuntajes.add_separator()
        menuPuntajes.add_command(label="Salir", command=self.__ventana.destroy, accelerator='Alt+F4')
        barraMenu.add_cascade(label='Puntajes', menu=menuPuntajes)
        self.__ventana.config(menu=barraMenu)

        #Labels, lista y timer
        self.labelJugador = Label(self.__ventana, textvariable=self.__nombre)
        self.labelJugador.grid(row=0, column=0)
        self.labelPuntos = Label(self.__ventana, textvariable=self.__puntos)
        self.labelPuntos.grid(row=0, column=1)
        self.labelDificultad = Label(self.__ventana, text='Dificultad:')
        self.labelDificultad.grid(row=1, column=0)
        self.dificultades = ['Principiante', 'Experto', 'Super experto']
        self.lista = ttk.Combobox(self.__ventana, values=self.dificultades, textvariable=self.dificultad)
        self.lista.grid(row=1, column=1)
        self.labelTimer1 = Label(self.__ventana, text="Timer:")
        self.labelTimer1.grid(row=2, column=0)
        self.labelTimer2 = Label(self.__ventana, text="0")
        self.labelTimer2.grid(row=2, column=1)
        self.labelDificultad.config(bg='#D9D9D9')
        self.labelJugador.config(bg='#D9D9D9')
        self.labelPuntos.config(bg='#D9D9D9')
        self.labelTimer1.config(bg='#D9D9D9')
        self.labelTimer2.config(bg='#D9D9D9')

        #Botones
        self.boton1 = Canvas(self.__ventana, width=145, height=200, bg='lime')
        self.boton1.grid(row=3, column=0, padx=5, pady=5)
        self.bind1 = self.boton1.bind("<Button-1>", lambda event: [self.animacion(1), self.sonido(1), self.comenzarJuego()])
        self.boton2 = Canvas(self.__ventana, width=145, height=200, bg='#9B0000')
        self.boton2.grid(row=3, column=1, padx=5, pady=5)
        self.bind2 = self.boton2.bind("<Button-1>", lambda event: [self.animacion(2), self.sonido(2), print("Presione el botón verde para comenzar.")])
        self.boton3 = Canvas(self.__ventana, width=145, height=200, bg='#9B9B00')
        self.boton3.grid(row=4, column=0, padx=5, pady=5)
        self.bind3 = self.boton3.bind("<Button-1>", lambda event: [self.animacion(3), self.sonido(3), print("Presione el botón verde para comenzar.")])
        self.boton4 = Canvas(self.__ventana, width=145, height=200, bg='#00009B')
        self.boton4.grid(row=4, column=1, padx=5, pady=5)
        self.bind4 = self.boton4.bind("<Button-1>", lambda event: [self.animacion(4), self.sonido(4), print("Presione el botón verde para comenzar.")])

        self.nombre()
        
        if self.__nombre.get() == '':
            self.__nombre.set('Jugador anónimo')

        self.__ventana.mainloop()

    def nombre(self):
        self.__ventanaNombre = Toplevel()
        self.__ventanaNombre.geometry('220x80+800+375')
        self.__ventanaNombre.title('Ingresar nombre')
        self.__ventanaNombre.resizable(0,0)
        label1 = LabelFrame(self.__ventanaNombre, padx=40, pady=15, text="Datos del Jugador")
        label2 = Label(label1, text='Jugador', padx=5)
        self.entry = Entry(label1, width=15, textvariable=self.__nombre)
        boton = Button(label1, text="Iniciar Juego", command=self.__ventanaNombre.destroy)
        label1.grid(column=0, row=0)
        label2.grid(column=0, row=1)
        self.entry.grid(column=1, row=1)
        boton.grid(column=1, row=2)
        self.__ventanaNombre.transient(master=self.__ventana)
        self.__ventanaNombre.grab_set()
        self.__ventana.wait_window(self.__ventanaNombre)

    def puntajes(self):
        self.__ventanaPuntajes = Toplevel()
        self.__ventanaPuntajes.geometry('700x300+760+260')
        self.__ventanaPuntajes.title('Puntajes - PySimon')
        labelPuntajes = LabelFrame(self.__ventanaPuntajes, padx=40, pady=10, text='Galería de puntajes')
        labelPuntajes.pack()
        treePuntajes = ttk.Treeview(labelPuntajes, columns=('Jugador', 'Fecha', 'Hora', 'Dificultad', 'Puntaje'), height=10, show='headings')
        treePuntajes.heading("Jugador", text="Jugador")
        treePuntajes.heading("Fecha", text="Fecha")
        treePuntajes.heading("Hora", text="Hora")
        treePuntajes.heading("Dificultad", text="Dificultad")
        treePuntajes.heading("Puntaje", text="Puntaje")
        for puntaje in self.__lista.getLista():
            treePuntajes.insert("", END, values=(puntaje.getNombre(), puntaje.getFecha(), puntaje.getHora(), puntaje.getDificultad(), puntaje.getPuntaje()))
            treePuntajes.pack(expand=True, fill=BOTH)
        boton = Button(labelPuntajes, text='Cerrar', padx=10, pady=5, command=self.__ventanaPuntajes.destroy)
        boton.pack()

    def comenzarJuego(self):
        if self.dificultad.get() == '':
            messagebox.showwarning(title="Ingrese dificultad", message="Ingrese una dificultad")
            self.boton1.config(bg='lime')
        else:
            self.colores = []
            if self.dificultad.get() == 'Principiante':
                self.timer = 6
                self.timerFlash = 600
            else:
                self.timer = 2
                self.timerFlash = 100
            self.__ventana.after(1500)
            self.juego()

    def juego(self):
        if self.dificultad.get() == 'Super experto':
            for i in range(2):
                self.colores.append(randint(1,4))
        else:
            self.colores.append(randint(1,4))
        self.unbindear()
        self.__ventana.config(bg='#AA0000')
        self.labelDificultad.config(bg='#AA0000')
        self.labelJugador.config(bg='#AA0000')
        self.labelPuntos.config(bg='#AA0000')
        self.labelTimer1.config(bg='#AA0000')
        self.labelTimer2.config(bg='#AA0000')
        for color in self.colores:
            self.flashColor(color)
        self.bindear()
        self.__ventana.config(bg='#00AA00')
        self.labelDificultad.config(bg='#00AA00')
        self.labelJugador.config(bg='#00AA00')
        self.labelPuntos.config(bg='#00AA00')
        self.labelTimer1.config(bg='#00AA00')
        self.labelTimer2.config(bg='#00AA00')
        for color in self.colores:
            self.startTimer()
            self.secuencia(color)
            self.bindear()
            self.stopTimer()
        self.__puntos.set(self.__puntos.get()+1)
        self.__ventana.after(1500)
        self.juego()

    def bindear(self):
        self.bind1 = self.boton1.bind("<Button-1>", lambda event: [self.animacion(1), self.sonido(1), self.setGameOver()])
        self.bind2 = self.boton2.bind("<Button-1>", lambda event: [self.animacion(2), self.sonido(2), self.setGameOver()])
        self.bind3 = self.boton3.bind("<Button-1>", lambda event: [self.animacion(3), self.sonido(3), self.setGameOver()])
        self.bind4 = self.boton4.bind("<Button-1>", lambda event: [self.animacion(4), self.sonido(4), self.setGameOver()])

    def unbindear(self):
        self.bind1 = self.boton1.bind("<Button-1>", lambda event: [self.animacion(1), print('Espere a que finalice la secuencia.')])
        self.bind2 = self.boton2.bind("<Button-1>", lambda event: [self.animacion(2), print('Espere a que finalice la secuencia.')])
        self.bind3 = self.boton3.bind("<Button-1>", lambda event: [self.animacion(3), print('Espere a que finalice la secuencia.')])
        self.bind4 = self.boton4.bind("<Button-1>", lambda event: [self.animacion(4), print('Espere a que finalice la secuencia.')])

    def flashColor(self, color):
        if 1 == color:
            self.boton1.configure(bg='lime')
            self.sonido(1)
            self.__ventana.update()
        if 2 == color:
            self.boton2.configure(bg='red')
            self.sonido(2)
            self.__ventana.update()
        if 3 == color:
            self.boton3.configure(bg='yellow')
            self.sonido(3)
            self.__ventana.update()
        if 4 == color:
            self.boton4.configure(bg='blue')
            self.sonido(4)
            self.__ventana.update()
            
        self.__ventana.after(500)
        self.__ventana.update()
        self.boton1.configure(bg='#009B00')
        self.boton2.configure(bg='#9B0000')
        self.boton3.configure(bg='#9B9B00')
        self.boton4.configure(bg='#00009B')
        self.__ventana.update()
        self.__ventana.after(self.timerFlash)

    def secuencia(self, color):
        if color == 1:
            self.bind1 = self.boton1.bind("<Button-1>", lambda event: [self.animacion(1), self.sonido(1), self.continuar()])
        elif color == 2:
            self.bind2 = self.boton2.bind("<Button-1>", lambda event: [self.animacion(2), self.sonido(2), self.continuar()])
        elif color == 3:
            self.bind3 = self.boton3.bind("<Button-1>", lambda event: [self.animacion(3), self.sonido(3), self.continuar()])
        else:
            self.bind4 = self.boton4.bind("<Button-1>", lambda event: [self.animacion(4), self.sonido(4), self.continuar()])
        self.__ventana.mainloop()

    def continuar(self):
        self.__ventana.quit()
        if self.dificultad.get() == 'Principiante':
            self.timer = 6
            self.timerFlash = 600
        else:
            self.timer = 2
            self.timerFlash = 50

    def setGameOver(self):
        self.stopTimer()
        messagebox.showerror(title='Game Over', message='Game Over. Puntaje obtenido {}.'.format(self.__puntos.get()))
        self.__lista.guardarJugador(Jugador(self.__nombre.get(), datetime.today().strftime("%d/%m/%Y"), datetime.now().strftime("%H:%M"), self.dificultad.get(), self.__puntos.get()))
        d = self.__lista.toJSON()
        self.__jsonF.guardarJSONArchivo(d, 'pysimonpuntajes.json')
        self.__ventana.config(bg='#D9D9D9')
        self.labelDificultad.config(bg='#D9D9D9')
        self.labelJugador.config(bg='#D9D9D9')
        self.labelPuntos.config(bg='#D9D9D9')
        self.labelTimer1.config(bg='#D9D9D9')
        self.labelTimer2.config(bg='#D9D9D9')
        self.boton1.config(bg='lime')
        self.bind1 = self.boton1.bind("<Button-1>", lambda event: [self.animacion(1), self.sonido(1), self.comenzarJuego()])
        self.bind2 = self.boton2.bind("<Button-1>", lambda event: [self.animacion(2), self.sonido(2), print("Presione el botón verde para comenzar.")])
        self.bind3 = self.boton3.bind("<Button-1>", lambda event: [self.animacion(3), self.sonido(3), print("Presione el botón verde para comenzar.")])
        self.bind4 = self.boton4.bind("<Button-1>", lambda event: [self.animacion(4), self.sonido(4), print("Presione el botón verde para comenzar.")])
        self.__puntos.set(0)
        self.nombre()

    def animacion(self, color):
        if color == 1:
            self.boton1.configure(bg='lime')
        elif color == 2:
            self.boton2.configure(bg='red')
        elif color == 3:
            self.boton3.configure(bg='yellow')
        else:
            self.boton4.configure(bg='blue')
            
        self.__ventana.update()
        self.__ventana.after(100)
        if color == 1:
            self.boton1.configure(bg='#009B00')
        elif color == 2:
            self.boton2.configure(bg='#9B0000')
        elif color == 3:
            self.boton3.configure(bg='#9B9B00')
        else:
            self.boton4.configure(bg='#00009B')
        self.__ventana.update()
        self.__ventana.after(150)

    def actualizarLabel(self):
        formato = f'{self.timer}'
        self.labelTimer2.config(text=formato)

    def startTimer(self):
        if self.timer > 0:
            self.timer -= 1
            self.actualizarLabel()
            self.after = self.__ventana.after(1000, self.startTimer)
        else:
            self.setGameOver()

    def stopTimer(self):
        self.__ventana.after_cancel(self.after)
        self.labelTimer2.config(text='0')

    def sonido(self, color):
        if color == 1:
            self.sonido1.play()
        elif color == 2:
            self.sonido2.play()
        elif color == 3:
            self.sonido3.play()
        else:
            self.sonido4.play()

if __name__ == '__main__':
    lista = GestorJugador()
    jsonF = ObjectEncoder()
    diccionario = jsonF.leerJSONArchivo('pysimonpuntajes.json')
    jugadores = jsonF.decodificarDiccionario(diccionario)
    for jugador in jugadores:
        lista.guardarJugador(jugador)
    app = App(lista, jsonF)