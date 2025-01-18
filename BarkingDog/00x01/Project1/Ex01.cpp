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
		// i가 1부터 올라가며 i의 제곱이 n과 일치하는지 확인
		if (i * i == n) {
			// 일치하면 제곱수이니 1 반환
			return 1;
		}
		else {
			// 일치하지 않으면 제곱수가 아니니 0 반환
			return 0;
		}
	}
}			// 시간복잡도 O(root n)

int fun4(int n) {
	int i = 1;
	do {
		i *= 2;
	} while (i * i <= n);
	return i;
}