import std.stdio, std.string, std.format, std.conv, std.algorithm.iteration, std.algorithm.searching;
import util;

long getNumberFromBinaryString(string binary) {
  long value = 0;
  long mult = 1;
  foreach_reverse (character; binary)
  {
    if (character == '1') value += mult;
    mult *= 2;
  }
  return value;
}

string hexToBin(string source)
{
    long value;
    formattedRead(source, "%x", &value);
    string bin = format("%b", value);
    string pad = "";
    for(long i = bin.length; i < 4; i++) 
      pad ~= "0";
    return pad ~ bin;
}

class Package 
{
  long packetVersion;
  long packetTypeID;

  this(ref string binaryLine) {
    packetVersion = getNumberFromBinaryString(binaryLine[0 .. 3]);
    packetTypeID = getNumberFromBinaryString(binaryLine[3 .. 6]); 
  }

  abstract long executeOperation();

  long getVersionSum() {
    return packetVersion;
  }
}

class ValuePackage : Package
{
  long value;
  
  this(ref string binaryLine, ref long parsedBits) {
    super(binaryLine);
    auto parsedHere = 6;
    string number = "";
    for(long i = 6; i < binaryLine.length; i += 5) {
      number ~= binaryLine[i + 1 .. i + 5];
      parsedHere += 5;
      if (binaryLine[i] == '0')
        break;
    }
    if (getNumberFromBinaryString(number) < 0 ) writeln("panic ", number, " ", parsedHere);
    parsedBits += parsedHere;
    binaryLine = binaryLine[parsedHere .. $];
    value = getNumberFromBinaryString(number);
  }

  override long executeOperation() {
    return to!long(value);
  }

  override string toString() const
  {
    return format("ValuePackage(packetVersion: %d, packetTypeID: %d, value: %d)", packetVersion, packetTypeID, value);
  }
}

class OperatorPackage : Package {
  long typeId;
  Package[] subPackages;

  this(ref string binaryLine, ref long parsedBits) {
    super(binaryLine);
    subPackages = [];
    typeId = getNumberFromBinaryString([binaryLine[6]]);
    switch(typeId) {
      case 0:
        parsedBits += 22;
        auto amountOfBits = getNumberFromBinaryString(binaryLine[7 .. 22]);
        binaryLine = binaryLine[22 .. $];
        for (long i = 0; i < amountOfBits; ) {
          long usedBits = 0;
          subPackages ~= addPackage(binaryLine, usedBits);
          i += usedBits;
          parsedBits += usedBits;
        }
        break;
      case 1:
        parsedBits += 18;
        auto amountOfPackages = getNumberFromBinaryString(binaryLine[7 .. 18]);
        binaryLine = binaryLine[18 .. $];
        for (long i = 0; i < amountOfPackages; i++) {
          subPackages ~= addPackage(binaryLine, parsedBits);
        }
        break;
      default:
        break;
    }
  }

  override long getVersionSum() {
    long sum = this.packetVersion;
    foreach (Package key; subPackages)
    {
      sum += key.getVersionSum;
    }
    return sum;
  }

  override long executeOperation() {
    long[] values = [];
    foreach (key; subPackages)
      values ~= key.executeOperation;
    switch(packetTypeID) {
      case 0:
        return reduce!"a+b"(values);
      case 1:
        return reduce!"a*b"(values);
      case 2:
        return minElement(values);
      case 3:
        return maxElement(values);
      case 5:
        return values[0] > values[1] ? 1 : 0;
      case 6:
        return values[0] < values[1] ? 1 : 0;
      case 7:
        return values[0] == values[1] ? 1 : 0;
      default: 
    }
    return 0;
  }

  private static Package addPackage(ref string binaryLine, ref long parsedBits) {
    auto packetTypeID = getNumberFromBinaryString(binaryLine[3 .. 6]);
    if (packetTypeID == 4) 
      return new ValuePackage(binaryLine, parsedBits);
    return new OperatorPackage(binaryLine, parsedBits);
  }

  override string toString() const
  {
    return format("OperatorPackage(packetVersion: %d, packetTypeID: %d, typeId: %d, packages: %s)", 
      packetVersion, packetTypeID, typeId, subPackages);
  }
}

long parseHexAndDecode(File file, bool partB = false) {
  string binLine = "";
  foreach (character; file.readln) 
    binLine ~= hexToBin(to!string(character));
  long bits = 0;
  auto mainPackage = new OperatorPackage(binLine, bits);

  if (partB) return mainPackage.executeOperation;
  return to!long(mainPackage.getVersionSum);
}

/** 
 * 
 * Params:
 *   file = Todays input files.
 * Returns: The answer to the given file.
 */
auto partA(File file) {
  // Call Part A code here.
  return parseHexAndDecode(file);
}

/** 
 * 
 * Params:
 *   file = Todays input files.
 * Returns: The answer to the given file.
 */
auto partB(File file) {
  // Call Part B code here.
  return parseHexAndDecode(file, true);
}

void main() {
  // Use these variables to decide what the runner needs to run.
	bool runReal = true;
	bool runB = true;
  
  runAnswers(&partA, &partB, runReal, runB);
}
