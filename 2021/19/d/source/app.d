import std.stdio, std.string, std.conv, std.format, std.typecons, std.math;
import util;

struct Vector3 {
  int x;
  int y;
  int z;
}

string[] rotate(string[] beacons, int xAxis, int yAxis, int zAxis) {
  if (xAxis) {
    //rotate
  }
  if (yAxis) {
    //rotate
  }
  if (zAxis) {
    //rotate
  }
  return beacons;
}

Vector3 getDistance(Vector3 a, Vector3 b) {
  return Vector3(abs(a.x-b.x), abs(a.y-b.y), abs(a.z-b.z));
}

bool sameDistance(Vector3 a, Vector3 b) {
  return a.x == b.x && a.y == b.y && a.z == b.z; 
}

class Scanner
{
  string name;
  // Where Tuple(distance, beaconB) indexed by beaconA
  Vector3[][] beacons;

  this(string name, string[] rawBeacons) {
    this.name = name;
    this.beacons = [];
    foreach (i, beaconA; rawBeacons)
    {
      auto parts = beaconA.split(',');
      Vector3 beaconAVec = Vector3(to!int(parts[0]), to!int(parts[1]), to!int(parts[2]));
      beacons ~= [beaconAVec];
      for(int j = 0; j < 24; j++) {
        auto currentRotation = possibleRotations[j];
        string[] currentBeacons = rawBeacons.dup;
        currentBeacons = currentBeacons.rotate(currentRotation[0], currentRotation[1], currentRotation[2]);
        writeln(currentBeacons);
        break;
      }
    }
    // writeln(beaconDistances);
  }

  void findOverlap(Scanner other) {
    auto count = 0;
    // key is vecA, value is [(distance, vecB), ..]
    foreach (vecA; beacons)
    {
      auto overlapCounter = 0;
      writeln(vecA);
      // Looping over possible others.
      foreach (vecB; other.beacons)
      {
        Vector3 difference = vecA.getDistance(vecB);
        writeln(" - ", vecB);

      }
      writeln("Overlap counter: ",  overlapCounter);
      break;
    }
    writeln(count);
  }

  override string toString() const
  {
    return format("Scanner{name: '%s', beacons: %d}", name, beacons.length);
  }
}

/** 
 * 
 * Params:
 *   file = Todays input file.
 * Returns: The answer to the given file.
 */
long partA(File file) {
  // Call Part A code here.
  Scanner[] scanners = [];
  foreach (line; file.byLine)
  {
    string name = to!string(line.strip);
    string[] beacons = [];
    foreach (beaconLine; file.byLine)
    {
      if (beaconLine == "") break;
      beacons ~= to!string(beaconLine.strip);
    }
    auto scanner = new Scanner(name, beacons);
    scanners ~= scanner;
    writeln(scanner);
    break;
  }
  {
    string name = to!string(line.strip);
    string[] beacons = [];
    foreach (beaconLine; file.byLine)
    {
      if (beaconLine == "") break;
      beacons ~= to!string(beaconLine.strip);
    }
    auto scanner = new Scanner(name, beacons);
    scanners ~= scanner;
    writeln(scanner);
    break;
  }
  scanners[0].findOverlap(scanners[1]);
  return 0;
}

/** 
 * 
 * Params:
 *   file = Todays input file.
 * Returns: The answer to the given file.
 */
long partB(File file) {
  // Call Part B code here.
  foreach (line; file.byLine)
  {
    
  }
  return 0;
}

void main() {
  // Use these variables to decide what the runner needs to run.
	bool runReal = false;
	bool runB = false;

  runAnswers(&partA, &partB, runReal, runB);
}
