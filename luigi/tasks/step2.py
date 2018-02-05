
from sys import argv

def main():

    if len(argv) != 3:
        raise Exception("Must have 3 args")
    else:
        
        in_file = open(argv[1])
        in_content = in_file.read()
        in_file.close()

        if in_content != "data2":
            raise Exception("Didn't get expected input data2, got " + in_content + " from " + argv[1])

     
        
        out_file = open(argv[2], "w")
        out_file.write("data4")
        out_file.close()
    

if __name__ == "__main__":
    main()
     