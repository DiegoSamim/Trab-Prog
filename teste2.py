from tkinter import *


def hide_button(widget):
    widget.pack_forget()


def show_button(widget):
    widget.pack()


class Aba:

    def __init__(self, nome="", quantidade="", preço=""):
        self.nome = nome
        self.quantidade = quantidade
        self.preço = preço


class Organizador:

    def __init__(self, master=None):
        self.container = Frame(master)
        self.container["pady"] = 10
        self.container.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.sla = ["Residencial", "Comercial", "Personalizado"]

        self.nome = Label(self.container, text="Clique abaixo para criar uma nova configuração")
        self.nome.pack()

        self.botao = Button(self.container2, text="Novo", width=10,
                            command=lambda: [hide_button(self.botao), self.novaconf()])
        self.botao.pack(side=RIGHT)

    def novaconf(self):
        self.entrada = Entry(self.container2)
        self.entrada.place(x=0, y=80, width=200, height=20)
        self.entrada.pack(side=LEFT)

        self.save = Button(self.container3, text="Salvar",
                           command=lambda: [hide_button(self.entrada), hide_button(self.save), show_button(self.botao),
                                            self.salvaconf(), hide_button(self.menu)])
        self.save.pack(side=BOTTOM)

        self.nsei = StringVar()
        self.nsei.set(self.sla[2])
        self.menu = OptionMenu(self.container4, self.nsei, *self.sla)
        self.menu.pack(side=BOTTOM)

    def salvaconf(self):
        self.conf = Button(self.container, text=self.entrada.get(), command=self.conf)
        self.conf.pack(side=BOTTOM)

    def conf(self):
        a = format(self.nsei.get())
        janela2 = Tk()
        janela2.title(self.entrada.get())
        janela2.geometry("400x400")

        self.container6 = Frame(janela2)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(janela2)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(janela2)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()
        self.container9 = Frame(janela2)
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.pack()
        self.container10 = Frame(janela2)
        self.container10["padx"] = 20
        self.container10["pady"] = 5
        self.container10.pack()
        self.container11 = Frame(janela2)
        self.container11["padx"] = 20
        self.container11["pady"] = 5
        self.container11.pack()
        self.container12 = Frame(janela2)
        self.container12["padx"] = 20
        self.container12["pady"] = 5
        self.container12.pack()
        self.container13 = Frame(janela2)
        self.container13["padx"] = 0
        self.container13["pady"] = 0
        self.container13.pack()
        self.container14 = Frame(janela2)
        self.container14["padx"] = 0
        self.container14["pady"] = 0
        self.container14.pack()

        self.lbl2 = Label(self.container6, text="Insira seus itens")
        self.lbl2.pack(side=LEFT)
        self.inserir2 = Button(self.container7, text="+",
                               command=lambda: [hide_button(self.inserir2), hide_button(self.lbl2), self.inserir()])
        self.inserir2.pack()

        janela2.mainloop()

    def inserir(self):
        self.lbl = Label(self.container6, text="Insira o nome do item")
        self.lbl.pack(side=LEFT)
        self.item = Entry(self.container6)
        self.item.pack(side=LEFT)

        self.lbl2 = Label(self.container7, text="Insira a quantidade")
        self.lbl2.pack(side=LEFT)
        self.item2 = Entry(self.container7)
        self.item2.pack(side=LEFT)

        self.lbl3 = Label(self.container8, text="Insira a categoria")
        self.lbl3.pack(side=LEFT)
        self.item3 = Entry(self.container8)
        self.item3.pack(side=LEFT)

        self.lbl4 = Label(self.container9, text="Insira o preço")
        self.lbl4.pack(side=LEFT)
        self.item4 = Entry(self.container9)
        self.item4.pack(side=LEFT)

        self.lbl5 = Label(self.container10, text="Insira limite")
        self.lbl5.pack(side=LEFT)
        self.item5 = Entry(self.container10)
        self.item5.pack(side=LEFT)

        self.inserir1 = Button(self.container11, text="Inserir",
                               command=lambda: [self.lbl.pack_forget(), self.lbl2.pack_forget(),
                                                self.lbl3.pack_forget(), self.lbl4.pack_forget(),
                                                self.lbl5.pack_forget(), self.item.pack_forget(),
                                                self.item2.pack_forget(), self.item3.pack_forget(),
                                                self.item4.pack_forget(), self.item5.pack_forget(), self.item.get(),
                                                self.item2.get(), self.item3.get(), self.item4.get(), self.item5.get(),
                                                hide_button(self.inserir1), self.novalista()])
        self.inserir1.pack(side=BOTTOM)

    def novalista(self):
        self.add = Button(self.container12, text="+")
        self.add.pack(side=LEFT)
        self.num = Label(self.container12, text=self.item2.get())
        self.num.pack(side=LEFT)
        self.sub = Button(self.container12, text="-")
        self.sub.pack(side=LEFT)
        self.nom = Label(self.container12, text=self.item.get())
        self.nom.pack(side=LEFT)
        self.money = Label(self.container12, text=self.item4.get())
        self.money.pack(side=LEFT)
        self.category = Label(self.container12, text=self.item3.get())
        self.category.pack(side=LEFT)
        self.money = Label(self.container12, text=self.item4.get())
        self.money.pack()


root = Tk()
root.title("Aplicativo de organizações")
root.geometry("400x400")
Organizador(root)
root.mainloop()