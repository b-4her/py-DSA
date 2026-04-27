def main():
    a = [0] * 4
    print(a)

    a.append(10)
    a.insert(0, 4)
    print(a)
    a.remove(10)
    # a.remove(3) # this crashes because 3 is not in the list
    print(a)
    a.pop() # removes last element
    print(a)

    del a  # removes the whole object!
    # print(a) # this will crash

if __name__ == "__main__":
    main()