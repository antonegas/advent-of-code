if __name__ == "__main__":
 import os
 __location__ = os.path.realpath(
 os.path.join(os.getcwd(), os.path.dirname(__file__)))
 with open(os.path.join(__location__, "input.txt"), "r") as f:
  data = f.read()
  grid = [list(x) for x in list(data.split("\n"))]
  part1 = 0
  part2 = 0
  removed = True
  first = True
  while removed:
   removed = False
   copied_grid = [x[:] for x in grid]
   for x in range(len(grid[0])):
    for y in range(len(grid)):
     if grid[y][x] == "@":
      count = 0
      part1 += first
      part2 += 1
      removed2 = True
      skip = False
      copied_grid[y][x] = "."
      for dx in [-1, 0, 1]:
       for dy in [-1, 0, 1]:
        if dx != 0 or dy != 0:
         if x + dx >= 0:
          if x + dx < len(grid[0]):
           if y + dy >= 0:
            if y + dy < len(grid):
             if grid[y + dy][x + dx] == "@":
              count += 1
              if not skip:
               if count >= 4:
                copied_grid[y][x] = "@"
                removed2 = False
                if first:
                 part1 -= 1
                part2 -= 1
                skip = True
      removed = removed or removed2
   first = False
   grid = copied_grid
  print("Part 1:", part1)
  print("Part 2:", part2)