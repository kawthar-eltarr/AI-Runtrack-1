# Job 23
print("This is job 23 :")
def draw_rectangle(width, height):
    filled_bar = '-'*width
    empty_bar = ' '*width
    print('|{}|'.format(filled_bar))
    for i in range(0, height):
        print('|{}|'.format(empty_bar))
    print('|{}|'.format(filled_bar))
draw_rectangle(10, 2)
