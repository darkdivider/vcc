import subprocess
import pdb

def main(): 
    script_path = 'gen_requests.py'
    arguments_file_path = 'arguments.txt'
    i=1
    with open(arguments_file_path, 'r') as file:
        for line in file:
            subprocess.run(['python', script_path] + line.split())

if __name__ == "__main__":  
    main()
