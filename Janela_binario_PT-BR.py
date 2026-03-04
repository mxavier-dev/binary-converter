import customtkinter as ctk


def so_binario(char):
    """Valida se a string `char` é um número binário aceitável para o Entry.

    Regras:
    - aceita string vazia (permite apagar o campo)
    - não permite que a entrada comece com '0' (evita zeros à esquerda)
    - permite somente os caracteres '0' e '1'
    """
    if char == '':
        return True
    if char[0] == '0':
        return False
    if all(c in '01' for c in char):
        return True
    return False


def so_decimal(char):
    """Valida se a string `char` é um número decimal aceitável para o Entry.

    Regras:
    - aceita string vazia (permite apagar o campo)
    - permite somente dígitos de 0 a 9
    """
    if char == '':
        return True
    if all(c in '0123456789' for c in char):
        return True
    return False


def binario_decimal():
    """Converte o conteúdo de `entry1` (binário) para decimal e atualiza `resultado`.

    O algoritmo transforma a string em lista de bits, inverte a ordem
    (LSB primeiro) e soma cada bit multiplicado pela potência de 2.
    """
    binario = entry1.get()
    if binario == '':
        resultado.configure(text='Por favor, \ninsira um número binário válido.')
    else:
        list_binario = [int(ch) for ch in binario]
        r = list(reversed(list_binario))
        soma = [int(r[i]) * (2 ** i) for i in range(len(r))]
        resultado.configure(text=f'O decimal de {binario} é:\n{sum(soma)}')


def decimal_binario():
    """Converte o conteúdo de `entry2` (decimal) para binário e atualiza `resultado2`.

    A função divide sucessivamente por 2 e coleta os restos (bits),
    depois reverte a lista para obter a representação binária corretamente.
    """
    try:
        decimal = int(entry2.get())
        if decimal == 0:
            resultado2.configure(text='O binário de 0 é:\n0')
            return
        binarios = []
        while decimal != 0:
            # determina o bit atual (0 ou 1) e reduz o valor pela divisão inteira
            if str(decimal / 2).endswith('0'):
                binarios.append(0)
                decimal //= 2
            else:
                binarios.append(1)
                decimal //= 2

        r = list(reversed(binarios))
        binario = ''.join(str(i) for i in r)
        resultado2.configure(text=f'O binário de {entry2.get()} é: \n{binario}')
    except ValueError:
        resultado2.configure(text='Por favor, \ninsira um número decimal válido.')


# --- Configuração da interface ---
janela = ctk.CTk()
ctk.set_appearance_mode('dark')
janela.geometry('360x360')
janela.title('Calculadora Binária')

# registra validadores para os Entry widgets (usados por validatecommand)
vcmd_binario = (janela.register(so_binario), '%P')
vcmd_decimal = (janela.register(so_decimal), '%P')

ctk.CTkLabel(janela, text='--- Conversor binária/decimal ---', font=('arial', 18, 'bold')).pack(pady=10)

tab = ctk.CTkTabview(janela)
tab.pack()
tab.add('Binário → Decimal')
tab.add('Decimal → Binário')

# Aba: Binário → Decimal
ctk.CTkLabel(tab.tab('Binário → Decimal'), text='Escreva um binário', font=('arial', 18, 'bold')).pack(pady=10)
entry1 = ctk.CTkEntry(tab.tab('Binário → Decimal'), font=('arial', 18, 'bold'), validate='key', validatecommand=vcmd_binario)
entry1.pack(pady=10)
botao = ctk.CTkButton(tab.tab('Binário → Decimal'), font=('arial', 18, 'bold'), text='Converter', command=binario_decimal)
botao.pack(pady=10)
resultado = ctk.CTkLabel(tab.tab('Binário → Decimal'), text='', font=('arial', 22, 'bold'))
resultado.pack()

# Aba: Decimal → Binário
ctk.CTkLabel(tab.tab('Decimal → Binário'), text='Escreva um decimal', font=('arial', 18, 'bold')).pack(pady=10)
entry2 = ctk.CTkEntry(tab.tab('Decimal → Binário'), font=('arial', 18, 'bold'), validate='key', validatecommand=vcmd_decimal)
entry2.pack(pady=10)
botao = ctk.CTkButton(tab.tab('Decimal → Binário'), font=('arial', 18, 'bold'), text='Converter', command=decimal_binario)
botao.pack(pady=10)
resultado2 = ctk.CTkLabel(tab.tab('Decimal → Binário'), text='', font=('arial', 22, 'bold'))
resultado2.pack()

janela.mainloop()