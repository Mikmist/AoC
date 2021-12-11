import std.stdio, std.conv, std.typecons;
import util;

/** 
 * Returns the value at given coordinates, will return -1 if invalid coordinates.
 */
auto getValueAt(int[][] map, int x, int y) {
  if (x < 0 ||  y < 0 || y > (map.length) - 1 || x > (map[y].length) - 1) {
    return -1;
  }
  return map[y][x];
}

/** 
 * Returns the value at given coordinates, will not check if the coord exists.
 */
void setValueAt(int[][] map, int x, int y, int val) {
  map[y][x] = val;
}

void doFlashFor(int[][] map, int curX, int curY) {
  foreach (x; curX + -1 .. curX + 2)
    foreach (y; curY +-1 .. curY + 2)
    {
      if (x == curX && y == curY) continue;
      auto curValue = map.getValueAt(x, y);
      if (curValue != -1 && curValue != 0) {
        map.setValueAt(x, y, curValue + 1);
      } 
    }
}

int[][] buildMap(File file) {
  int[][] map = [];
  foreach (line; file.byLine)
  {
    int[] currentRow = [];
    foreach (value; line)
      currentRow ~= to!int(to!string(value));
    map ~= currentRow;
  }
  return map;
}

void print(int[][] map) {
  for (int y = 0; y < map.length; y++) {
    for(int x = 0; x < map[y].length; x++)
    {
      write(map.getValueAt(x, y), " ");
    }
    writeln();
  }
  writeln();
}

int runOctopusSimulator(File file, int steps) {
  auto map = buildMap(file);
  auto flashes = 0;
  
  foreach (step; 1 .. steps + 1)
  {
    // Gain Energy
    for (int y = 0; y < map.length; y++) {
      for(int x = 0; x < map[y].length; x++)
      {
        map.setValueAt(x, y, map.getValueAt(x, y) + 1);
      }
    }

    // Flash and reset until no more flashes.
    bool flashed;
    auto flashesThisRound = 0;
    do {
      flashed = false;
      for (int y = 0; y < map.length; y++) {
        for(int x = 0; x < map[y].length; x++)
        {
          if (map.getValueAt(x, y) > 9) {
            map.doFlashFor(x, y);
            map.setValueAt(x, y, 0);
            flashed = true;
            flashesThisRound++;
          }
        }
      }
    } while(flashed);
    if (flashesThisRound == map.length * map[0].length)
      return step;
    flashes += flashesThisRound;
  }

  return flashes;
}

/** 
 * 
 * Params:
 *   file = Todays input files.
 * Returns: The answer to the given file.
 */
int partA(File file) {
  // Call Part A code here.
  return runOctopusSimulator(file, 100);
}

/** 
 * 
 * Params:
 *   file = Todays input files.
 * Returns: The answer to the given file.
 */
int partB(File file) {
  // Call Part B code here.
  return runOctopusSimulator(file, 1000);
}

void main() {
  // Use these variables to decide what the runner needs to run.
	bool runReal = true;
	bool runB = true;

  runAnswers(&partA, &partB, runReal, runB);
}
