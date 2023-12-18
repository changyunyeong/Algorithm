#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int a = 0, b = 0, c = 0;
	cin >> a >> b >> c;
	int total;
	if (a == b && b == c) {
		total = 10000 + 1000 * a;
		cout << total;
	}
	else if (a != b && b != c && c != a) {
		int total = max(max(a, b), c) * 100;
		cout << total;
	}
	else {
		int x = max(max(a, b), c);
		int y = min(min(a, b), c);
		int z = a + b + c - x - y;
		// 두 개가 같으므로 중간값은 항상 겹치는 값
		total = z * 100 + 1000;
		cout << total;
	}
	//else if a==b || a==c		// 같은 눈이 두 개일 때 (a가 중복)
	//else if b==c			// 같은 눈이 두 개일 때 (a만 다름)
	//else max 함수			// 모두 다른 눈일 때
}