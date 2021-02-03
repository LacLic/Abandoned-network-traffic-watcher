"""Failed"""
# #!/usr/bin/env python3
# import subprocess
# import sys
# cmd1 = [f'python3 {sys.argv[0]}tcpdump.py']
# p1 = subprocess.Popen(cmd1,stdout=subprocess.STDOUT,stderr=subprocess.STDOUT,encoding='utf-8')

# cmd2 = ['python3',f'{sys.argv[0]}manage.py','runserver','0.0.0.0:8000']
# p2 = subprocess.Popen(cmd2, stdout=subprocess.PIPE, stdin=p1.stdout)

# print("Programme server started at http://0.0.0.0:8000/")
# while True:
#     console = print("Type 'quit' to quit the programme safely:\n  ")
#     if console == 'quit':
#         p1.terminate()
#         p2.terminate()
#         print("Quit successfully!")
#         break
