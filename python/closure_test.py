def make_averager():
    series = []
    def averager(new_val):
        series.append(new_val)
        return sum(series)/len(series)
    return averager

def make_averager2():
    count = 0
    total = 0
    def averager(new_val):
        nonlocal count, total
        count += 1
        total += new_val
        return total /count
    return averager


if __name__ == "__main__":
    avg = make_averager()
    print(avg(10),avg(11),avg(12),)

    avg2 = make_averager2()
    print(avg(10),avg(11),avg(12),)