import docker
import sys

orchestrator_images = [
    'docker_redis-cluster_1',
    'aws_localstack_ssm',
    'qrcode-orchestrator-db',
]

consumer_images = [
    'nodedns',
    'cayman-rabbit-server'
]

def check_and_restart(container_names, force = False):
    client = docker.from_env()
    for c in client.containers.list(all = True):
        if c.name in container_names:
            print(f'Container {c.name} is {c.status}')
            if c.status != 'running' or force:
                c.restart()
                print(f'Container {c.name} restarted...')

def force_restart(all=False):
    client = docker.from_env()
    names = [c.name for c in client.containers.list(all=all)]
    check_and_restart(names, True)

def kill_everything():
    client = docker.from_env()
    for c in client.containers.list(): 
        c.stop()
        print(f'Container {c.name} killed...')

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('''
    Opções:
            active - restart todos ativos
            all - restar todos containers
            kill - mata todos containers
            c (f) - levanta (ou força restart) consumer
            o (f) - levanta (ou força restart) orchestrator
        ''')
    else:
        opt = sys.argv[1] if len(sys.argv)>=2 else 'c'
        ensure = sys.argv[2] if len(sys.argv)>=3 else 'n'
        force = True if ensure == 'f' else False

        if opt == 'active':
            force_restart()
        elif opt == 'all':
            force_restart(True)
        elif opt == 'kill':
            kill_everything()
        else:
            images = consumer_images if opt == 'c' else orchestrator_images
            check_and_restart(images, force=force)   