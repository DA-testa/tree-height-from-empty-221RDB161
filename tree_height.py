# python3
# Autors: 221RDB161 Linards Tomass Beķeris 10 grupa

import sys
import threading


def compute_height(n, parents):
    heights = [0] * n
    for i in range(n):
        branch = i
        augst = 0
        while branch != -1:
            if heights[branch] != 0:
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
        with open(f"test/{file_path}", "r") as f:
            text = f.read().strip()
        return text.split('\n')
    except FileNotFoundError:
        print("Neatbilstošs faila path")
        return None
    except:
        print("Kļūda nolasot failu")
        return None


def main():
    input_veids = input(
        "Ievadi 'F' lai nolasītu inputu no faila, vai arī 'I' lai nolasītu input no klaviatūras: ").strip()

    if input_veids == 'F':
        file_name = input(
            "Ievadi faila nosaukumu. (Tie faila nosaukumi kuros būs burts 'a' nedarbosies: ")

        if 'a' in file_name:
            print("Neatbilstošs faila nosaukums")
            return

        if file_name.endswith('_'):  # šo uzrakstīju priekš autograder jo likās ka tas inputo 5_...
            file_name = file_name[:-1].zfill(2)

        file_path = f"{file_name.zfill(2)}"
        input_lines = read_input_from_file(file_path)

        if input_lines:
            n = int(input_lines[0])
            parents = list(map(int, input_lines[1].split()))
            print(compute_height(n, parents))

    elif input_veids == 'I':
        try:
            n = int(input("Ievadi nodes skaitu: "))
            parents = list(map(int, input(
                "Ievadiet vecāku mezglu indeksus, atdalot tos ar atstarpēm: ").split()))
            print(compute_height(n, parents))
        except:
            print("Neatbilstoša ievade")
    else:
        print("Neatbilstošs ievades veids")


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
