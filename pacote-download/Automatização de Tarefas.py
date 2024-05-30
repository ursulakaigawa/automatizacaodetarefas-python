# Passo a passo do projeto

# 1. abrir sistema
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# para instalar pyautogui
import pyautogui
import time

# para que o computador tenha tempo de executar o código sem que uma linha atropele a outro, usar o pyaotogui.PAUSE = 0.5

pyautogui.PAUSE = 0.5

# abrir o navegador (Chrome)
pyautogui.press ("win")
pyautogui.write ("chrome")
pyautogui.press ("enter")

# entrar no site do sistema
pyautogui.write ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press ("enter")

# pode ser que demore alguns segundos para carregar o site, então usar o time.sleep (3) para pausar por 3 segundos somente na linha que eu quero.

time.sleep(3)

# 2. fazer login na plataforma

pyautogui.click(x=398, y=373)
pyautogui.write("ursula@hotmail.com")

pyautogui.press("tab") #passou para local de senha
pyautogui.write("sua senha aqui")

pyautogui.press("tab") #passou para botão de login
pyautogui.press("enter")

# 3. abrir base de dados de produtos

#pip install pandas numpy openpyxl
import pandas as pd

tabela = pd.read_csv ("produtos.csv")

print(tabela)

# 4. cadastrar o produto
#como algumas colunas da tabelas são de números, para nao dar erro transformar tudo em strings colocando str antes do linha de código

for linha in tabela.index:

    codigo = str(tabela.loc[linha, "codigo"])

    #clicar no campo de código do produto
    pyautogui.click(x=405, y=266)
    pyautogui.write(codigo)

    #preencher o código
    pyautogui.press("tab")

    #marca
    pyautogui.write (str(tabela.loc[linha, "marca"]))

    #preencher o código
    pyautogui.press("tab")

    #tipo
    pyautogui.write (str(tabela.loc[linha, "tipo"]))

    #preencher o código
    pyautogui.press("tab")

    #categoria
    pyautogui.write (str(tabela.loc[linha, "categoria"]))

    #preencher o código
    pyautogui.press("tab")

    #preço
    pyautogui.write (str(tabela.loc[linha, "preco_unitario"]))

    #preencher o código
    pyautogui.press("tab")


    #custo
    pyautogui.write (str(tabela.loc[linha, "custo"]))

    #preencher o código
    pyautogui.press("tab")

    #obs
    obs = (str(tabela.loc[linha, "obs"]))
    if obs != "nan":
        pyautogui.write(obs)
    #preencher o código
    pyautogui.press("tab")

    #apertar o botao
    pyautogui.press("enter")
    pyautogui.scroll(5000)

#passar pro próximo campo
#repetir até o final