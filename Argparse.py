# import the necessary packages
import argparse
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#instantiate the ArgumentParser object as ap
ap.add_argument("-n", "--name", required=True,
	help="name of the user")
#add our only argument, --name . We must specify both shorthand (-n) and longhand versions (--name)  where either flag could be used in the command line. This is a required argument as is noted by required=True
#help string gives additional info in terminal if u need
#A flag is another term for a command-line option (like -n or -h) 
args = vars(ap.parse_args())
#instructs Python and the argparse  library to parse the command line arguments
# display a friendly message to the user
print("Hi there {}, it's nice to meet you!".format(args["name"]))
