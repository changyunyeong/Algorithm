#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int arr[8];
	for (int i = 0; i < 8; i++) {
		cin >> arr[i];
	}
	int max = -1;
	int num;
	for (int i = 0; i < 8; i++) {
		if (arr[i] > max) {
			max = arr[i];
			num = i;
		}
	}
	cout << max << "\n" << num + 1;
}