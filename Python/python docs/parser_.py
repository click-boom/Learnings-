import argparse
parser=argparse.ArgumentParser(description='Program to add numbers via CLI')

parser.add_argument('add', nargs='*', metavar='num',type=int, help='numbers separated by space will be added')  #default type= str

args=parser.parse_args()  # reads the given arguments from CLI

if len(args.add)!=0:
    print(sum(args.add))


