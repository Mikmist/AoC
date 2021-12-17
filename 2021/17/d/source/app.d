import std.stdio, std.string, std.conv, std.algorithm, std.math.algebraic;
import util;

bool inAreaOnAxis(int xOrY, int[] range) {
  return xOrY <= maxElement(range) && xOrY >= minElement(range);
}

int[] calculateHit(int xV, int yV, int[][] area) {
  auto curX = 0, curY = 0, step = 0, maxHeight = 0;
  while((xV != 0 || inAreaOnAxis(curX, area[0])) && curY >= minElement(area[1])) {
    // writeln(format("xV: %d, yV: %d, curX: %d, curY: %d (%d, %d)", xV, yV, curX, curY, inAreaOnAxis(curX, area[0]), 
    //   inAreaOnAxis(curY, area[1])));
    if (inAreaOnAxis(curX, area[0]) && inAreaOnAxis(curY, area[1])) {
      return [maxHeight, true];
    }
    curX += xV;
    curY += yV;
    step++;
    yV--;
    if (curY > maxHeight) maxHeight = curY;
    if (xV > 0) xV--;
    if (xV < 0) xV++;
  }
  return [0, false];
}

/** 
 * 
 * Params:
 *   file = Todays input files.
 * Returns: The answer to the given file.
 */
long partA(File file) {
  // Call Part A code here.
  auto line = file.readln[13 .. $].split(", ");
  auto x = to!(int[])(line[0].split("=")[1].split(".."));
  auto y = to!(int[])(line[1].split("=")[1].split(".."));
  auto area = [x, y];
  //max(abs(0 - y[1]), abs(0 - y[0]))
  int curX = 0, curY = 0;
  auto highest = [0,0,0];
  while(curX < x[1]) {
    while(curY < 1000) {
      auto res = calculateHit(curX, curY, area);
      if (res[1] && curY > highest[1]) {
        highest = [curX, curY, res[0]];
      }
      curY++;
    }
    curY = 0;
    curX++;
  }
  return highest[2];
}

/** 
 * 
 * Params:
 *   file = Todays input files.
 * Returns: The answer to the given file.
 */
long partB(File file) {
  // Call Part A code here.
  auto line = file.readln[13 .. $].split(", ");
  auto x = to!(int[])(line[0].split("=")[1].split(".."));
  auto y = to!(int[])(line[1].split("=")[1].split(".."));
  auto area = [x, y];
  int curX = 0, curY, count = 0;
  while(curX <= x[1]) {
    curY = minElement(area[1]);
    while(curY < 1000) {
      if (calculateHit(curX, curY, area)[1]) {
        count++;
      }
      curY++;
    }
    curX++;
  }
  return count;
}

void main() {
  // Use these variables to decide what the runner needs to run.
	bool runReal = true;
	bool runB = true;

  runAnswers(&partA, &partB, runReal, runB);
}
