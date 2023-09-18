#
def list_square():
    num_list = list()
    for i in range(4):
        score=float(input("number: "))
        num_list.append(score)
        i+=1
    print([score_item ** 2 for score_item in num_list])

list_square()
