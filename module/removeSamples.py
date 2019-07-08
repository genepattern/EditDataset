import pandas as pd
from gp.data import write_gct
from gp.data import GCT
import getopt
import sys

def main(argv):
	inputFile = ''
	outputFile = ''
	removeFile = ''

	try:
		# print(argv)
		opts, args = getopt.getopt(argv, "i:r:o", ["gct.file=", "removelist=", "extension="])
	except getopt.GetoptError:
		print("removeSamples.py -i <gct file> -r <removelist> -o <output_filename>")
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print("removeSamples.py -i <gct file> -o <output_filename>")
			sys.exit(0)
		elif opt in ["-i", "--gct.file"]:
			inputFile = arg
		elif opt in ["-r", "--removelist"]:
			removeFile = arg
		elif opt in ["-o", "--extension"]:
			outputFile = arg
			if (not outputFile.lower().endswith(".gct")):
				outputFile = outputFile + ".gct"

	# temp redirect since this always generates an error message to stderr
	temp = sys.stderr
	sys.stderr = sys.stdout
	gct_df = GCT(inputFile)
	sys.stderr = temp

	print("Shape before removal:", gct_df.shape)
	err_count = 0
	with open(removeFile) as fp:
		# do stuff with fp
		for cnt, sampleName in enumerate(fp):
			try:
				gct_df.drop(sampleName.strip(), axis=1, inplace=True)
				print("removed " + sampleName)
			except KeyError:
				err_count = err_count + 1
				print("Sample " + sampleName + " not found in file.")

	print("Shape after removal:", gct_df.shape)

	write_gct(gct_df, outputFile)

	sys.exit(err_count)


if __name__ == "__main__":
	main(sys.argv[1:])


