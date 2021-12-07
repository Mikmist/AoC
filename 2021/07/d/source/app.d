import std.stdio, std.conv, std.string;
import util : submit;
import std.algorithm.sorting;
import std.algorithm.iteration;
import std.math.algebraic;
import std.math.rounding;

auto calculateFuelA() {
  auto values = (to!(int[])(File("./../input/input").readln().split(',')).sort());
  auto fuel = 0; 
  foreach (value; values)
    fuel += abs(values[$/2] - value);
  return fuel;
}

auto calculateFuelB() {
  auto values = (to!(int[])(File("./../input/input").readln().split(',')));
  auto mean = to!int(values.mean());
  auto fuel = 0;
  foreach (value; values) {
    auto n = abs(mean - value);
    fuel += n*(n+1)/2;
  }
  return fuel;
}

void main() {
  writeln("Part A: ", calculateFuelA());
  writeln("Part B: ", calculateFuelB());
}
