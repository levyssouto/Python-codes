import os
import random as rd

def pai_e_filho():

    '''
    os.wait()
        Aguarda a conclusão de um processo filho e retorna uma tupla contendo seu pid e indicação de status de saída: um número de 16 bits, cujo byte baixo é o número do sinal que matou o processo e cujo byte alto é o status de saída (se o sinal número é zero); o bit alto do byte baixo é definido se um arquivo principal foi produzido.
        Se não houver filhos que possam ser esperados, ChildProcessError é levantada.
        waitstatus_to_exitcode() pode ser usado para converter o status de saída em um código de saída.
        Disponibilidade: Unix, não Emscripten, não WASI.
        Ver também
        As outras funções wait*() documentadas abaixo podem ser usadas para aguardar a conclusão de um processo filho específico e ter mais opções. waitpid() é o único também disponível no Windows.
    '''
    
    n = os.fork()
    
    if n > 0:
        print(f'processo pai PID: {os.getpid()} PPID: {os.getppid()}')
        print(os.wait())
        print('processo pai esperou o processo filho')

    else:
        print(f'processo filho PID: {os.getpid()} PPID: {os.getppid()}')
        for j in range(100000000):
            if (rd.random()<0.9999999):
                next
            else:
                print(f'processo filho terminou abruptamente em {j}')
                os.abort()
        print('processo filho terminou normalmente')


pai_e_filho()