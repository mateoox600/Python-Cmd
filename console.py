import os
import ctypes

class Console():
    def __init__(self, idx : int = 0):
        self.console_id = idx

    def run(self):
        print('Python Cmd by Mateoox600 \n')
        while True:
            os.system('PCMD > H:/PythonConsole/pcmd.bat')
            try:
                console_input = input(f'{os.getcwd()}> ').split(' ')
            except:
                print('\n \n')
                break
            try:
                process_result = self.process(console_input[0], list(*[console_input[1:]]))

                if process_result == 'stop': break
                else:
                    if process_result == None: continue
                    else: print(f'{process_result}')
            except:
                print(f'somethings got wrong with the command \'{console_input[0]}\' try help')

    def process(self, cmd : str, args):
        if cmd == 'stop': return 'stop'
        elif cmd == 'id': return f'{self.console_id}'
        elif cmd == 'help': return self.get_help()
        elif cmd == 'calc':
            if len(args) < 1: return 'calc <calcul: 1+1>'
            return f'{self.calc(args)}'
        elif cmd == 'cd':
            if len(args) < 1: return 'cd <directory>'
            try:
                os.chdir(' '.join(args))
            except:
                return 'This folder dosn\'t exist'
            return
        elif cmd == 'dir':
            result = ''
            for dir in os.listdir(): result += f' {dir} \n'
            return result
        elif cmd == 'mkdir':
            if len(args) < 1: return 'mkdir <name>'
            os.mkdir(' '.join(args)); return
        elif cmd == 'ren':
            if len(args) < 1: return 'ren <old name>/<new name>'
            names = ' '.join(args).split('/'); os.rename(names[0], names[1]); return
        elif cmd == 'start': os.startfile('H:\PythonConsole\pcmd.bat'); return
        elif cmd == 'execute': 
            if len(args) < 1: return 'execute <file>'
            try:
                os.startfile(f"{os.getcwd()}/{''.join(args)}"); return
            except:
                return 'This file dosn\'t exist'
        elif cmd == 'mkfile':
            if len(args) < 1: return 'mkfile <file>'
            open(' '.join(args), 'x'); return
        return f'{cmd} is not a valid command. try help'
    
    def calc(self, args):
        calcul = ''.join(args)
        try:
            return calcul  + " = " + str(eval(calcul))
        except:
            return f'{calcul} is not valid'
    
    def get_help(self):
        help_message = 'Help: \n'
        help_message += '- stop : stop the console \n'
        help_message += '- id : return your console id \n'
        help_message += '- calc <calcul> : make the calcul that you input \n'
        help_message += '- cd <directory> : move to the directory that you input \n'
        help_message += '- dir : output all child of the folder you are in \n'
        help_message += '- mkdir <name> : create a file with the name input \n'
        help_message += '- ren <old name>/<new name> : rename the file with the old name with the new name \n'
        help_message += '- start : start a new console \n'
        help_message += '- execute <file name> : execute the file you input it \n'
        help_message += '- mkfile <file name>.<file extension> : create a new file \n'
        return help_message

