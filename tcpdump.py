"""
08:18:39.506290 IP 172.19.128.1.54239 > 172.19.137.44.38797: tcp 62
08:18:39.555459 IP 172.19.128.1.54239 > 172.19.137.44.38797: tcp 0
08:18:39.560364 IP 172.19.128.1.53 > 172.19.137.44.40162: UDP, length 278
08:18:39.581865 IP 172.19.128.1.53 > 172.19.137.44.40162: UDP, length 179
08:18:39.631127 IP 13.107.5.93.443 > 172.19.137.44.39216: tcp 0
08:18:39.637724 IP 172.19.128.1.54239 > 172.19.137.44.38797: tcp 55
08:18:39.679623 IP 172.19.128.1.54239 > 172.19.137.44.38797: tcp 0
08:18:39.681551 IP 13.107.5.93.443 > 172.19.137.44.39216: tcp 1436
08:18:39.829211 IP 13.107.5.93.443 > 172.19.137.44.39216: tcp 1436
08:18:40.129115 IP 13.107.5.93.443 > 172.19.137.44.39216: tcp 1436
08:18:40.180882 IP 13.107.5.93.443 > 172.19.137.44.39216: tcp 326
"""
"""
[('172.19.128.1.54238', 'tcp', '0')]
[('172.19.128.1.54238', 'tcp', '0')]
[('172.19.128.1.53', 'UDP', '260')]
[('172.19.128.1.53', 'UDP', '207')]
[('172.19.128.1.54238', 'tcp', '0')]
[('172.19.128.1.54238', 'tcp', '0')]
"""

def parse_the_echo(text):
    import re
    pattern = re.compile(  # Regex
      r'IP (.*)\.[0-9]*? > .*?: (...).*?([0-9][0-9]*)', re.S) # items[0]: source ip 发送方ip，[1]: protocal(previous 3 letters) 协议名（显示前三个字母），[2]: length 长度
    items = re.findall(pattern, text)
    try:
        # print(items)
        return items[0][0],items[0][1],int(items[0][2]) # src ip, port, protocol, length(str)
    except Exception:
        pass

def tcpdump(local_ip,debug=False):
    import subprocess,time
    global total
    total = {}
    cmd1 = [f'tcpdump -q -n dst {local_ip}']
    p1 = subprocess.Popen(cmd1,stdout=subprocess.PIPE,encoding='utf-8',shell=True,stderr=subprocess.STDOUT,bufsize=0) # dst: destination 接收方, src: source 发送方
    cmd2 = ['grep', '--line-buffered', '-a', '-o', '-E' , '.*IP.*']
    p2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE, stdin=p1.stdout)
    
    while True:
        echo = p2.stdout.readline().strip().decode('utf-8')
        if debug:
            time.sleep(0.05) # debug, need to be removed
        ip, protocol, lenth = parse_the_echo(echo)  # local: 172.19.143.195
        try:
            total[ip] += lenth
        except KeyError:
            total[ip] = lenth
        print(total)
        
    p.stdout.close()

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
tcpdump(local_ip,debug=True)