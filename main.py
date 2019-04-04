from mybox import MyBox
from myboxiterator import MyBoxIterator

box=MyBox()
box.add(1)
box.add('2')
box.add(3.5)
box.add('box')
box.add(6)
box.add('resolved')
box.remove('2')
if ('first' in box) and (len(box)>0):
    box.remove('first')
for i in box:
    print(i)
