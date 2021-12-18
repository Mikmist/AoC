import std.stdio, std.format, std.string, std.conv, std.algorithm;
import util;

struct Number {
  int number;
  int length;
  
  static Number from(string a, ulong startingIndex) {
    string parsed = "";
    int lengthCnt = 0;
    foreach (character; a[startingIndex .. $])
    {
      if (character == ']' || character == ',') break;
      parsed ~= character;
      lengthCnt++;
    }
    return Number(to!int(parsed), lengthCnt);
  }

  string toString() const 
  {
    return to!string(number);
  }

  string buildSplitNumber() {
    return format("[%d,%d]", number/2, number/2 + number%2);
  }
}

long calculateMagnitude(string sum) {
  auto depth = 0;
  string partA = "";
  string partB = "";

  foreach (index, character; sum)
  {
    if (character == '[') depth++;
    if (character == ']') depth--;
    if (depth == 1 && character == ',') { 
      return 3*calculateMagnitude(sum[1 .. index]) + 2*calculateMagnitude(sum[index+1 .. $-1]);
    }
  }
  return to!int(sum);
}

auto addPair(string a, string b) {
  return format("[%s,%s]", a, b);
}

string replaceStringAtIndex(string a, string newValue, ulong index, ulong removeExtra = 0) {
  return a[0 .. index] ~ newValue ~ a[index + 1 + removeExtra .. $];
}

auto reducePair(string a) {
  bool hasReduced = true;
  while (hasReduced) {
    hasReduced = false;
    auto hasExploded = false;
    auto depth = 0;
    foreach (index, character; a)
    {
      if (character == '[') depth++;
      if (character == ']') depth--;
      if (depth > 4) {
        auto leftValueIncrement = Number.from(a, index+1);
        auto rightValueIncrement = Number.from(a, index+2 + leftValueIncrement.length);
        a = a[0 .. index] ~ "0" ~ a[index + 3 + leftValueIncrement.length + rightValueIncrement.length .. $];
        foreach (curIdx; index + 1 .. a.length)
          if (a[curIdx] != '[' && a[curIdx] != ']' && a[curIdx] != ',') {
            auto curNum = Number.from(a, curIdx);
            a = replaceStringAtIndex(
              a, format("%d", Number.from(a, curIdx).number + rightValueIncrement.number), curIdx, (curNum.length) - 1);
            break;
          }
        outer: foreach_reverse (curIdx; 0 .. index)
          if (a[curIdx] != '[' && a[curIdx] != ']' && a[curIdx] != ',') {
            for (ulong i = curIdx; i > 0; i--) {
              if (a[i] == '[' || a[i] == ']' || a[i] == ',') {
                auto curNum = Number.from(a, i+1);
                a = replaceStringAtIndex(
                  a, format("%d", curNum.number + 
                  leftValueIncrement.number),i+1, (curNum.length) - 1);
                break outer;
              }
            }
          }
        hasExploded = true;
        hasReduced = true;
        break;
      }
    }
    if (!hasExploded) {
      foreach (index; 0 .. a.length)
      {
        if (a[index] != '[' && a[index] != ']' && a[index] != ',') {
          auto number = Number.from(a, index);
          if (number.number > 9) {
            a = replaceStringAtIndex(a, number.buildSplitNumber, index, (number.length) - 1);
            hasReduced = true;
            break;
          }
        }
      }
    }
  }

  return a;
}

/** 
 * 
 * Params:
 *   file = Todays input files.
 * Returns: The answer to the given file.
 */
long partA(File file) {
  // Call Part A code here.
  string sum = file.readln.strip;
  foreach (line; file.byLine)
  {
    sum = sum.addPair(to!string(line));
    sum = sum.reducePair;
  }
  return calculateMagnitude(sum);
}

/** 
 * 
 * Params:
 *   file = Todays input files.
 * Returns: The answer to the given file.
 */
long partB(File file) {
  // Call Part B code here.
  string[] lines = [];
  foreach (line; file.byLine)
    lines ~= to!string(line);
  long sum = 0;
  foreach (a; lines)
    foreach(b; lines) {
      sum = max(sum, calculateMagnitude(a.addPair(b).reducePair));
    }
  return sum;
}

void main() {
  // Use these variables to decide what the runner needs to run.
	bool runReal = true;
	bool runB = true;

  runAnswers(&partA, &partB, runReal, runB);
}
