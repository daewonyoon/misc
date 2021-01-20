from collections import Counter


def main():
    file_name = "개역한글판성경.txt"
    with open(file_name, "r", encoding="cp949") as f:
        txt = list(f.readlines())

    four_gram = []
    for line in txt:
        line = line.strip()
        line = line[line.find(" ") + 1 :]
        for i in range(len(line) - 3):
            ngram = line[i : i + 4]
            four_gram.append(ngram)

    c = Counter(four_gram)
    for gram, n in c.most_common(1000):
        print(f"{gram} : {n}")


if __name__ == "__main__":
    main()
