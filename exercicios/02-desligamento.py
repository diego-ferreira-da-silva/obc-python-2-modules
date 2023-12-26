import os

# 1- exemplo de como desligar o computador(Desliga imediatamente)
# os.system("shutdown /s") <- nesse caso, desliga por padrão em 1 minuto
# os.system("shutdown /s /t 0") <- Desliga o computador imediatamente
# os.system("shutdown / a") <- cancela o desligamento do computador


def turn_off_one_hour():
    os.system("shutdown /s /t 3600")


def turn_off_half_an_hour():
    os.system("shutdown /s /t 1800")


# def turn_off_choice():
#     tempo = input(
#         "Você deseja desligar seu computador em (M)Minutos ou (H)Horas? \n")
#     if tempo == "M" or tempo == "m":
#         min_desligamento = int(input("Em quantos minutos deseja desligar?\n")) * 60
#         os.system("shutdown /s /t {min_desligamento}")
#         min_desligamento /= min_desligamento
#         print(f"Seu computador será desligado em {min_desligamento} minutos")
#     else:
#         horas_desligamento = int(input("Em quantas horas deseja desligar?\n")) * 3600
#         os.system("shutdown /s /t {horas_desligamento}")
#         horas_desligamento /= horas_desligamento
#         print(f"Seu computador será desligado em {horas_desligamento} horas")

def cancel_shutdown():
    os.system("shutdown /a")

turn_off_one_hour()
cancel_shutdown()



