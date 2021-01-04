#!/usr/bin/python3 
import argparse
import functions

parser = argparse.ArgumentParser()
parser.add_argument('-v','--version',action='version',version='Lamppy v1')
parser.add_argument('-l', '--lampp', type=str,
                    choices=['start', 'stop', 'restart', 'repare'], help='manage the lampp service')
parser.add_argument('-m', '--mysql', type=str,
                    choices=['stop', 'enter'], help='manage the mysql service')
parser.add_argument('-ho', '--host', type=str, help='Host of mysql')
parser.add_argument('-u', '--user', type=str, help='mysql user')
parser.add_argument('-p', '--password', type=str, help='mysql user password')
args = parser.parse_args()

if args.lampp == 'start':
    functions.start_lampp()
elif args.lampp == 'stop':
    functions.stop_lampp()
elif args.lampp == 'restart':
    functions.restart_lampp()
elif args.lampp == 'repare':
    functions.repare_lampp()

if args.mysql == 'stop':
    functions.stop_mysql()
elif args.mysql == 'enter':
    if args.password:
        functions.enter_mysql(args.host, args.user, args.password)
    else:
        functions.enter_mysql(args.host, args.user)
