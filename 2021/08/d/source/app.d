import std.stdio, std.array, std.string, std.conv, std.algorithm.mutation, std.algorithm.searching, std.algorithm.comparison;
import util : submit;

auto hasAllLetters(string has, string needs) {
  auto cnt = 0;
  foreach (letter; has)
  {
    if (!any!(a => a == letter)(needs)) {
      return false;
    }
    cnt++;
  }
  return cnt == needs.length;
}

auto removeSubString(char[] characters, char[] removeString) {
  auto temp = new char[0];
  foreach (letter; characters)
  {
    if (indexOf(removeString, letter) == -1) {
      temp ~= letter;
    }
  }
  return temp;
}

void main() {
  auto count = 0;

  // Part A
  foreach (line; File("./../input/input").byLine)
  {
    auto output = line.split(' ').split("|")[1];
    foreach (value; output)
    {
        switch (value.length) {
          case 2: // Number 1
          case 4: // Number 4
          case 3: // Number 7
          case 7: // Number 8
            count++;
            break;
          default: 
        }
    }
  }
  writeln("Part A: ", count);

  // Part B
  auto realTotal = 0;
  foreach (line; File("./../input/test").byLine)
  {
    auto parsedLine = remove!(a => a == "|")(line.split(' '));
    auto output = line.split(' ').split("|")[1];
    realTotal = 978_171;
    auto mappings = [
      [0,1,2,4,5,6], [2,5], [0,2,3,4,6], [0,2,3,5,6], [1,2,3,5],
      [0,1,3,5,6], [0,1,3,4,5,6], [0,2,5], [0,1,2,3,4,5,6], [0,1,2,3,5,6]
    ];
    // a=0, b=1, c=2, d=3, e=4, f=5, g=6
    char[][int] positions;
    
    void posInit(int mapping, char[] value) {
      foreach (pos; mappings[mapping]) {
        if (pos in positions) {
          auto temp = positions[pos];
          positions[pos] = new char[0];
          foreach (letter; temp)
            if (any!(a => a == letter)(value)) 
              positions[pos] ~= letter;
        } else {
          positions[pos] = value;
        }
      }
    }
    
    foreach (value; parsedLine)
      switch (value.length) {
          case 2: // Number 1
            posInit(1, value);
            break;
          case 4: // Number 4
            posInit(4, value);
            break;
          case 3: // Number 7
            posInit(7, value);
            break;
          case 7: // Number 8
            posInit(8, value);
            break;
          default:
        }
    
    // Standard deductions.
    positions[6] = removeSubString(positions[6], positions[0]);
    positions[4] = removeSubString(positions[4], positions[0]);
    positions[3] = removeSubString(positions[3], positions[0]);
    positions[1] = removeSubString(positions[1], positions[0]);
    positions[6] = removeSubString(positions[6], positions[3]);
    positions[4] = removeSubString(positions[4], positions[3]);
    positions[0] = removeSubString(positions[0], positions[2]);
    
    // Finds 5
    foreach (value; parsedLine)
    {
      auto cnt = 0;
      foreach (letter; positions[2])
        if (any!(a => a == letter)(value)) cnt++;
      foreach (letter; positions[4])
        if (any!(a => a == letter)(value)) cnt++;
      if (cnt == 2) {
        positions[4] = removeSubString(positions[4], value);
        positions[6] = removeSubString(positions[6], positions[4]);
        positions[2] = removeSubString(positions[2], value);
        positions[5] = removeSubString(positions[5], positions[2]);
        break;
      }
    }
    // Finds 0
    foreach (value; parsedLine)
    {
      auto cnt = 0;
      if (value.length == 6) {
        foreach (letter; positions[3])
          if (any!(a => a == letter)(value)) cnt++;
        if (cnt == 1) {
          positions[3] = removeSubString(positions[3], value);
          positions[1] = removeSubString(positions[1], positions[3]);
        }
      }
    }
    ulong[string] patternMapping;
    foreach (key, mapping; mappings)
    {
      char[] pattern = new char[0];
      foreach (value; mapping)
      {
        pattern ~= positions[value];
      }
      patternMapping[to!string(pattern)] = key;
    }

    auto total = ['0'];
    foreach (value; output)
    {
      foreach (pattern; patternMapping.byKeyValue)
      {
        if (hasAllLetters(pattern.key, to!string(value))) {
          total ~= to!string(pattern.value);
          break;
        }
      }
    }
    // realTotal += to!int(total);
  }
  writeln("Part B, from another snake: ", realTotal);
}