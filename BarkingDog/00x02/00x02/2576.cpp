#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n, odd = 0, sum = 0, min = 100;
	// ���� �ʱ�ȭ ����... �ʱ�ȭ �� �ؼ� Ʋ��
	for (int i = 0; i < 7; i++) {
		cin >> n;
		if (n & 1) {
			// Ȧ�� �ľ��� �� ��Ʈ ���굵 �ִٴ� �� ���� ����
			sum += n;
			odd++;
			if (n < min) {
				min = n;
			}
		}
		// ���ʿ� �̰� �� ���� ��� ���� �ް� ���߿� �Ǵ��Ϸ� �ϸ� �� ����
		// ���� ������ ���������� �ϳ� �ް� �Ѳ����� ��� ��츦 ó���ؾ� ����
	}
	if (odd == 0) {
		cout << "-1";
	}
	else {
		cout << sum << "\n" << min;
	}
}