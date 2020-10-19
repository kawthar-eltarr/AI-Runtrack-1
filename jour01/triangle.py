# Job 29
print("This is job 29 :")
def draw_triangle(height):
    for i in range(0, height-1):
        print(' '*(height-i)+'/'+2*i*' '+'\\')
    print(' /'+'_'*(2*height-2)+'\\')
draw_triangle(8)

