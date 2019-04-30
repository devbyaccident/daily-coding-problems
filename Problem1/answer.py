import array as arr

# input = [3, 2, 1]
input = [1, 2, 3, 4, 5]

def multiplier(args):
    output = []
    num = 0
    for i in args:
        total = 0
        args.pop(num)
        for j in args:
            if total == 0:
                total = j
            else:
                total = int(total) * int(j)
        args.insert(num, i)        
        print(i, j, total, args, output)
        output.insert(num, total)
        num = num + 1
    print('output: ', output)
    return output
        


multiplier(input)