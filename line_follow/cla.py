



import argparse
parser = argparse.ArgumentParser(description="Line Following Robot Configuration")
parser.add_argument("-n","--name",metavar="name",type=str,help="Name of the robot",required=True)
args=parser.parse_args()
msg=f"Hello {args.name}, welcome to the Line Following Robot Program!"
print(msg)