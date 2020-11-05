import wikipedia


def main():
    # "Monty" did not produce any error, so no error handling was added.
    page_name = "wikipedia"
    while page_name != "":
        page_name = input("What page do you want? ")
        page = wikipedia.page(page_name)
        print("Page name: {}, {}, URL: {}".format(page.title, page.summary, page.url))


main()
