from os import popen
from random import *
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pickle

MEDIDA_VENTANA_PRINCIPAL = 300
#filas
Matriz_1Y = 215 #y de 1era fila
Matriz_2Y = 370 #y de 2da fila
Matriz_3Y = 525 #y de 3era fila

#columnas
Matriz_1X = 25
Matriz_2X = 180
Matriz_3X = 335
Matriz_4X = 490
Matriz_5X = 670
Matriz_6X = 825
Matriz_7X = 1000
Matriz_8X = 1150

class interfaz():
    def __init__(self):
        # Ventana principal
        self.ven_principal = Tk()
        self.ven_principal.geometry("300x300+200+200")
        self.ven_principal.title("Menú principal del teléfono")

        # Ventana de contactos
        self.ven_tablero = Toplevel(self.ven_principal)
        self.ven_tablero.geometry("1305x880+0+0")
        self.ven_tablero.title("Juego Real de Ur")
        self.ven_tablero.protocol("WM_DELETE_WINDOW", self.cerrar_todo)

        # Cargar imagenes
        self.ImgBackground = PhotoImage(file="Include/tablero.png")    
        self.ImgFichaBlanca = PhotoImage(file="Include/blanca.png")
        self.ImgFichaNegra = PhotoImage(file="Include/negra.png")
        self.ImgDado0A = PhotoImage(file="Include/dado0-a.png")
        self.ImgDado0B = PhotoImage(file="Include/dado0-b.png")
        self.ImgDado1A = PhotoImage(file="Include/dado1-a.png")
        self.ImgDado1B = PhotoImage(file="Include/dado1-b.png")
        self.ImgPilaNegra = PhotoImage(file="Include/pila-negra.png")
        self.ImgPilaBlanca = PhotoImage(file="Include/pila-blanca.png")

        # Fondos y Etiquetas
        Label(self.ven_principal, bg="white", height=MEDIDA_VENTANA_PRINCIPAL, width=MEDIDA_VENTANA_PRINCIPAL).place(x=0, y=0)
        Label(self.ven_principal, bg="white", text="Juego Real de Ur", underline=0, fg="orange red", bd=5, pady=20, padx=7, font=("Tahoma", 28)).grid(row=0, column=0)

        # Botones
        self.btnInicio = Button(self.ven_principal, text="Inicio Juego", font=("Tahoma", 12), command=self.iniciarJuego, pady=4, padx=2).grid(row=4, column=0)
        # Variante:
        # self.btnInicio = Button(..., command=lambda: iniciarJuego(dificultad)).place...

        Label(self.ven_tablero, bg="white", text=" ", width=1305, height=880).place(x=0, y=0)
        Label(self.ven_tablero, image=self.ImgBackground, bd=0).place(x=0, y=197)
        #prueba de posiciones
        #fichas 1er fila
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_1X, y=Matriz_1Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_2X, y=Matriz_1Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_3X, y=Matriz_1Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_4X, y=Matriz_1Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_7X, y=Matriz_1Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_8X, y=Matriz_1Y)
        #fichas 2da fila
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_1X, y=Matriz_2Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_2X, y=Matriz_2Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_3X, y=Matriz_2Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_4X, y=Matriz_2Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_5X, y=Matriz_2Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_6X, y=Matriz_2Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_7X, y=Matriz_2Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_8X, y=Matriz_2Y)
        #fichas 3er fila
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_4X, y=Matriz_3Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_3X, y=Matriz_3Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_2X, y=Matriz_3Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_1X, y=Matriz_3Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_7X, y=Matriz_3Y)
        Label(self.ven_tablero, image=self.ImgFichaBlanca, bd=0).place(x=Matriz_8X, y=Matriz_3Y)

        
        #INFO IA
        Label(self.ven_tablero, text="Oponente", bg="red", fg="white", font=("Tahoma", 15)).place(x=10, y=10)

        self.iaCasaVal = StringVar()
        Label(self.ven_tablero, text="Fichas restantes en casa:", bg="white", font=("Tahoma", 15)).place(x=40, y=50)
        Label(self.ven_tablero, textvariable=self.iaCasaVal, bg="white", font=("Tahoma", 15)).place(x=270, y=50)
        Label(self.ven_tablero, image=self.ImgPilaNegra).place(x=400, y=20)
        self.iaSalidaVal = StringVar()
        Label(self.ven_tablero, text="Fichas en salida: ", bg="white", font=("Tahoma", 15)).place(x=1080, y=50)
        Label(self.ven_tablero, textvariable=self.iaSalidaVal, bg="white", font=("Tahoma", 15)).place(x=1230, y=50)
        Label(self.ven_tablero, image=self.ImgPilaNegra).place(x=880, y=20)
        Label(self.ven_tablero, image=self.ImgDado0A, bd=0).place(x=660, y=210)
        Label(self.ven_tablero, image=self.ImgDado0B, bd=0).place(x=765, y=210)
        Label(self.ven_tablero, image=self.ImgDado0A, bd=0).place(x=870, y=210)

        #INFO JUGADOR
        Label(self.ven_tablero, text="Jugador", bg="deepSkyBlue", font=("Tahoma", 15)).place(x=10, y=700)

        self.jgdrCasaVal = StringVar()
        Label(self.ven_tablero, text="Fichas restantes en casa:", bg="white", font=("Tahoma", 15)).place(x=40, y=740)
        Label(self.ven_tablero, textvariable=self.jgdrCasaVal, bg="white", font=("Tahoma", 15)).place(x=270, y=740)
        Label(self.ven_tablero, image=self.ImgPilaBlanca).place(x=400, y=710)
        self.jgdrSalidaVal = StringVar()
        Label(self.ven_tablero, text="Fichas en salida: ", bg="white", font=("Tahoma", 15)).place(x=1080, y=740)
        Label(self.ven_tablero, textvariable=self.jgdrSalidaVal, bg="white", font=("Tahoma", 15)).place(x=1230, y=740)
        Label(self.ven_tablero, image=self.ImgPilaBlanca).place(x=880, y=710)
        Label(self.ven_tablero, image=self.ImgDado0A, bd=0).place(x=660, y=570)
        Label(self.ven_tablero, image=self.ImgDado0B, bd=0).place(x=765, y=570)
        Label(self.ven_tablero, image=self.ImgDado0A, bd=0).place(x=870, y=570)

        self.btnLanzarDado = Button(self.ven_tablero, text="Lanzar Dados", font=("Tahoma", 12),
                                pady=4, padx=2, state="disabled").place(x=660, y=680)

        self.ven_tablero.withdraw()  # Oculta ventana
        self.ven_principal.mainloop()

    # Interfáz gráfica


    # Mostrar y Ocultar ventanas

    def cerrar_todo(self):
        self.ven_principal.destroy()

    def iniciarJuego(self):
        """
    Salidas: Muestra la ventana del lirbo de contactos y esconde la principal"""
        self.ven_tablero.deiconify()  # Despliega la ventana
        self.ven_principal.withdraw()  # Oculta la ventana


    # ----------------------------------------------------------------------------------------------------------------------

    # Datos
    '''
    codigo = ""  # Almacena el código a adivinar creado aleatoriamente
    otros_codigos = []  # Evita que los codigos se repitan
    cont_codigos = 0  # Cuando llegue a 100 se reinician las apariciones aleatorias
    intento = ["", "", "", ""]  # Contiene la jugada actual a calificar
    numero_de_jugada = 2  # Leva la cuenta del numero de jugada
    opciones = '123456'  # Opciones para crear el código
    coincidencias = 0  # Contadores de las jugadas
    apariciones = 0
    segs = 0  # Variables para el reloj
    mins = 0
    hora = 0
    terminar = False  # Variable que termina el juego si se excede el tiempo ingresado
    temp = 0  # Almacena la cantidad de segundos transcurridos 
    segundos_config = 0  # Contendria los segundos sacados del archivos

    # Funciones
    def iniciar():
        """
    Salidas: Despliega en la pantalla todo lo necesario para el juego seleccionado de acuerdo con la configuracion ingresada e inicializa el juego"""
        global tiempo, nombre, jugada_max, vdificultad, tablero
        cargar_configuracion()
        if jugador.get() == "":  # No inicia el juego si no ha ingresado un nombre para jugar
            messagebox.showerror(title="Error", message="Primero ingrese un nombre para poder jugar")
        else:
            nombre = jugador.get()  # Guarda el nombre del jugador y no puede ser modificado en media partida
            # Botones del juego
            Button(ven_juego, text="Finalizar Juego", bg="green", font=("Tahoma", 14), command=boton_fin).place(x=220,
                                                                                                                y=600)  # Boton finalizar partida
            Button(ven_juego, text="Calificar", bg="sky blue", font=("Tahoma", 14), command=calificar).place(x=255,
                                                                                                             y=550)  # Boton para Calificar las jugadas
            if vdificultad == 1:  # Condicional para verificar el nivel de dificultad y la cantidad de jugadas posibles
                jugada_max = 9
            elif vdificultad == 2:
                jugada_max = 8
            elif vdificultad == 3:
                jugada_max = 7
            if tablero == 1:  # Posicion del tablero
                lugar = 7
            else:
                lugar = 0
            if elementos == 1:  # Tipo de elementos a utilizar (colores, letras, números o símbolos)
                Button(ven_juego, image=ImgColor1, command=lambda: colocar_color(ImgColor1)).grid(row=2, column=lugar)
                Button(ven_juego, image=ImgColor2, command=lambda: colocar_color(ImgColor2)).grid(row=3, column=lugar)
                Button(ven_juego, image=ImgColor3, command=lambda: colocar_color(ImgColor3)).grid(row=4, column=lugar)
                Button(ven_juego, image=ImgColor4, command=lambda: colocar_color(ImgColor4)).grid(row=5, column=lugar)
                Button(ven_juego, image=ImgColor5, command=lambda: colocar_color(ImgColor5)).grid(row=6, column=lugar)
                Button(ven_juego, image=ImgColor6, command=lambda: colocar_color(ImgColor6)).grid(row=7, column=lugar)
            elif elementos == 2:
                Button(ven_juego, text="A", font=("Tahoma", 22), width=2, command=lambda: colocar_color("A")).grid(
                    row=2, column=lugar)
                Button(ven_juego, text="B", font=("Tahoma", 22), width=2, command=lambda: colocar_color("B")).grid(
                    row=3, column=lugar)
                Button(ven_juego, text="C", font=("Tahoma", 22), width=2, command=lambda: colocar_color("C")).grid(
                    row=4, column=lugar)
                Button(ven_juego, text="D", font=("Tahoma", 22), width=2, command=lambda: colocar_color("D")).grid(
                    row=5, column=lugar)
                Button(ven_juego, text="E", font=("Tahoma", 22), width=2, command=lambda: colocar_color("E")).grid(
                    row=6, column=lugar)
                Button(ven_juego, text="F", font=("Tahoma", 22), width=2, command=lambda: colocar_color("F")).grid(
                    row=7, column=lugar)
            elif elementos == 3:
                Button(ven_juego, text="1", font=("Tahoma", 22), width=2, command=lambda: colocar_color("1")).grid(
                    row=2, column=lugar)
                Button(ven_juego, text="2", font=("Tahoma", 22), width=2, command=lambda: colocar_color("2")).grid(
                    row=3, column=lugar)
                Button(ven_juego, text="3", font=("Tahoma", 22), width=2, command=lambda: colocar_color("3")).grid(
                    row=4, column=lugar)
                Button(ven_juego, text="4", font=("Tahoma", 22), width=2, command=lambda: colocar_color("4")).grid(
                    row=5, column=lugar)
                Button(ven_juego, text="5", font=("Tahoma", 22), width=2, command=lambda: colocar_color("5")).grid(
                    row=6, column=lugar)
                Button(ven_juego, text="6", font=("Tahoma", 22), width=2, command=lambda: colocar_color("6")).grid(
                    row=7, column=lugar)
            elif elementos == 4:
                Button(ven_juego, text="@", font=("Tahoma", 22), width=2, command=lambda: colocar_color("@")).grid(
                    row=2, column=lugar)
                Button(ven_juego, text="+", font=("Tahoma", 22), width=2, command=lambda: colocar_color("+")).grid(
                    row=3, column=lugar)
                Button(ven_juego, text="&", font=("Tahoma", 22), width=2, command=lambda: colocar_color("&")).grid(
                    row=4, column=lugar)
                Button(ven_juego, text="$", font=("Tahoma", 22), width=2, command=lambda: colocar_color("$")).grid(
                    row=5, column=lugar)
                Button(ven_juego, text="!", font=("Tahoma", 22), width=2, command=lambda: colocar_color("!")).grid(
                    row=6, column=lugar)
                Button(ven_juego, text="?", font=("Tahoma", 22), width=2, command=lambda: colocar_color("?")).grid(
                    row=7, column=lugar)
            # Etiquetas invisibles de espacio para colocar los colores
            Label(ven_juego, width=6, height=2).grid(row=2, column=2)
            Label(ven_juego, width=6, height=2).grid(row=2, column=3)
            Label(ven_juego, width=6, height=2).grid(row=2, column=4)
            Label(ven_juego, width=6, height=2).grid(row=2, column=5)
            x = 1
            for i in range(2, jugada_max + 1):  # Coloca las etiquetas de los numeros de jugadas posibles
                Label(ven_juego, width=5, height=3, text=str(x), font=("Tahoma", 10)).grid(row=i, column=1)
                x += 1
            Label(ven_juego, width=7, height=2).grid(row=2, column=6)
            # Radiobuttons
            Radiobutton(ven_juego, value=1, variable=seleccion_lugar).grid(row=1,
                                                                           column=2)  # Botones para decidir donde poner la opción presionada
            Radiobutton(ven_juego, value=2, variable=seleccion_lugar).grid(row=1, column=3)
            Radiobutton(ven_juego, value=3, variable=seleccion_lugar).grid(row=1, column=4)
            Radiobutton(ven_juego, value=4, variable=seleccion_lugar).grid(row=1, column=5)
            Label(ven_juego, height=1).grid(row=10, column=0)  # Etiqueta invisible
            tiempo = Label(ven_juego)  # Etiqueta del reloj
            tiempo.grid(row=12, column=0)
            timer()

    # Funciones para globalizar los valores de los botones en configuración
    def dificultad():
        global vdificultad
        vdificultad = seleccion_dificultad.get()

    def config_tablero():
        global tablero
        tablero = seleccion_tablero.get()

    def elementos():
        global elementos
        elementos = seleccion_elementos.get()

    # Interfaz
    def mostrar_menu():
        Button(ven_mm, image=ImgRegresar, command=regresar_a_ventana).place(x=30, y=115)
        cargar_configuracion()
        ven_mm.deiconify()
        ven_principal.withdraw()

    def mostrar_juego():
        global jugador
        Button(ven_juego, image=ImgRegresar, command=boton_fin).grid(row=0, column=0)  # Boton para regresar
        Button(ven_juego, text="Iniciar Juego", bg="pink", font=("Tahoma", 14), command=iniciar).place(x=230,
                                                                                                       y=600)  # Boton para iniciar el juego
        Entry(ven_juego, textvariable=jugador, width=35).place(x=145,
                                                               y=690)  # Cuadro de texto para el nombre del jugador
        Label(ven_juego, text="Nombre del Jugador:", font=("Tahoma", 12)).place(x=145, y=665)
        Label(ven_juego, text="MASTER MIND", font=("Copperplate Gothic Bold", 20), fg="yellow", bg="green").place(x=65,
                                                                                                                  y=10)
        ven_juego.deiconify()
        ven_mm.withdraw()

    def mostrar_config():
        segundos.set(segundos_config)  # Coloca en el cuadro de texto el valor que contiene el reloj en el diccionario
        Button(ven_config, image=ImgRegresar, command=salir_config).place(x=0, y=0)  # Boton para regresar
        Label(ven_config, text="Dificultad", font=("Tahoma", 14)).place(x=10, y=70)
        Label(ven_config, image=ImgColor1).place(x=30, y=380)
        Label(ven_config, image=ImgColor2).place(x=30, y=430)
        Label(ven_config, image=ImgColor3).place(x=30, y=480)
        Label(ven_config, image=ImgColor4).place(x=30, y=530)
        Label(ven_config, image=ImgColor5).place(x=30, y=580)
        Label(ven_config, image=ImgColor6).place(x=30, y=630)
        Label(ven_config, text="A", font=("Tahoma", 23)).place(x=125, y=380)
        Label(ven_config, text="B", font=("Tahoma", 23)).place(x=125, y=430)
        Label(ven_config, text="C", font=("Tahoma", 23)).place(x=125, y=480)
        Label(ven_config, text="D", font=("Tahoma", 23)).place(x=125, y=530)
        Label(ven_config, text="E", font=("Tahoma", 23)).place(x=125, y=580)
        Label(ven_config, text="F", font=("Tahoma", 23)).place(x=125, y=630)
        Label(ven_config, text="1", font=("Tahoma", 23)).place(x=205, y=380)
        Label(ven_config, text="2", font=("Tahoma", 23)).place(x=205, y=430)
        Label(ven_config, text="3", font=("Tahoma", 23)).place(x=205, y=480)
        Label(ven_config, text="4", font=("Tahoma", 23)).place(x=205, y=530)
        Label(ven_config, text="5", font=("Tahoma", 23)).place(x=205, y=580)
        Label(ven_config, text="6", font=("Tahoma", 23)).place(x=205, y=630)
        Label(ven_config, text="@", font=("Tahoma", 23)).place(x=290, y=380)
        Label(ven_config, text="+", font=("Tahoma", 23)).place(x=290, y=430)
        Label(ven_config, text="&", font=("Tahoma", 23)).place(x=290, y=480)
        Label(ven_config, text="$", font=("Tahoma", 23)).place(x=290, y=530)
        Label(ven_config, text="!", font=("Tahoma", 23)).place(x=290, y=580)
        Label(ven_config, text="?", font=("Tahoma", 23)).place(x=290, y=630)
        ven_config.deiconify()
        ven_mm.withdraw()

    def salir_config():
        ven_mm.deiconify()
        ven_config.withdraw()

    def salir_juego():
        ven_mm.deiconify()
        ven_juego.withdraw()
    '''

