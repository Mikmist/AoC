import std.stdio, std.conv, std.string;
import util : submit;

auto calculateFishies(int days) {
  auto file = File("./../input/input");
  long count = 0;
  auto fishActions = new long[days];
  // Init
  foreach (line; file.readln().split(',')) 
  {
    fishActions[to!long(line)] += 1;
    count++;
  }
  foreach (i, day; fishActions)
  {
    if (i+7 < days) fishActions[i + 7] += day;
    if (i+9 < days) fishActions[i + 9] += day;
    count += day;
  }
  return count;
}

void main() {
  writeln("Part A: ", calculateFishies(80));
  writeln("Part B: ", calculateFishies(256));
}
