import speedtest

def check(*args):  # has to get arguments to run with `bind()`
    test = speedtest.Speedtest()
    test.get_best_server()
    down = test.download()
    up   = test.upload()
    # print('Download Speed: {:5.2f} Mb'.format( down/(1024*1024) ))
    # print('Upload Speed: {:5.2f} Mb'.format(   up/(1024*1024) ))
    
    return down, up