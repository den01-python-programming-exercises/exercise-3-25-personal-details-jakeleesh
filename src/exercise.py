def main():
    #write your code below this line
    sum = 0
    count = 0
    longest = 0
    long_name = ""
    while True:
        details = input()
        if (details != ""):
            details_split = details.split(",")
            sum += int(details_split[1])
            count += 1
            if (len(details_split[0]) > longest):
                longest = len(details_split[0])
                long_name = details_split[0]
        else:
            break
    avg = sum / count
    print("Longest name: " + long_name)
    print("Average of the birth years: " + str(avg))

if __name__ == '__main__':
    main()
