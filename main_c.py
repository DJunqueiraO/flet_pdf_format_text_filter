import pdfplumber

from scripts.book import Book


def main():
    print("Informe o nome do arquivo a ser lido: ", end="")
    filename = input()
    print("Informe o tamanho da fonte: ", end="")
    size = float(input())
    print("Informe o nome da fonte: ", end="")
    fontname = input()
    with pdfplumber.open(f"in/{filename}.pdf") as file:
        print("Processando...")
        book = Book(file.pages)
        text = book.get_text(size, fontname)
    with open(f"out/{filename}.txt", "w") as file:
        print("Gravando...")
        file.write(text)


if __name__ == '__main__':
    main()