#include <iostream>
using namespace std;

int func1(int n) {
	int temp = 0;
	if (n % 3 == 0 || n % 5 == 0) {
		temp += n;
	}
	return temp;
}

int fun2(int arr[], int n) {
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			if (arr[i] + arr[j] == 100) {
				return 1;
			}
			else {
				return 0;
			}
		}
	}
}

int fun3(int n) {
	for (int i = 1; i * i <= n; i++) {
		// i�� 1���� �ö󰡸� i�� ������ n�� ��ġ�ϴ��� Ȯ��
		if (i * i == n) {
			// ��ġ�ϸ� �������̴� 1 ��ȯ
			return 1;
		}
		else {
			// ��ġ���� ������ �������� �ƴϴ� 0 ��ȯ
			return 0;
		}
	}
}			// �ð����⵵ O(root n)

int fun4(int n) {
	int i = 1;
	do {
		i *= 2;
	} while (i * i <= n);
	return i;
}