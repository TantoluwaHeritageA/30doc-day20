def convert_time(n):
    last_word = n[-1]
    dgt = ""
    if last_word == "s":
        for i in n:
            if i.isdigit():
                dgt = dgt + i
                count = int(dgt)
        while count > 0:
            print(f"> {count}s left")
            count -= 1
            if count == 0:
                print("*continuous indefinite beeping*")

    elif last_word == "m":
        for j in n:
            if j.isdigit():
                dgt = dgt + j
        print(dgt)
        min_to_sec = int(dgt) * 60
        print(min_to_sec, "seconds")
        while min_to_sec > 0:
            print(f"> {min_to_sec}s left")
            min_to_sec -= 1
            if min_to_sec == 0:
                print("*continuous indefinite beeping*")
    elif last_word == "h":
        for k in n:
            if k.isdigit():
                dgt = dgt + k
        print(dgt)
        hr_to_sec = int(dgt) * 3600
        print(hr_to_sec, "seconds")
        while hr_to_sec > 0:
            print(f"> {hr_to_sec}s left")
            hr_to_sec -= 1
            if hr_to_sec == 0:
                print("*continuous indefinite beeping*")


convert_time(input("Enter time in s, m or h: "))
