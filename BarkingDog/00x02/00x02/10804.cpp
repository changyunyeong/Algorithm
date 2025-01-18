#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int arr[21] = { 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 };
	int a, b;
	for (int i = 0; i < 10; i++) {
		cin >> a >> b;
		int range = (b - a + 1) / 2;
		for (int i = 0; i < range; i++) {
			swap(arr[a + i], arr[b - i]);
		}		// 배열 인덱스 헷갈려서 오래걸림...ㅎ 사람이냐
	}
	for (int i = 1; i <= 20; i++) {
		cout << arr[i] << " ";
	}

	//for (int i = 1; i <= 10; i++) {
	//	int a, b;
	//	cin >> a >> b;
	//	reverse(num + a, num + b + 1);
	//}			// reverse STL 이용할 수도 있다
}
