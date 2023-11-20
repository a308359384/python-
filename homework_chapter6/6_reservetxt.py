with open('file1.txt', 'r', encoding='utf-8') as file1, open('file2.txt', 'w', encoding='utf-8') as file2:
    for line in file1:
        reversed_line = line.strip()[::-1]
        file2.write(reversed_line + '\n')