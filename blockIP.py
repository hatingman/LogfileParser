import codecs, re, os, sys
from collections import Counter


def iplistcsv(filename, ip):
    with codecs.open(filename, 'r', 'utf-8') as f:
        log = f.read()
        ipl = re.findall(ip, log)
    count=Counter(ipl)
    iplist = [ item for item in count if int(count[item]) > 3 ]
    return iplist


def iplistreg():

    ipmask = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    rulename = 'blockIP'
    filename = input('Enter the full path to the log file (including its full name)\n:> ')

    try:
        tf = open('temp.ib', 'w')
        tf.close()
    except:
        pass

    tfpath = os.path.dirname(sys.argv[0]) + '\\temp.ib'
    os.system(r'netsh advfirewall firewall show rule name="{}">{}'.format(str(rulename), str(tfpath)))

    with open(tfpath, 'r') as f:
        log = f.read()
        regipl = re.findall(ipmask, log)
        f.close()

    if str([line.rstrip('\n') for line in open(tfpath)][1]) == 'Rule Name:                            blockIP':

        fulllist = regipl + iplistcsv(filename=filename, ip=ipmask)
        list = ''.join( str(ip) + ',' for ip in fulllist)
        os.system(r'netsh advfirewall firewall set rule name="{}" new remoteip="{}"'.format(str(rulename), list))

    else:

        newlist = iplistcsv(filename=filename, ip=ipmask)
        list = ''.join( str(ip) + ',' for ip in newlist)
        os.system(r'netsh advfirewall firewall add rule name="{}" action=block dir=IN remoteip="{}"'.format(str(rulename), list))

    os.remove(tfpath)

if __name__ == '__main__':
    iplistreg()

