
from sys import argv

def main():

    if len(argv) != 4:
        raise Exception("Must have 4 args")
    else:
        
        in_file = open(argv[1])
        in_content = in_file.read()
        in_file.close()

        if in_content != "data3":
            raise Exception("Didn't get expected input data3, got " + in_content + " from " + argv[1])

     

        in_file = open(argv[2])
        in_content = in_file.read()
        in_file.close()

        if in_content != "data4":
            raise Exception("Didn't get expected input data4, got " + in_content + " from " + argv[2])

     
        
        out_file = open(argv[3], "w")
        out_file.write("data5")
        out_file.close()
    

if __name__ == "__main__":
    main()
     