int submit(int day, int answer) {
   	import std.process : execute;
        import std.conv;
	auto dmd = execute(["./submit", to!string(day), to!string(answer)]);
   	return dmd.status;
}

