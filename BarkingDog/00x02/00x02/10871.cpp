#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	// 저거 두 개 쓰니까 시간 확 준다... 앞으로 까먹지 말자
	int n, x, a[10000];
	cin >> n >> x;
	for (int i = 0; i < n; i++) {
		cin >> a[i];
		if (a[i] < x) {
			cout << a[i] << " ";
		}
	}
}