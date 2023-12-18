#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
// hash table 자료 구조를 사용하기 위한 C++ STL
using namespace std;

int main() {
	unordered_map<string, string> hashTable;
	ifstream file;
	file.open("optable.txt");
	string word, op;			// 파일에 저장되어 있는 미모닉 코드, 머신 코드
	string mne;				// 사용자가 입력할 미모닉 코드

	if (file.is_open()) {			
		// 파일 오픈에 성공하면
			while (file >> word >> op) {
				// 미모닉 코드와 머신 코드를 입력받고
				hashTable[word] = op;
				// 해시테이블에 저장
			}
	}
	else {
		// 파일 오픈에 실패하면
		cout << "Error: 파일이 존재하지 않습니다." << "\n";
		// 파일이 존재하지 않다는 경고문을 띄우고
		return 1;			// 프로그램 종료
	}
	file.close();

	int n;			// 사용자가 입력할 미모닉 코드의 개수
	cout << "검색할 미모닉의 개수를 입력하세요: ";
	cin >> n;
	for (int i = 0; i < n; i++) {
		// 입력 개수에 맞추어 반복문 실행
		cout << "미모닉 코드를 입력하세요. 종료하려면 0를 입력하세요: " << "\n";
		cin >> mne;

		if (hashTable.find(mne) != hashTable.end()) {
			// 해시 테이블에서 탐색을 성공하면
			cout << mne << " - " << hashTable[mne] << "\n";
			// 미모닉 코드 - 머신 코드 출력
		}
		else if (hashTable.find(mne) == hashTable.end() && mne != "0") {
			// 탐색에 실패하면
			cout << "미모닉 코드가 존재하지 않습니다." << "\n";
			// 경고문 출력
		}
		if (n == 0) {
			return 0;
			// 0을 입력하면 프로그램 종료
		}
	}

	return 0;
}