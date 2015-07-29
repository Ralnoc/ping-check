#!/usr/bin/python2

import argparse
import ping
import socket
import time
import datetime

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', nargs='+', type=str,
                        help='Servers to ping')
    parser.add_argument('-n', '--dry-run', action='store_true', help='Dry Run. (Send no metrics to Graphite)')
    parser.add_argument('-d', '--graphite-server', type=str, help='Graphite Server')
    parser.add_argument('-p', '--graphite-port', type=int, help='Graphite Port')
    parser.add_argument('-x', '--graphite-prefix', type=str, 
                        default="internet.connection.ping.", help='Graphite Metric Prefix')

    return parser.parse_args()

def submit_graphite(metric, value, server, port):
    graphite_socket = {'socket': socket.socket( socket.AF_INET, socket.SOCK_STREAM ), 'host': server, 'port': port}
    time_epoch = int(time.time())
    try:
        graphite_socket['socket'].connect( ( graphite_socket['host'], int( graphite_socket['port'] ) ) )
    except socket.error as serr:
        print 'Connection to Graphite server failed: ' + str(serr)

    metric_string = "%s %.2f %d" % ( metric, value, time_epoch )
    try:
        #print 'Metric String: %s' % (metric_string,)
        graphite_socket['socket'].send( "%s\n" % metric_string )
    except socket.error:
        pass


if __name__ == '__main__':
    args = get_args()
    time_done = datetime.datetime.now()
    while True:
        current_time = datetime.datetime.now()
        if (current_time - time_done).seconds >= 60:
            for idx in range(len(args.server)):
                try:
                    ping_destination = ping.detailed_ping(args.server[idx], 5, 5, 1024)
                    for k, v in ping_destination.iteritems():
                        submit_graphite(args.graphite_prefix + args.server[idx].replace('.', '_') + '.' + k, v, args.graphite_server, args.graphite_port)
                except TypeError:
                    pass
                finally:
                    time_done = datetime.datetime.now()
