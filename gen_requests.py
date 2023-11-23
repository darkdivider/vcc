import requests
from datetime import datetime
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, wait
import numpy as np
import random
import argparse
import pdb
import matplotlib.pyplot as plt
plt.switch_backend('agg')

def make_request(method='rn'):
    ostart = datetime.now()
    if method == 'rn':
        url = 'http://'+host+':' + str(ports[random.choice(list(ports.keys()))])+path
    
    elif method == 'rr':
        robin[0] = (robin[0]+1)%n_apps
        app = list(ports.keys())[robin[0]]
        url = 'http://'+host+':' + str(ports[app]) + path

    elif method == 'ls':
        app = min(mean_times, key=lambda k: mean_times[k])
        url = 'http://'+host+':' + str(ports[app]) + path

    elif method == 'lt':
        app = min(last_times, key=lambda k: last_times[k])
        url = 'http://'+host+':' + str(ports[app])+path

        
    with requests.Session() as s:
        lag = None
        response = None
        s.keep_alive = False
        start = datetime.now()
        try:
            response = s.get(url, headers={'Connection': 'close'})
            lag = (datetime.now()-start).total_seconds()
        except Exception as e:
            rtf += 1
        finally:
            s.close()
    key = response.text.split()[-1]
    mean_times[key] = (mean_times[key]*rtc[key]+lag)/(rtc[key]+1)
    rtc[key] += 1
    rtl[key].append(lag)
    last_times[key] = lag
    overheads.append((start-ostart).total_seconds())
    return response, lag


def runtest_flood(n_iter=100, method='random'):

    with ThreadPoolExecutor() as executor:
        start = datetime.now()
        # Send a GET request
        futures = [executor.submit(make_request, method)
                   for _ in tqdm(range(n_iter))]
        wait(futures)
        cycle_time.append((datetime.now()-start).total_seconds())

def runtest_seq(n_iter=100,method='random'):
    start = datetime.now()
    for _ in tqdm(range(n_iter)):
        make_request(method)
    cycle_time.append((datetime.now()-start).total_seconds())

def runtest_ran(n_iter=100,method='random'):
    start = datetime.now()
    for _ in tqdm(range(n_iter)):
        time.sleep(random.random())
        make_request(method)
    cycle_time.append((datetime.now()-start).total_seconds())

def trim_dict(D,t):
    if t>=len(D.keys()):
        return D
    return {key:D[key] for key in list(D.keys())[:t]}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n', help='Number of requests', type= int)
    parser.add_argument('--method', '-m', help='Balancing method(rn:random, rb:roundrobin, ls: least mean, lt: last)',
                        default = 'rn', choices = ['rn', 'rr', 'ls', 'lt'])
    parser.add_argument('--apps', '-a', help='Number of server apps running',
                         default = 7, choices = range(1,8), type=int)
    parser.add_argument('--req', '-r', help='requests mode(f: flood, r:random, s:sequential)',
                         default = 'f', choices = ['f', 'r', 's'], )
    args = parser.parse_args()
    ports = {'app1': 5001, 'app2': 5002, 'app3': 5003,
             'app4': 5004, 'app5': 5005, 'app6': 5006, 'app7': 5007}
    host = "localhost"
    path = "/"

    n_apps = args.apps
    method = args.method
    n = args.n

    ports = trim_dict(ports,n_apps)
    
    mean_times = {key: 0 for key in ports.keys()}
    last_times = {key: 0 for key in ports.keys()}

    overheads=[]
    cycle_time = [0]
    robin = [0]

    rtl = {key:[] for key in ports.keys()}
    rtc = {key:0 for key in ports.keys()}
    rtf = 0

    if args.req=='f':
        runtest_flood(n, method)
    elif args.req=='r':
        runtest_ran(n, method)
    else:
        runtest_seq(n, method)
        
    lags = np.concatenate(list(rtl.values()))
    mean_lag = lags.mean()
    std_lag = lags.std()
    
    methods = {'rr':'RoundRobin', 'rn': 'Random', 'ls': 'Least time', 'lt': 'Least Last time'}

    print(f'\nNumber of apps: {len(ports.keys())}')
    print(f'Method : {methods[method]}')
    print(f'Cycletime / request : {sum(cycle_time)/n:0.3g} s')
    print(f'Response time / request : {mean_lag:0.3g} +/- {std_lag:0.3g} s')
    print(f'Overheads / request : {sum(overheads)/n:0.3g} s')
    print(rtc)
    plt.plot(rtc.values())
    plt.show()
