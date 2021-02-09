from os import kill, popen
import subprocess

def restart_process(target_process):
    s, e = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE).communicate()

    for line in s.splitlines():
        if target_process in str(line):
            pid = int(line.split(None, 1)[0])
            kill(pid, 9)
    popen(f'{target_process}')

if __name__ == "__main__":
    restart_process('prospect-mail')


