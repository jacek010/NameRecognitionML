import recognizer

test_names = ['Anna', 'Bob', 'Charlie', 'David', 'Adam', 'Janusz', 'Agata', 'Andrzej']


def main():
    for test_name in test_names:
        print(recognizer.check_gender(test_name))


if __name__ == '__main__':
    main()
