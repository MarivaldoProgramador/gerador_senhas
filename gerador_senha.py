import secrets
import string
from tkinter import *
from tkinter import messagebox


def gerar():
    try:
        tamanho = int(entry_size.get())
    except:
        messagebox.showerror('Erro', 'Apenas digite números!')
        entry_size.delete(0, END)
    else:
        itens = (string.ascii_letters + string.digits + string.punctuation)
        senha = [secrets.choice(itens)  for i in range(tamanho)]
        senha = ''.join(senha)

    
        tela.clipboard_clear()
        tela.clipboard_append(senha)
        tela.update()
        messagebox.showinfo('Copiado', f'\tSENHA: {senha}\n\nCopiado para a área de transferência!')
    

def vai(event):
    gerar()


tela = Tk()
tela.title('Gerador')
tela.geometry('200x150')
tela.configure(background='lightblue')

size = Label(tela, text='Tamanho', font=('arial', 14), background='lightblue')
entry_size = Entry(tela, width=10)
botao = Button(tela,
        text='Gerar',
        font=('arial', 12),
        background='#191970', 
        foreground='white',
        width=15,
        command=gerar
)

tela.bind('<Return>', vai)

size.pack(pady=10)
entry_size.place(x=65, y=45)
botao.place(x=25, y=90)


tela.mainloop()