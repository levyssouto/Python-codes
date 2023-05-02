import os

def pai_e_filho():

    '''
    os.fork()
        Faz um fork de um processo filho. Retorna 0 no filho e o ID de processo do filho no pai. Se ocorrer um erro, uma OSError é levantada.
        Note que algumas plataformas incluindo FreeBSD <= 6.3 e Cygwin têm problemas conhecidos ao usar fork() a partir de um thread.
        Levanta um evento de auditoria os.fork com nenhum argumento.
        Alterado na versão 3.8: Chamar fork() em um subinterpretador não é mais suportado (RuntimeError é levantada).
        Aviso: veja ssl para aplicações que usam o módulo SSL com fork(). 
    
    os.getpid()
        Retorna o ID do processo atual.
        A função é um stub em Emscripten e WASI, veja Plataformas WebAssembly para mais informações.

    os.getppid()
        Retorna o ID do processo pai. Quando o processo pai é encerrado, no Unix, o ID retornado é o do processo init(1); no Windows, ainda é o mesmo ID, que já pode ser reutilizado por outro processo.
        Disponibilidade: Unix, Windows, não Emscripten, não WASI.
        Alterado na versão 3.2: Adicionado suporte para Windows.
    '''
    
    n = os.fork()
    
    if n > 0:
        for i in range(10):
            print(f'{i}: processo pai PID: {os.getpid()} PPID: {os.getppid()}')
            for j in range(100000000):
                next
    else:
        for i in range(10):
            print(f'{i}: processo filho PID: {os.getpid()} PPID: {os.getppid()}')
            for j in range(100000000):
                next


pai_e_filho()