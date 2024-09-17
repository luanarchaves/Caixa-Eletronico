import customtkinter



def get_value():
    number_str = retirar_valor.get("1.0", "end-1c")

    try:
        number = int(number_str.replace(',', '.'))
    except ValueError:
        print("Erro: Valor não pode ser convertido para número.")


    numeros = ['100,00', '50,00', '20,00', '10,00', '5,00', '2,00', '1,00']
    value = [100, 50, 20, 10, 5, 2, 1]
    notas = [0, 0, 0, 0, 0, 0, 0]
    i = 0

    for i in range(len(value)):
        if number >= value[i]:
            while number >= value[i]:
                number -= value[i]
                notas[i] += 1    

    resultado_label.configure(text=(
        f'{notas[0]} nota(s) de R$ {numeros[0]}\n'
        f'{notas[1]} nota(s) de R$ {numeros[1]}\n'
        f'{notas[2]} nota(s) de R$ {numeros[2]}\n'
        f'{notas[3]} nota(s) de R$ {numeros[3]}\n'
        f'{notas[4]} nota(s) de R$ {numeros[4]}\n'
        f'{notas[5]} nota(s) de R$ {numeros[5]}\n'
        f'{notas[6]} nota(s) de R$ {numeros[6]}'
    ))


caixa_eletronico = customtkinter.CTk()
caixa_eletronico.geometry("500x400")

titulo_fonte = customtkinter.CTkFont(size=30, weight="bold") 
title = customtkinter.CTkLabel(caixa_eletronico, text='Caixa Eletrônico', font=titulo_fonte)
title.pack(padx=20, pady=20)

retirar_valor = customtkinter.CTkTextbox(caixa_eletronico, corner_radius=15, width=300, height=50)
retirar_valor.pack(padx=20, pady=20)

resultado_label = customtkinter.CTkLabel(caixa_eletronico, text="")
resultado_label.pack(pady=10)

button = customtkinter.CTkButton(caixa_eletronico, text="Retirar", command=get_value)
button.pack(padx=20, pady=20)

caixa_eletronico.mainloop()