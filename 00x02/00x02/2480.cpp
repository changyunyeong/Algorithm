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
		// �� ���� �����Ƿ� �߰����� �׻� ��ġ�� ��
		total = z * 100 + 1000;
		cout << total;
	}
	//else if a==b || a==c		// ���� ���� �� ���� �� (a�� �ߺ�)
	//else if b==c			// ���� ���� �� ���� �� (a�� �ٸ�)
	//else max �Լ�			// ��� �ٸ� ���� ��
}