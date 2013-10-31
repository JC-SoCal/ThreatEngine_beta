def main():
    print("This program extracts the first name of the students")
    print("in the text file.")

    infilename = raw_input("What file are the names in? ")
    outfileName = raw_input("What file should the usernames go in? ")

    infile = open(infilename, "r")
    outfile = open(outfileName, "w")
    

    for line in infile:
        items = line.split()
        username = (items[0]+items[1][:7]).lower()
        print username
        outfile.write(username+'\n')


    infile.close()


    print("Usernames have been written to", outfileName)

main()