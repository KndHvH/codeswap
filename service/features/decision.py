def decision() -> str:
    while True:
        try:
            print('a_ add | r_ read | e_ edit')
            choice = input("_").lower()

            if choice != 'a' and choice != 'r' and choice != 'q' and choice != 'e' and choice != 'd':
                raise ValueError

            return choice

        except ValueError:
            print("error!")