import std.stdio, std.conv, std.array;

void main() {
    auto inputFile = "./input/input";
    writeln("Currently testing: " ~ inputFile);
    auto input = new File(inputFile, "r");

    auto previous = -1;
    auto cnt = 0;
    auto sums = new int[0];
    auto idx = 0;
    foreach (element; input.byLine)
    {
        auto intElement = to!int(element);

        // Part A
        if (previous != -1 && previous < intElement)
            cnt++;

        // Part B
        sums ~= intElement;
        if (idx-1 >= 0) sums[idx-1] += intElement;
        if (idx-2 >= 0) sums[idx-2] += intElement;
        idx++;

        // General
        previous = intElement;
    }
    writeln("Part A: " ~ to!string(cnt));
    
    previous = -1;
    cnt = 0;
    foreach (sum; sums)
    {
        auto intElement = to!int(sum);
        if (previous != -1 && previous < intElement)
            cnt++;
        previous = intElement;
    }
    writeln("Part B: " ~ to!string(cnt));
}