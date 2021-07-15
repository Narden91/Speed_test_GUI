import speedtest

def check(*args):  # has to get arguments to run with `bind()`
    test = speedtest.Speedtest()
    test.get_best_server()
    down = test.download()
    up   = test.upload()
    
    return down, up