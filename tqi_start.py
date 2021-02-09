from os import popen, kill, system
import time
import sys
import subprocess
import docker_control

def open_dev():
    popen('prospect-mail')
    popen('slack')
    popen('code')
    popen('/snap/intellij-idea-community/273/bin/idea.sh')
    popen('teams')
    popen('/usr/local/pulse/pulseUi')

def restart_docker_images():
    docker_control.check_and_restart(docker_control.consumer_images)

def open_casual():
    popen('xdg-open https://web.whatsapp.com/')
    time.sleep(0.1)
    popen('xdg-open https://www.youtube.com')
    time.sleep(0.1)
    popen('xdg-open https://mail.google.com/mail/u/0/#inbox')
    time.sleep(0.1)
    popen('xdg-open https://calendar.google.com/calendar/u/0/r')
    time.sleep(0.1)
    popen('xdg-open https://trello.com/b/FayUjhWu/fugenda')
    # popen('spotify')

def kill_processes():
    process_name = [
        'prospect-mail',
        'slack',
        'code',
        'idea.sh',
        'teams',
        'pulseUi',
        'chrome',
        'spotify'
    ]
    s, e = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE).communicate()

    for line in s.splitlines():
        for target_process in process_name:
            if target_process in str(line): 
                pid = int(line.split(None, 1)[0])
                kill(pid, 9)

def open_selector(intensity):
    if intensity >= 1:
        open_casual()

    if intensity >= 2:
        open_dev()
        
    if intensity >= 3:
        restart_docker_images()

if __name__ == "__main__":
    kill_processes()
    
    try:
        intensity = int(sys.argv[1])
    except :
        intensity = 1

    open_selector(intensity)         
    