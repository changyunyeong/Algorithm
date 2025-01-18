#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n;
	int arr[100];
	int v;
	int cnt = 0;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}
	cin >> v;
	for (int i = 0; i < n; i++) {
		if (arr[i] == v) {
			cnt++;
		}
	}
	cout << cnt;
}