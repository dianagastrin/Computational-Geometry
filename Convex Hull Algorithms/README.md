TBD

## Purpose
Find the convex hull of a set S.

## Complexity (for n vertics)
1. slow convex hull - O(n^3)
2. convex hull - O(nlogn)

## Result
<img src="https://i.imgur.com/i18lsgZ.png" width="250">

## Problems
1. Slow Convex Hull
    1. Very slow
    2. Not robust, small errors in the computations can make it fail in completely unexpected ways as shown here
    <img src="https://i.imgur.com/5BpsXDA.jpg" width="150">
2. Convex Hull
    1. If x-coordinate is identical, then sort also by y-coordinate (Lexicographic order)
    2. Colinear points (which do not make right/left turn), should be considered as left turn.

## Algorithm
TBD

