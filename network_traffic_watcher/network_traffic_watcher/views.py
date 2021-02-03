
from django.shortcuts import render
import json

def chart(request):
    with open('temp','r') as fio:
        data = json.load(fio)
        data = sorted(data.items(), key=lambda data : data[1], reverse=True) 
        fio.close()
    
    cnt = 1
    dic = {}
    ip = []
    flow = []
    for element in data:
        try:
            ip.append(element[0])
            flow.append(element[1])
            cnt += 1
            if cnt > 10:
                break
        except Exception:
            break
    ip_str = str(ip).replace('\'', '\"')
    flow_str = str(flow)
    dic['ip'] = ip_str
    dic['flow'] = flow_str
    print(data)

    return render(request, 'chart.html', dic)
