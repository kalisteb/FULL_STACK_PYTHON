
from turtle import *
color('blue', 'green')
begin_fill()
while True:
    forward(200)
    right(220)
    if abs(pos()) < 1:
        break

end_fill()
done()

