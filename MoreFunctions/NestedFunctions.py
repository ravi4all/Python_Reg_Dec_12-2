def parent():
    print("This is parent")

    def child():
        print("This is child")

        def grandChild():
            print("This is grandChild...")

        grandChild()

    child()

parent()
