# python3
# 221RDB161 Linards Tomass Beķeris 10 grupa

import sys
import threading

def compute_height(n, parents):

    heights = [0] * n

    for i in range(n):

        branch = i 
        augst = 0 

        while branch != -1:

            if heights[branch] !=0:

                augst += heights[branch]
                break

            augst += 1
            branch = parents[branch]
            j = i 

        while j != -1:

            if heights[j] != 0:
                break

            heights[j] = augst
            augst -= 1
            j = parents[j]

    return max(heights)

def read_input_from_file(file_path):
    try:
        with open(file_path, "r") as f:
            text = f.read().strip()
        return text.split('\n')

    except FileNotFoundError:
        print("Neatbilstošs faila path")
        return None
    
    except:
        print("Kļūda nolasot failu")
        return None

def main():
    input_veids = input("Ievadi 'F' lai nolasītu inputu no faila, vai arī 'I' lai nolasītu input no klaviatūras: ").strip()
    
    if input_veids == 'F':
        file_name = input("Ievadi faila nosaukumu. (Tie faila nosaukumi kuros būs burts 'a' nedarbosies: ")
        if 'a' in file_name:
            print("Neatbilstošs faila nosaukums")
            return

        file_path = f"/workspaces/tree-height-from-empty-221RDB161/test/{file_name}"
        input_lines = read_input_from_file(file_path)
        
        if input_lines:
            n = int(input_lines[0])
            parents = list(map(int, input_lines[1].split()))
            print(compute_height(n, parents))
        
    elif input_veids == 'I':

        try:
            n = int(input("Ievadi nodes skaitu: "))
            parents = list(map(int, input("Ievadiet vecāku mezglu indeksus, atdalot tos ar atstarpēm: ").split()))
            print(compute_height(n, parents)) 

        except:
            print("Neatbilstoša ievade")
    else:
        print("Neatbilstošs ievades veids")

    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
