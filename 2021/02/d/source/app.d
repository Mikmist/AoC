import std.stdio;
import util : submit;
import std.conv;
import std.uni;
import std.string;

void main() {
  auto horizontalPos = 0;
  auto verticalPos = 0;

  auto horizontalPosB = 0;
  auto aim = 0;
  auto depth = 0;

  foreach (line; File("../input/input").byLine) {
	auto lineParts = line.strip.split!isWhite;
	auto value = to!int(lineParts[1]);
	switch(lineParts[0]) {
		case "forward":
			horizontalPos += value;
			horizontalPosB += value;
			depth += (aim * value);
			break;
		case "down":
			verticalPos += value; 
			aim += value;
			break;
		case "up":
			verticalPos -= value;
			aim -= value;
			break;
		default: assert(0);
	}
  }
  writeln(verticalPos * horizontalPos);
  writeln(depth * horizontalPos);
  

  
//  writeln(submit(2, verticalPos * horizontalPos));
}
