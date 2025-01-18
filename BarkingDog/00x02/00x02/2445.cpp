#include <iostream>
using namespace std;

int main() {
	// 걍 나중에 다시 풀어라... 
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		for (int j = i; j > 0; j--) {
			cout << "*";
		}
		for (int j = 2 * (n - i); j > 0; j--) {
			cout << " ";
		}
		for (int j = i; j > 0; j--) {
			cout << "*";
		}
		cout << "\n";
	}
	for (int i = n - 1; i > 0; i--) {
		for (int j = i; j > 0; j--) {
			cout << "*";
		}
		for (int j = 2 * (n - i); j > 0; j--) {
			cout << " ";
		}
		for (int j = i; j > 0; j--) {
			cout << "*";
		}
		cout << "\n";
	}
}