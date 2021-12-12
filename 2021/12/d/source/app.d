import std.stdio, std.string, std.conv, std.ascii;
import util;

struct Map
{
  string[][string] map;

  this(File file) {
    foreach (line; file.byLine)
    {
      auto caves = line.split('-');
      if (caves[0] in map) {
        auto current =  caves[1];
        bool isIn = false;
        foreach(path; map[caves[0]]) {
          if (path == current) isIn = true;
        }
        if (!isIn) map[to!string(caves[0])] ~= to!string(caves[1]);
      } else {
        map[to!string(caves[0])] ~= to!string(caves[1]);
      }
      if (caves[1] in map) {
        auto current =  caves[1];
        bool isIn = false;
        foreach(path; map[caves[1]]) {
          if (path == current) isIn = true;
        }
        if (!isIn) map[to!string(caves[1])] ~= to!string(caves[0]);
      } else {
        map[to!string(caves[1])] ~= to!string(caves[0]);
      }
    }
  }
}

int explorePathsA(Map* map, string current, string[] visited) {
  if (current == "end") {
    return 1;
  }

  foreach (visitor; visited)
  {
    if (toUpper(current) != current && current == visitor) {
      return 0;
    } 
  }
  
  auto total = 0;
  visited ~= current;
  foreach (possiblePath; map.map[current])
  {
    total += map.explorePathsA(possiblePath, visited);
  }
  return total;
}

int explorePathsB(Map* map, string current, int[string] visited, bool smallDoublePassed = false) {
  if (current == "end") {
    return 1;
  }

  if (
    ("start" in visited && current == "start") ||
    (toUpper(current) != current && current in visited && visited[current] == 1 && smallDoublePassed)
  ) {
    return 0;
  }

  if (current in visited) {
    visited[current] += 1;
    if (visited[current] > 1 && toUpper(current) != current) smallDoublePassed = true;
    if (visited[current] > 2 && toUpper(current) != current) return 0;
  }
  else visited[current] = 1;

  auto total = 0;
  // writeln(visited, map.map[current]);
  foreach (possiblePath; map.map[current])
  {
    // writeln(possiblePath);
    total += map.explorePathsB(possiblePath, visited.dup, smallDoublePassed);
  }
  return total;
}


/** 
 * 
 * Params:
 *   file = Todays input files.
 * Returns: The answer to the given file.
 */
int partA(File file) {
  // Call Part A code here.
  auto map = new Map(file);
  return map.explorePathsA("start", []);
}

/** 
 * 
 * Params:
 *   file = Todays input files.
 * Returns: The answer to the given file.
 */
int partB(File file) {
  // Call Part B code here.
  auto map = new Map(file);
  int[string] visitors;
  return map.explorePathsB("start", visitors);
}

void main() {
  // Use these variables to decide what the runner needs to run.
	bool runReal = true;
	bool runB = true;

  runAnswers(&partA, &partB, runReal, runB);
}
