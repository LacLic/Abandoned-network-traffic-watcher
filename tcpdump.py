def tcpdump(local_ip):
    import subprocess,sys,time,os
    env = os.environ.copy()
    env['PYTHONUNBUFFERED'] = '1'
    p = subprocess.Popen(f'tcpdump -q -n -u dst {local_ip}',stdout=subprocess.PIPE,encoding='utf-8',shell=True,env=env,stderr=subprocess.STDOUT,bufsize=0) # dst: destination 接收方, src: source 发送方
    while True:
        echo = p.stdout.readline()
        time.sleep(0.1)
        print(echo.strip())  # local: 172.19.143.195
        # for line in iter(p.stdout.readline, b''):
        #     print(line)
    p.stdout.close()

# def get_local_ip(): # useless
#     import socket
#     return socket.gethostbyname(socket.gethostname())

def get_host_ip():
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

local_ip = get_host_ip()
print(local_ip)
tcpdump(local_ip)