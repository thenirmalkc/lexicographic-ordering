
# lexicographic ordering
# Algorithm

# Find the largest x such that P[x]<P[x+1].
# (If there is no such x, P is the last permutation.)
# Find the largest y such that P[x]<P[y].
# Swap P[x] and P[y].
# Reverse P[x+1 .. n].


li = [1, 2, 3, 4, 5]
orders = []


# swaps elements in li
def swap(li, i, j):
  temp = li[i]
  li[i] = li[j]
  li[j] = temp


# calculates all possible order
def main():
  while True:
    orders.append(li.copy())

    # stores index of list
    lx = None
    ly = None

    for i in range(len(li) - 1):
      if li[i] < li[i + 1]:
        lx = i

    if lx == None:
      break

    for i in range(len(li)):
      if li[lx] < li[i]:
        ly = i

    swap(li, lx, ly)

    rev_li = li[lx + 1 : len(li)]
    rev_li.reverse()
    li[lx + 1 : len(li)] = rev_li


main()


# printing the orders
for i in range(len(orders)):
  print(orders[i])

print('\nTotal order:', len(orders))