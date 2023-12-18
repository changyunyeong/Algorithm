#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, x, sum1 = 0, sum2 = 0;
	// int* arr = new int[n];
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> x;
		sum1 += (x / 30) * 10 + 10;
		sum2 += (x / 60) * 15 + 15;
	}
	if (sum1 < sum2) {
		cout << "Y " << sum1;
	}
	else if (sum1 > sum2) {
		cout << "M " << sum2;
	}
	else {
		cout << "Y M " << sum1;
	}
}