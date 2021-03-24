from os import popen, kill, system
import time
import sys
import subprocess

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

def open_work():
    popen('prospect-mail')
    popen('slack')
    popen('teams')
    popen('code')
    popen('xdg-open https://jiraps.atlassian.net/secure/RapidBoard.jspa?rapidView=661')

def open_dev():
    popen('/snap/intellij-idea-community/273/bin/idea.sh')
    popen('/usr/local/pulse/pulseUi')
    restart_docker_images()

def restart_docker_images():
    docker_control.check_and_restart(docker_control.consumer_images)

def kill_processes():
    process_name = [
        'prospect-mail',
        'slack',
        'code',
        'idea.sh',
        # 'teams',
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
        open_work()
        
    if intensity >= 3:
        open_dev()

if __name__ == "__main__":
    kill_processes()
    
    try:
        intensity = int(sys.argv[1])
    except :
        intensity = 1

    open_selector(intensity)         
    