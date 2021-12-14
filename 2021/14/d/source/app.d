import std.stdio, std.file, std.string, std.array, std.conv, std.math, std.algorithm;
import util;

/** 
 * Native solution creating all polymers. 
 *
 * Params:
 *   file = Todays input files.
 * Returns: The answer to the given file.
 */
long partA(File file) {
  // Call Part A code here.
  auto parts = readText(file.name).split("\n\n");
  string polymer = parts[0];
  string min = to!string(polymer[0]);
  string max = to!string(polymer[1]);
  string[string] rules;
  long[string] histoElements;

  foreach (part; parts[1].split("\n"))
  {
    if (part == polymer) continue;
    auto ruleParts = part.split(" -> ");
    rules[ruleParts[0]] = ruleParts[1];
  }

  foreach (step; 1 .. 11)
  {
    histoElements.clear;
    string newPoly = "";
    for(uint i = 0; i < polymer.length; i++) {
      if (i == 0) {
        newPoly ~= polymer[0];
        continue;
      }
      string currentPolyPart = to!string(polymer[i - 1]) ~ to!string(polymer[i]);
      if (currentPolyPart in rules) {
        newPoly ~= rules[currentPolyPart];
        if (!(rules[currentPolyPart] in histoElements)) histoElements[rules[currentPolyPart]] = 1;
        else histoElements[rules[currentPolyPart]] += 1;
      }
      if (!(to!string(polymer[i]) in histoElements)) histoElements[to!string(polymer[i])] = 1;
      else histoElements[to!string(polymer[i])] += 1;
      newPoly ~= polymer[i];
    }

    polymer = newPoly; 
  }
  
  foreach (element; histoElements.byKeyValue)
  {
    if (element.value < histoElements[min]) {
      min = element.key;
    }
    if (element.value > histoElements[max]) {
      max = element.key;
    }
  }
  return histoElements[max] - histoElements[min];
}

/** 
 * 
 * Params:
 *   file = Todays input files.
 * Returns: The answer to the given file.
 */
long partB(File file) {
  // Call Part B code here.
  auto parts = readText(file.name).split("\n\n");
  string polymer = parts[0];
  string[string] rules;
  dchar min = polymer[0];
  dchar max = polymer[0];
  string[][string] expansionRules;
  long[string] pairs;

  foreach (part; parts[1].split("\n"))
  {
    if (part == polymer) continue;
    auto ruleParts = part.split(" -> ");
    rules[ruleParts[0]] = ruleParts[1];
  }
  foreach (rule; rules.byKeyValue)
  {
    expansionRules[rule.key] = [rule.key[0] ~ rule.value, rule.value ~ rule.key[1]];
  }

  for(uint i = 0; i < polymer.length; i++) {
    if (i == 0) {
      continue;
    }
    pairs[to!string(polymer[i - 1]) ~ to!string(polymer[i])] = 1;
  }

  foreach (step; 0 .. 40)
  {
    long[string] newPairs;
    foreach (pair; pairs.byKeyValue)
    {
      foreach (expansionRule; expansionRules[pair.key])
      {
        if (expansionRule in newPairs) newPairs[expansionRule] += pair.value; 
        else newPairs[expansionRule] = pair.value;
      }
    }
    pairs = newPairs;
  }

  long[dchar] counts;
  foreach (pair; pairs.byKeyValue)
  {
    if (pair.key[0] in counts) counts[pair.key[0]] += pair.value / 2;
    else counts[pair.key[0]] = pair.value / 2;
    if (pair.key[1] in counts) counts[pair.key[1]] += pair.value / 2;
    else counts[pair.key[1]] = pair.value / 2 ;
  }
  foreach (element; counts.byKeyValue)
  {
    if (element.value < counts[min]) {
      min = element.key;
    }
    if (element.value > counts[max]) {
      max = element.key;
    }
  }

  return counts[max] - counts[min];
}

void main() {
  // Use these variables to decide what the runner needs to run.
	bool runReal = true;
	bool runB = true;

  runAnswers(&partA, &partB, runReal, runB);
}
