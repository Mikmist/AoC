import std.algorithm.mutation;
import std.stdio;
import util : submit;
import std.string;
import std.typecons;
import std.conv;

Tuple!(int, int) printAndCalculateDecimalValue(int[] counts, int amount) {
	int value = 0;
	int inverseValue = 0;
	int mult = 1;

	foreach (countNumber; counts) {
		if (countNumber > amount/2) {
			value += mult;
		} else {
			inverseValue += mult;
		}	
		mult *= 2;
	}
	Tuple!(int,int) values = [value, inverseValue];
	return values;
}

int calculateDecimalValueFromString(string binary) {
	auto value = 0;
	auto mult = 1;
	foreach_reverse(digit; binary) {
		if (digit == '1') {
			value += mult;
		}
		mult *= 2;
	}
	return value;
}

void main() {
	auto file = File("./../input/input");
	auto counts = new int[12];
	auto count = 0;
	auto remainingIndecies = new int[0];
	auto lines = new string[0];
	auto linesInverted = new string[0];

	foreach (line; file.byLine) {
		// Part A
		auto index = 1;
		foreach(number; line) {
			if (number == '1') {
				counts[$ - index] += 1;
			}
			index++;
		}
		
		// Part B
		remainingIndecies ~= count;
	    	lines ~= to!string(line);	
	    	linesInverted ~= to!string(line);	

		count++;
	}
	writeln(lines);
	
	auto finished = false;
	auto currentBitIndex = 0;
	do {
		auto amountOfOnes = 0;
		char removeBit;
		
		// oxygen generator
		if (lines.length > 1) {
			foreach (line; lines) {
				if (line[currentBitIndex] == '1') {
					amountOfOnes++;
				}
			}
			removeBit = lines.length - amountOfOnes > amountOfOnes ? '1' : '0';
			lines = remove!(a => a[currentBitIndex] == removeBit)(lines);
		}
		
		// CO2 scrubber rating
		if (linesInverted.length > 1) {
			amountOfOnes = 0;
			foreach (line; linesInverted) {
				if (line[currentBitIndex] == '1') {
					amountOfOnes++;
				}
			}
			removeBit = linesInverted.length - amountOfOnes <= amountOfOnes ? '1' : '0';
			linesInverted = remove!(a => a[currentBitIndex] == removeBit)(linesInverted);
		}

		writeln(lines);
		writeln(linesInverted);
		finished = lines.length == 1 && linesInverted.length == 1;
		currentBitIndex++;
	} while(!finished);
	
	auto values = printAndCalculateDecimalValue(counts, count);
	writeln("Part A: ", values[0] * values[1]);
	writeln("Part B: ", calculateDecimalValueFromString(lines[0]) * calculateDecimalValueFromString(linesInverted[0]));
}
