import std.stdio, std.conv, std.string, std.algorithm.mutation, std.typecons;

class Board
{
  ulong[int] coords;
  bool[ulong] markedValues;

  this(int[] numbers) {
    foreach (index, number; numbers)
    {
      coords[number] = index;
      markedValues[index] = false;
    }
  }

  bool markNumber(int number) {
    if (number in coords) {
      markedValues[coords[number]] = true;
    }

    int[][] possibilties = [
      [0,1,2,3,4],
      [5,6,7,8,9],
      [10,11,12,13,14],
      [15,16,17,18,19],
      [20,21,22,23,24],
      [0,5,10,15,20],
      [1,6,11,16,21],
      [2,7,12,17,22],
      [3,8,13,18,23],
      [4,9,14,19,24],
    ];
    foreach (possibilty; possibilties)
    {
      foreach (index, coord; possibilty)
      {
        if (!markedValues[coord]) {
          break;
        }
        if (index == 4) {
          return true;
        }
      }
    }

    return false;
  }

  int calculateUnusedValues() {
    auto sum = 0;
    
    foreach (number, coord; coords)
    {
      if (!markedValues[coord]) {
        sum += number;
      }
    }

    return sum;
  }

  void resetBoard()
  {
    foreach (ref markedValue; markedValues)
    {
      markedValue = false;
    }
  }
}


void main() {
  auto file = File("./../input/input");
  auto numbers = to!(int[])(file.readln.strip.split(','));

  auto count = 0;
  auto boards = new Board[0];
  auto values = new int[0];
  foreach (line; file.byLine)
  {
    if (count == 6) {
      boards ~= new Board(values);
      count = 0;
      values = new int[0];
    }
    
    values ~= to!(int[])(remove!(`a == ""`)(line.strip.split(' ')));
    count++;
  }

  outer: foreach (int number; numbers)
  {
    foreach (board; boards)
    {
      if (board.markNumber(number)) {
        writeln("Part A: ", board.calculateUnusedValues() * number);
        break outer;
      }
    }
  }
  int slowestFinalScore;
  ulong slowestIndex = 0;
  foreach (board; boards)
  {
    board.resetBoard();
    foreach (index, number; numbers)
    {
      if (board.markNumber(number)) {
        int finalScore = board.calculateUnusedValues() * number;
        if (slowestIndex < index || slowestIndex == -1) {
          slowestFinalScore = finalScore;
          slowestIndex = index;
        }
        break;
      }
    }
  }
  writeln("Part B: ", slowestFinalScore);
}
