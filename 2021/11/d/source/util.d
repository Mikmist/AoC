import std.typecons, std.stdio;

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