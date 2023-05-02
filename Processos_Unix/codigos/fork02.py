import os

def pai_e_filho():

    '''
    fork permite criar vários processos a partir de um processo pai
    vamos criar 5 processos para cada processo filho
    '''
    
    numProc = 5
    pid = os.fork()
    
    if pid > 0:
        print(f'Processo pai PID: {os.getpid()} PPID: {os.getppid()}')
        for j in range(100000000):
            next
    else:
        for i in range(numProc):
            pid = os.fork()
            print(f'{i}: processo filho PID: {os.getpid()} PPID: {os.getppid()}')
            for j in range(100000000):
                next


pai_e_filho()