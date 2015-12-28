#
#
#
#
#
import argparse

def parse_everything():
	parser = argparse.ArgumentParser()
	parser.add_argument("val", type=str, action="store", nargs="+" )
	args = parser.parse_args()
	
	print args.val

	

if __name__=="__main__":
	parse_everything()
