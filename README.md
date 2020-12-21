# Lexicographic Ordering

Suppose that P[1..n] is a permutation of 1 through n. We can construct the next permutation in lexicographic order by following these simple steps:

  - Find the largest x such that P[x]<P[x+1].
  - (If there is no such x, P is the last permutation.)
  - Find the largest y such that P[x]<P[y].
  - Swap P[x] and P[y].
  - Reverse P[x+1 .. n].
