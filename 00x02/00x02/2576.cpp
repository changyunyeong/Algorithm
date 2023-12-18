#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, odd = 0, sum = 0, min = 100;
	// 변수 초기화 하자... 초기화 안 해서 틀림
	for (int i = 0; i < 7; i++) {
		cin >> n;
		if (n & 1) {
			// 홀수 파악할 땐 비트 연산도 있다는 거 잊지 말자
			sum += n;
			odd++;
			if (n < min) {
				min = n;
			}
		}
		// 애초에 이건 한 번에 모든 수를 받고 나중에 판단하려 하면 안 됐음
		// 숫자 개수가 정해졌으니 하나 받고 한꺼번에 모든 경우를 처리해야 했음
	}
	if (odd == 0) {
		cout << "-1";
	}
	else {
		cout << sum << "\n" << min;
	}
}