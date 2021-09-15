#include <iostream>
#include <iomanip>

using namespace std;

// Simple C++ program to demonstrate calculation on Django server;
// Prints output of first 100 numbers of the Fibonacci sequence

void fibSequence(int n) {

	// Initialize int values
	double val1 = 0, val2 = 1, next = 0;

	// Cases that cover n = 0 or 1; shouldn't be used unless
	// max is modified in main()
	if (n == 0) {
		cout << n;
		return;
	} else if (n == 1) {
		cout << val1 << " " << val2;
		return;
	}

	cout << val1 << " ";

	// Calculate next number in sequence and insert into vector
	for (int i = 1; i <= n; i++) {
		cout << setprecision(21) << val2 << " ";
		next = val1 + val2;
		val1 = val2;
		val2 = next;
	}
}

// Calls fibSequence function with sequence_num
int main() {

	// Number of Fibonacci numbers to calculate, create vector
	int max = 100;
	fibSequence(max);

	cout << "\n";
	return 0;
}