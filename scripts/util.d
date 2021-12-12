import std.typecons, std.stdio, std.conv;

int submit(int part, int answer) {
   	import std.process : execute;
    import std.conv;
	auto dmd = execute(["./submit", to!string(part), to!string(answer)]);
   	return dmd.status;
}

void runAnswers(
	int function(File) partA,
	int function(File) partB,
	bool runReal = false,
	bool b = false
) {
	writeln("Part A");
	auto file = File("../input/test");
	writeln(" - Test: ", partA(file));
	file = File("../input/input");
	if (runReal) writeln(" - Real: ", partA(file));
	
	if (b) {
		writeln("\nPart B");
		file = File("../input/test");
		if (runReal) writeln(" - Test: ", partB(file));
		file = File("../input/input");
		writeln(" - Real: ", partB(file));
	}
}

struct IntMap2D
{
	int[][] map;
	
	/** 
	* Returns the value at given coordinates, will return -1 if invalid coordinates.
	*/
	auto getValueAt(int x, int y) {
		if (x < 0 ||  y < 0 || y > (map.length) - 1 || x > (map[y].length) - 1) {
			return -1;
		}
		return map[y][x];
	}

	/** 
	* Returns the value at given coordinates, will not check if the coord exists.
	*/
	void setValueAt(int x, int y, int val) {
		map[y][x] = val;
	}

	this(File file) {
		map = [];
		foreach (line; file.byLine)
		{
			int[] currentRow = [];
			foreach (value; line)
			currentRow ~= to!int(to!string(value));
			map ~= currentRow;
		}
	}

	void print() {
		for (int y = 0; y < map.length; y++) {
			for(int x = 0; x < map[y].length; x++)
			{
			write(getValueAt(x, y), " ");
			}
			writeln();
		}
		writeln();
	}
}