import std.stdio, std.conv, std.string, std.array, std.typecons, std.algorithm;
import util : submit;

/** 
 * Returns the value at given coordinates, will return -1 if invalid coordinates.
 */
auto getValueAt(int[][] map, int x, int y) {
  if (x < 0 ||  y < 0 || y > (map.length) - 1 || x > (map[y].length) - 1) {
    return -1;
  }
  return map[y][x];
}

auto isLowPoint(int[][] map, int x, int y, ulong height, ulong length) {
  auto current = map.getValueAt(x, y);
  // Square Right
  if (x < length - 1 && map.getValueAt(x + 1, y) <= current) 
    return false;
  // Square Above
  if (y > 0 && map.getValueAt(x, y - 1) <= current) 
    return false;
  // Square Below
  if (y < height - 1 && map.getValueAt(x, y + 1) <= current) 
    return false;
  // Square Left
  if (x > 0 && map.getValueAt(x - 1, y) <= current) 
    return false;
  return true;
}

void recursiveExplore(int [][] map, int x, int y, ref bool[string] points) {
  auto currentValue = map.getValueAt(x, y);
  if (currentValue == 9 || currentValue == -1 || format("%d,%d", x, y) in points)
    return;

  points[format("%d,%d", x, y)] = true;
  map.recursiveExplore(x + 1, y, points);
  map.recursiveExplore(x - 1, y, points);
  map.recursiveExplore(x, y + 1, points);
  map.recursiveExplore(x, y - 1, points);
}

auto exploreLowPointBasin(int[][] map, int x, int y) {
  bool[string] points;
  map.recursiveExplore(x, y, points);
  return points.length;
}

void main() {
  auto index = 0;
  auto fileLines = File("../input/input").byLine.array();
  auto height = fileLines.length, length = fileLines[0].length;
  auto riskLevel = 0;
  auto basins = new ulong[0];

  int[][] map = new int[][](height, length);
  // Map Building
  foreach (line; File("../input/input").byLine)
  {
    auto currentRow = new int[0];
    foreach (value; line)
      currentRow ~= to!int(to!string(value));
    map[index] = currentRow; index++;
  }

  // Part A
  for (int y = 0; y < height ; y++)
    for (int x = 0; x < length; x++)
      if (isLowPoint(map, x, y, height, length)) {
        riskLevel += map.getValueAt(x, y) + 1;
        // Part B
        basins ~= map.exploreLowPointBasin(x, y);
      }
  
  basins.sort!("a > b");

  writeln("Part A: ", riskLevel);
  writeln("Part B: ", basins[0] * basins[1] * basins[2]);
}
