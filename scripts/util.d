int submit(int part, int answer) {
   	import std.process : execute;
    import std.conv;
	auto dmd = execute(["./submit", to!string(part), to!string(answer)]);
   	return dmd.status;
}

