#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	long long a, b;
	// ���� ���� �����ؼ� long long���� ������ �� ������
	cin >> a >> b;
	if (a > b) {
		swap(a, b);
		// �׻� a�� b���� ���� �Ŷ� ��������
	}
	if (a == b || b - a == 1) {
		// a,b�� ���ų� 1 ���̰� ���ٸ� �� ���̿� �ִ� ���� ����
		// �׻� ���ܸ� ������ ��
		cout << 0;
	}
	else {
		cout << b - a - 1 << "\n";
		for (long long i = a + 1; i < b; i++) {
			cout << i << " ";
		}
	}
}