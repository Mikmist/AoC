import std.stdio, std.string, std.conv, std.format;
import util;

class Player {
  int number;
  int position;
  int score;
  int winningScore;

  this(char[] line, int winningScore) {
    auto parts = line.split(' ');
    score = 0;
    position = to!int(parts[4]);
    number = to!int(parts[1]);
    this.winningScore = winningScore;
  }

  bool playRound(Dice dice) {
    auto increase = 0;
    for(int i = 0; i < 3; i++) {
      auto roll = dice.roll;
      increase += roll;
    }
    
    position += ((increase - 1) % 10) + 1;
    if (position > 10) position -= 10;
    score += position;
    return score >= winningScore;
  }

  override string toString() const
  {
    return format("Player(number: %d, position: %d, score: %d)", number, position, score);
  }
}

class Dice {
  int currentValue;
  int rolls;

  this() {
    currentValue = 1;
    rolls = 0;
  }

  int roll() {
    auto value = currentValue;
    currentValue++; 
    rolls++; 
    if (currentValue > 100) currentValue = 1;
    return value;
  }
}

/** 
 * 
 * Params:
 *   file = Todays input file.
 * Returns: The answer to the given file.
 */
long partA(File file) {
  Player[] players = [];
  Dice dice = new Dice();
  foreach (line; file.byLine)
    players ~= new Player(line, 1000);
  
  while (true) {
    foreach (i, Player player; players)
    {
      if (player.playRound(dice))
        return players[((i+1)%2)].score * dice.rolls;
    }
  }

}

/** 
 * 
 * Params:
 *   file = Todays input file.
 * Returns: The answer to the given file.
 */
long partB(File file) {
  return 0;
}

void main() {
  // Use these variables to decide what the runner needs to run.
	bool runReal = true;
	bool runB = false;

  runAnswers(&partA, &partB, runReal, runB);
}