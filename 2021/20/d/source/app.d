import std.stdio, std.string, std.format, std.conv;
import util;

struct Image
{
  bool[string] map;
  int minX;
  int minY;
  int maxX;
  int maxY;

  void runAlgo(string algo) {
    bool[string] newMap;
    foreach (y; minY .. maxY + 1)
    {
      foreach (x; minX .. maxX + 1)
      {
        auto cur = format("%d,%d", y, x);
        auto algoIndex = getAlgoIndexFor(x,y);
        if (algo[algoIndex] == '#') newMap[cur] = true;
      }
    }
    map = newMap;
  }

  private int getAlgoIndexFor(int xCur, int yCur) {
    auto mult = 1;
    auto sum = 0; 
    foreach_reverse (y; yCur-1 .. yCur+2)
    {
      foreach_reverse (x; xCur-1 .. xCur+2)
      {
        auto cur = format("%d,%d", y, x);
        if (cur in map) sum += mult;
        mult *= 2;
      }
    }
    return sum;
  }

  int getAmountOfLitPixels(int minX, int minY, int maxX, int maxY) {
    auto count = 0; 
    foreach (y; minY - 2 .. maxY + 3)
    {
      foreach (x; minX - 2 .. maxX + 3)
      {
        string cur = format("%d,%d", y, x);
        if (cur in map) count++;
      }
    }
    return count;
  }

  void print() {
    foreach (y; minY - 2 .. maxY + 3)
    {
      foreach (x; minX - 2 .. maxX + 3)
      {
        string cur = format("%d,%d", y, x);
        if (cur in map) write('#');
        else write('.');
      }
      write('\n');
    }
  }
}

int solve(File file, int steps) {
  auto imageAlgo = file.readln; file.readln;
  bool[string] map;
  int row = 0, minX = 0, minY = 0, maxX, maxY;
  foreach (line; file.byLine)
  {
    foreach (col, character; line)
    {
      if (character == '#') {
        map[format("%d,%d", row, col)] = true;
      }
      maxX = to!int(col);
    }
    row++;
    maxY = row;
  }
  auto stepMult = 3*steps;
  auto image = Image(map, minX - stepMult, minY - stepMult, maxX + stepMult, maxY + stepMult);
  foreach (step; 0 .. steps)
  {
    image.runAlgo(imageAlgo);
  }
  return image.getAmountOfLitPixels(minX - steps, minY - steps, maxX + steps, maxY + steps);

}

/** 
 * 
 * Params:
 *   file = Todays input file.
 * Returns: The answer to the given file.
 */
long partA(File file) {
  return solve(file, 2);
}

/** 
 * 
 * Params:
 *   file = Todays input file.
 * Returns: The answer to the given file.
 */
long partB(File file) {
  return solve(file, 50);
}

void main() {
  // Use these variables to decide what the runner needs to run.
	bool runReal = true;
	bool runB = true;

  runAnswers(&partA, &partB, runReal, runB);
}
