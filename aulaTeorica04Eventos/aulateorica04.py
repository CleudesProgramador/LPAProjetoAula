import sched
import time

# import keyboard as keyboard
#
# #
# # # Evento de Teclado
# #
# # def on_key_event(event):
# #     if event.event_type == keyboard.KEY_DOWN:
# #         print(f'Tecla pressionada: {event.name}')
# #         if event.name == 'a':
# #             print('a em especial')
# #
# #
# # # main
# # keyboard.on_press(on_key_event) # Registra o hook para o evento de tecla pressionada
# #
# # # Mantém o código em execução para capturar os eventos de tecla indefinidamente
# #
# # try:
# #     while True:
# #         pass
# # except KeyboardInterrupt:
# #     print('Programa interrompido pelo usuário.')
#
#
# # 1.2 Evento de tempo
#
# def exibir_mensagem(mensagem):
#     print(mensagem)
#
#
# def agendar_evento(scheduler, intervalo, mensagem):
#     # agendando o proximo evento
#     scheduler.enter(intervalo, 1, agendar_evento, (scheduler, intervalo, mensagem))
#
#     # Exibindo a mensagem
#     exibir_mensagem(mensagem)
#
#
# # main -> cria uma instância do objeto scheduler
# new_scheduler = sched.scheduler(time.time, time.sleep)
#
# # agendando o primeiro evento
# agendar_evento(new_scheduler, 1, 'Esta é a mensagem agendada a cada 1 segundo!')
#
# print('Esperando para exibir as mensagens agendadas...')
#
# # Executando o scheduler em loop
# new_scheduler.run()


# 3 - Definindo o decorator
#
# def meu_decorator(funcao):
#     def wrapper():
#         print('A função será executada agora.')
#         funcao()
#         print('A função foi executada!')
# #     return wrapper
# #
# # @meu_decorator
# # def minha_funcao():
# #     print('Esta é a função original.')
#
#
# # Método main -> Chamando a função decorada
# # minha_funcao()
#
# definindo o decorator para medir o tempo de execução

def medir_tempo(function):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = function(*args, **kwargs)
        fim = time.time()
        duracao = fim - inicio
        print(f'A função levou {duracao} segundos.')
        return resultado

    return wrapper
#
# # aplicando o decorator usando o simbolo @
#
# @medir_tempo
# def exemplo_funcao(tempo_espera):
#     time.sleep(tempo_espera)
#     print('A função foi executada.')
#
# # Chamando a função decorada
# exemplo_funcao(2)
@medir_tempo
def retorna_lista_sem_comprehension(max_value):
    lista_pares = []
    for num in range(max_value):
        if num % 2 == 0:
            lista_pares.append(num)
    return lista_pares

@medir_tempo
def retorna_lista_com_comprehension(max_value):
    lista_pares = [num for num in range(max_value) if num % 2 == 0]
    return


# Main
retorna_lista_sem_comprehension(1000000000)
retorna_lista_com_comprehension(1000000000)




























