def main(a, b):
    print("on workflow dispatch")
    print("total nya : ", a+b)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2]) 