#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int tall[10];
	int sum = 0;
	for (int i = 0; i < 9; i++) {
		cin >> tall[i];
		sum += tall[i];
	}
	sort(tall, tall + 9);
	for (int i = 0; i < 8; i++) {
		for (int j = i + 1; j < 9; j++) {
			if (sum - (tall[i] + tall[j]) == 100) {
				// 두 명을 뺀 값의 합이 100이 되면
				for (int k = 0; k < 9; k++) {
					if (k != i && k != j) {
						cout << tall[k] << "\n";
					}
				}
				return 0;
				// 종료 안 하면 runtime error (정상적으로 종료 안 될 수 있음)
			}
		}
	}
}