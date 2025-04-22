import pyautogui
import time

# Quantas vezes repetir o processo
repeticoes = 200


# Tempo para se preparar antes de começar
print("Você tem 5 segundos para posicionar o mouse sobre a imagem.")
time.sleep(5)
centena = 0
dezena = 0
unidade = 1

for i in range(repeticoes):
    print(f"Executando iteração {i + 1}")
    unidade = unidade + 1
    if(unidade > 9):
        dezena = dezena + 1
        unidade = 0
    if(dezena > 9):
        centena = centena + 1
        dezena = 0
    
    # Clique com o botão direito
    pyautogui.click(button='right')
    time.sleep(0.5)

    # Pressiona a seta para baixo 2x e ENTER para escolher "Salvar imagem como..."
    pyautogui.press('down', presses=2, interval=0.2)
    pyautogui.press('enter')
    time.sleep(1.5)  # tempo para a janela de salvar abrir

    # Pressiona ENTER para confirmar o nome e salvar
    pyautogui.press(str(centena))
    pyautogui.press(str(dezena))
    pyautogui.press(str(unidade))
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(1.5)

    # Pressiona seta para direita para ir para próxima imagem
    pyautogui.click(button='left')
    time.sleep(1)

print("Processo concluído.")