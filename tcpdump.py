def tcpdump():
    import subprocess,sys,time
    p = subprocess.Popen('tcpdump -q -n',stdout=subprocess.PIPE,encoding='utf-8',shell=True)
    # time.sleep(1)
    sys.stdout.flush()
    echo = p.stdout.read()
    print(echo[:-1].split('\n'))  # local: 172.19.143.195

tcpdump()