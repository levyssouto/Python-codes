import os

def pai_e_filho():

    '''
    os.execvp(file, args)
        Todas essas funções executam um novo programa, substituindo o processo atual; eles não voltam. No Unix, o novo executável é carregado no processo atual e terá a mesma identificação de processo do chamador. Os erros serão relatados como exceções de OSError.
        O processo atual é substituído imediatamente. Objetos de arquivos abertos e descritores não são descarregados, então se houver dados em buffer nesses arquivos abertos, você deve descarregá-los usando sys.stdout.flush() ou os.fsync() antes de chamar uma função exec*.
        As variantes “l” e “v” das funções exec* diferem em como os argumentos da linha de comando são passados. As variantes “l” são talvez as mais fáceis de trabalhar se o número de parâmetros for fixo quando o código for escrito; os parâmetros individuais simplesmente se tornam parâmetros adicionais para as funções execl*(). As variantes “v” são boas quando o número de parâmetros é variável, com os argumentos sendo passados em uma lista ou tupla como o parâmetro args. Em qualquer caso, os argumentos para o processo filho devem começar com o nome do comando que está sendo executado, mas isso não é obrigatório.
        As variantes que incluem um “p” próximo ao final (execlp(), execlpe(), execvp() e execvpe()) usarão a variável de ambiente PATH para localizar o programa file. Quando o ambiente está sendo substituído (usando uma das variantes exec*e, discutidas no próximo parágrafo), o novo ambiente é usado como fonte da variável PATH As outras variantes, execl(), execle(), execv() e execve(), não usarão a variável PATH para localizar o executável; path deve conter um caminho absoluto ou relativo apropriado.
'''
    
    n = os.fork()
    
    if n > 0:
        print(f'processo pai PID: {os.getpid()} PPID: {os.getppid()}')
        print(os.wait())
        print('processo pai esperou o processo filho')

    else:
        print(f'processo filho PID: {os.getpid()} PPID: {os.getppid()}')
        os.execvp('python',('-m', 'fork10.py'))


pai_e_filho()