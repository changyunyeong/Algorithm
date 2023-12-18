#include <iostream>
#include <sstream>
using namespace std;

int main() {
	string indev;
	cin >> indev;
	// string type의 16진수 입력
	cout << hex << indev;
	// 정수 입출력 연산 시 16진법 사용하도록 하는 hex stream 사용
}

