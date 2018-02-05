
from sys import argv

def main():

    if len(argv) != 3:
        raise Exception("Must have 3 args")
    else:
        
        
        out_file = open(argv[1], "w")
        out_file.write("data1")
        out_file.close()
    

        out_file = open(argv[2], "w")
        out_file.write("data2")
        out_file.close()
    

if __name__ == "__main__":
    main()
     