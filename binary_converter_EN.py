import customtkinter as ctk


def is_binary(text):
    """Return True if `text` is an acceptable binary string for the Entry widget.

    Rules:
    - allow empty string (so user can clear field)
    - disallow leading '0' (prevents leading zeros)
    - allow only '0' and '1' characters
    """
    if text == '':
        return True
    if text[0] == '0':
        return False
    if all(c in '01' for c in text):
        return True
    return False


def is_decimal(text):
    """Return True if `text` is an acceptable decimal string for the Entry widget.

    Rules:
    - allow empty string (so user can clear field)
    - allow only digits 0-9
    """
    if text == '':
        return True
    if all(c in '0123456789' for c in text):
        return True
    return False


def binary_to_decimal():
    """Convert the value from `binary_entry` to decimal and update `result_label`.

    Algorithm: parse bits, reverse (LSB first) and sum bit * 2 ** index.
    """
    binary = entry1.get()
    if binary == '':
        result_label.configure(text='Please, \ninsert a valid binary number.')
    else:
        list_binary = [int(ch) for ch in binary]
        r = list(reversed(list_binary))
        decimal_value = [int(r[i]) * (2 ** i) for i in range(len(r))]
        result_label.configure(text=f'The decimal of {binary} is:\n{sum(decimal_value)}')


def decimal_to_binary():
    """Convert the value from `decimal_entry` to binary and update `result_label2`.

    Uses repeated division by 2 (collecting remainders) and reverses the bits.
    """
    try:
        decimal = int(entry2.get())
        if decimal == 0:
            result_label2.configure(text='The binary of 0 is:\n0')
            return
        binarys = []
        while decimal != 0:
            if str(decimal / 2).endswith('0'):
                binarys.append(0)
                decimal //= 2
            else:
                binarys.append(1)
                decimal //= 2

        r = list(reversed(binarys))
        binary = ''.join(str(i) for i in r)
        result_label2.configure(text=f'The binary of {entry2.get()} is: \n{binary}')
    except ValueError:
        result_label2.configure(text='Please, \ninsert a valid decimal number.')


# --- Interface configuration ---
window = ctk.CTk()
ctk.set_appearance_mode('dark')
window.geometry('360x360')
window.title('Binary Calculator')

# Registers validators for Entry widgets (used by validatecommand)
vcmd_binary = (window.register(is_binary), '%P')
vcmd_decimal = (window.register(is_decimal), '%P')

ctk.CTkLabel(window, text='--- Binary/Decimal Converter ---', font=('arial', 18, 'bold')).pack(pady=10)

tab = ctk.CTkTabview(window)
tab.pack()
tab.add('Binary → Decimal')
tab.add('Decimal → Binary')

# Tab: Binary → Decimal
ctk.CTkLabel(tab.tab('Binary → Decimal'), text='Write a binary number', font=('arial', 18, 'bold')).pack(pady=10)
entry1 = ctk.CTkEntry(tab.tab('Binary → Decimal'), font=('arial', 18, 'bold'), validate='key', validatecommand=vcmd_binary)
entry1.pack(pady=10)
button = ctk.CTkButton(tab.tab('Binary → Decimal'), font=('arial', 18, 'bold'), text='Convert', command=binary_to_decimal)
button.pack(pady=10)
result_label = ctk.CTkLabel(tab.tab('Binary → Decimal'), text='', font=('arial', 22, 'bold'))
result_label.pack()

# Tab: Decimal → Binary
ctk.CTkLabel(tab.tab('Decimal → Binary'), text='Write a decimal number', font=('arial', 18, 'bold')).pack(pady=10)
entry2 = ctk.CTkEntry(tab.tab('Decimal → Binary'), font=('arial', 18, 'bold'), validate='key', validatecommand=vcmd_decimal)
entry2.pack(pady=10)
button2 = ctk.CTkButton(tab.tab('Decimal → Binary'), font=('arial', 18, 'bold'), text='Convert', command=decimal_to_binary)
button2.pack(pady=10)
result_label2 = ctk.CTkLabel(tab.tab('Decimal → Binary'), text='', font=('arial', 22, 'bold'))
result_label2.pack()

window.mainloop()