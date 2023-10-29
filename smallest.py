# python for everybody, loop patter, sayfa: 63
smallest = None
print('Before:', smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
  if smallest is None or itervar < smallest:
    smallest = itervar
  print('Loop:', itervar, smallest)
print('Smallest:', smallest)

  # olurda None'dan başlatmayıp bir değer vermişsem ya da 
  # listenin ilk öğesinden başlatmışsam 'or' dan sonrasına bakılır.
  # misal list = [3, 41, 12, 9, 74, 15],  list[0] gibi
