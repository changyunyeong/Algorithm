#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int arr[3];
	for (int i = 0; i < 3; i++) {
		cin >> arr[i];
	}
	//for (int i = 0; i < 3; i++) {
	//	for (int j = 0; j < 3; j++) {
	//		if (arr[j] < arr[j + 1]) {
	//			int temp = arr[j];
	//			arr[j] = arr[j + 1];
	//			arr[j + 1] = temp;
	//		}
	//	}
	//}			// 굳이 정렬 이용할 필요 없음 sort 이용하면 쉽고 빠름
	sort(arr, arr + 3);
	for (int i = 0; i < 3; i++) {
		cout << arr[i] << "\n";
	}
}