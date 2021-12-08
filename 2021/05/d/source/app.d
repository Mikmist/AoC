import std.stdio, std.string, std.conv;
import util : submit;

class Point {
  int x;
  int y;
  this(char[][] parts) {
    x = to!int(parts[0]);
    y = to!int(parts[1]);
  }
}

class Line {
  Point a;
  Point b;
  bool vertical;
  bool horizontal;

  this(char[] unparsedLine) {
    auto parts = unparsedLine.strip().split(' ');
    a = new Point(parts[0].split(','));
    b = new Point(parts[2].split(','));
    vertical = a.x == b.x;
    horizontal = a.y == b.y;
  }

  auto getHorOrVerPoints(bool partB = false) {
    string[] points = new string[0];
    if (vertical || horizontal) {
      if (a.x < b.x) {
        foreach (x; a.x .. b.x + 1)
          points ~= format("%d,%d", x, a.y); 

      } else if (a.x > b.x) {
        foreach (x; b.x .. a.x + 1)
          points ~= format("%d,%d", x, a.y); 
      } else {
        if (a.y < b.y) {
          foreach (y; a.y .. b.y + 1)
            points ~= format("%d,%d", a.x, y); 
        } else {
          foreach (y; b.y .. a.y + 1)
            points ~= format("%d,%d", a.x, y); 
        }
      }
    } else if (partB) {
      if (a.x < b.x) {
        foreach (x; a.x .. b.x + 1)
          points ~= format("%d,%d", x, a.y + (x - a.x) * (a.y < b.y ? 1 : -1)); 
      } else {
        foreach (x; b.x .. a.x + 1)
          points ~= format("%d,%d", x, b.y + (x - b.x) * (a.y < b.y ? -1 : 1)); 
      }
    }
    return points;
  }
}

void main() {
  auto file = File("./../input/input");
  auto lines = new Line[0];
  int[string] gridPointsA, gridPointsB;
  auto countA = 0, countB = 0;

  foreach (line; file.byLine)
  {
    auto parsedLine = new Line(line);
    lines ~= parsedLine;
    foreach (pointString; parsedLine.getHorOrVerPoints)
    {
      gridPointsA[pointString] += 1;
      if (gridPointsA[pointString] == 2) {
        countA++;
      }
    }
    foreach (pointString; parsedLine.getHorOrVerPoints(true))
    {
      gridPointsB[pointString] += 1;
      if (gridPointsB[pointString] == 2) {
        countB++;
      }
    }
  }
  writeln("Part A: ", countA);
  writeln("Part B: ", countB);
}
