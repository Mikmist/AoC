import std.stdio, std.format, std.string, std.conv;
import util;

void print(int[string] map, int maxX, int maxY) {
  for(int y = 0; y < maxY; y++) {
    for(int x = 0; x < maxX; x++) {
      if (format("%d,%d", y, x) in map) {
        if (map[format("%d,%d", y, x)] == 0) write(">");
        if (map[format("%d,%d", y, x)] == 1) write("v");
      }
      else write(".");
    }
    writeln();
  }
}

string stringifyCoords(int y, int x) {
  return format("%d,%d", y, x);
}

int solveCucumbers(File file) {
  int[string] map;
  int maxY = 0, maxX = 0;
  bool movement = false;
  foreach (line; file.byLine)
  {
    foreach (x, chararcter; line)
    {
      if (chararcter == '>') map[format("%d,%d", maxY, x)] = 0;
      if (chararcter == 'v') map[format("%d,%d", maxY, x)] = 1;
      maxX=to!int(x) + 1;
    }
    maxY++;
  }
  
  int step = 0;
  while (true)
  {
    step++;
    movement = false;
    // East
    auto newMap = map.dup;
    foreach (cucumber; map.byKeyValue)
    {
      if (cucumber.value == 0) {
        auto coords = to!(int[])(cucumber.key.split(","));
        int newX = coords[1] + 1 == maxX ? 0 : coords[1] + 1;
        if (stringifyCoords(coords[0], newX) !in map) {
          movement = true;
          newMap.remove(cucumber.key);
          newMap[stringifyCoords(coords[0], newX)] = 0;
        }
      }
    }

    // South
    map = newMap;
    newMap = map.dup;
    foreach (cucumber; map.byKeyValue)
    {
      if (cucumber.value == 1) {
        auto coords = to!(int[])(cucumber.key.split(","));
        int newY = coords[0] + 1 == maxY ? 0 : coords[0] + 1;
        if (stringifyCoords(newY, coords[1]) !in map) {
          movement = true;
          newMap.remove(cucumber.key);
          newMap[stringifyCoords(newY, coords[1])] = 1;
        }
      }
    }
    map = newMap;
    // map.print(maxX, maxY);
    if (!movement) break;
  }
  return step;
}

/** 
 * 
 * Params:
 *   file = Todays input file.
 * Returns: The answer to the given file.
 */
long partA(File file) {
  // Call Part A code here.
  
  return solveCucumbers(file);
}

/** 
 * 
 * Params:
 *   file = Todays input file.
 * Returns: The answer to the given file.
 */
long partB(File file) {
  // Call Part B code here.
  foreach (line; file.byLine)
  {
    
  }
  return 0;
}

void main() {
  // Use these variables to decide what the runner needs to run.
	bool runReal = true;
	bool runB = true;

  runAnswers(&partA, &partB, runReal, runB);
}
