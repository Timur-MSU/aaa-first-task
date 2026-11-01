moscow = {201, 202, 203, 204}
kazan = {203, 204, 205, 206}


def main():
    print("Можно забрать в любом из двух городов:", moscow & kazan)
    print("Есть только в Москве:", moscow - kazan)
    print("Есть только в Казани:", kazan - moscow)
    print("Сколько разных товаров на обоих складах вместе:", len(moscow | kazan))


if __name__ == "__main__":
    main()
