#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	long long a, b;
	// 문제 조건 생각해서 long long으로 접근한 건 좋았음
	cin >> a >> b;
	if (a > b) {
		swap(a, b);
		// 항상 a가 b보다 작을 거라 생각했음
	}
	if (a == b || b - a == 1) {
		// a,b가 같거나 1 차이가 난다면 그 사이에 있는 수는 없음
		// 항상 예외를 생각할 것
		cout << 0;
	}
	else {
		cout << b - a - 1 << "\n";
		for (long long i = a + 1; i < b; i++) {
			cout << i << " ";
		}
	}
}