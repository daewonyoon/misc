import random



def main():
    file_name = "개역한글판성경.txt"
    with open(file_name, "r", encoding="cp949") as f:
        bible_list = [ line for line in f.readlines() ]
    
    r = random.choice(bible_list)
    print(r)

if __name__ == "__main__":
    main()    
