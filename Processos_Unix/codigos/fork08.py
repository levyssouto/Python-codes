import os
import sys
import time

"""
sys.stdin¶
sys.stdout¶
sys.stderr¶
    File objects used by the interpreter for standard input, output and errors:
        stdin is used for all interactive input (including calls to input());
        stdout is used for the output of print() and expression statements and for the prompts of input();
        The interpreter’s own prompts and its error messages go to stderr.
    These streams are regular text files like those returned by the open() function. Their parameters are chosen as follows:
        The encoding and error handling are is initialized from PyConfig.stdio_encoding and PyConfig.stdio_errors.
        On Windows, UTF-8 is used for the console device. Non-character devices such as disk files and pipes use the system locale encoding (i.e. the ANSI codepage). Non-console character devices such as NUL (i.e. where isatty() returns True) use the value of the console input and output codepages at startup, respectively for stdin and stdout/stderr. This defaults to the system locale encoding if the process is not initially attached to a console.
        The special behaviour of the console can be overridden by setting the environment variable PYTHONLEGACYWINDOWSSTDIO before starting Python. In that case, the console codepages are used as for any other character device.
        Under all platforms, you can override the character encoding by setting the PYTHONIOENCODING environment variable before starting Python or by using the new -X utf8 command line option and PYTHONUTF8 environment variable. However, for the Windows console, this only applies when PYTHONLEGACYWINDOWSSTDIO is also set.
        When interactive, the stdout stream is line-buffered. Otherwise, it is block-buffered like regular text files. The stderr stream is line-buffered in both cases. You can make both streams unbuffered by passing the -u command-line option or setting the PYTHONUNBUFFERED environment variable.
    Alterado na versão 3.9: Non-interactive stderr is now line-buffered instead of fully buffered.
    Nota
    To write or read binary data from/to the standard streams, use the underlying binary buffer object. For example, to write bytes to stdout, use sys.stdout.buffer.write(b'abc').
    However, if you are writing a library (and do not control in which context its code will be executed), be aware that the standard streams may be replaced with file-like objects like io.StringIO which do not support the buffer attribute.
"""

sys.stdout.write('Preparado para o fork? (tecle <enter> para continuar)')
sys.stdout.flush()

sys.stdin.readline()

pidDepoisDoFork = os.fork()

if pidDepoisDoFork > 0:
    print(f'Dentro do processo pai\nPID: {os.getpid()} PPID: {os.getppid()}')
    time.sleep(10)
    print('fim do processo pai')
else:
    print(f'Dentro do processo filho\nPID: {os.getpid()} PPID: {os.getppid()}')
    time.sleep(20)
    print('fim do processo filho')

# inverter os valores do sleep