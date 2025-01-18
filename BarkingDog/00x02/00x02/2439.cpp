#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		for (int j = t; j > i; j--) {
			// 5,4,3,2 -> 5,4,3 이런 식으로 실행됨
			cout << " ";
		}
		for (int j = 1; j <= i; j++) {
			// 1 -> 1,2 이런 식으로 실행됨
			cout << "*";
		}
		cout << "\n";
	}
}