import sys

if len(sys.argv) > 2:
    sys.exit("Too many arguments.")
elif len(sys.argv) <= 1:
    sys.exit("Few argument.")
elif not sys.argv[-1].strip().endswith('.py'):
    sys.exit("Not a python file")
else:
    file_name = sys.argv[1]
    try:
        count = 0
        with open(file_name, mode='r') as file:
            lines = file.readlines()
            
            
            for line in lines:
                
                if line.strip().startswith("#") or line.strip() == "":
                   continue
                else:
                    count +=1
                    
        print(f"{count} line(s) of code.")
    except FileNotFoundError:
        sys.exit("File Not Found.")
        