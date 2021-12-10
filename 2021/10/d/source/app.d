import std.stdio, std.algorithm.mutation, std.algorithm.sorting, std.string, std.conv;
import util : submit;

void main() {
  auto file = File("../input/input");
  char[char] mapping = ['(': ')', '{': '}', '[': ']', '<': '>'];
  int[char] scores = [')': 3, ']': 57, '}': 1197, '>': 25_137];
  int[char] scoreMappingsB = [')': 1, ']': 2, '}': 3, '>': 4];
  auto score = 0; ulong[] scoresB = [];

  foreach (line; file.byLine)
  {
    long scoreB = 0;
    char[] needsClosing = [];
    char error = '-';
    foreach (character; line)
    {
      if (character in mapping) {
        needsClosing ~= character;
      } else {
        if (character == mapping[needsClosing[$ - 1]]) {
          needsClosing = needsClosing.remove((needsClosing.length) - 1);
        } else {
          error = character;
          break;
        }
      }
    }
    if (error == '-') {
      foreach_reverse (character; needsClosing)
        scoreB = (scoreB * 5) + scoreMappingsB[mapping[character]];
      scoresB ~= scoreB;
    }
    score += (error in scores) ? scores[error] : 0;
  }
  writeln("Part A: ", score);
  writeln("Part B: ", scoresB.sort[$/2]);
}
