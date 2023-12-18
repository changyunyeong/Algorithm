#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
// hash table �ڷ� ������ ����ϱ� ���� C++ STL
using namespace std;

int main() {
	unordered_map<string, string> hashTable;
	ifstream file;
	file.open("optable.txt");
	string word, op;			// ���Ͽ� ����Ǿ� �ִ� �̸�� �ڵ�, �ӽ� �ڵ�
	string mne;				// ����ڰ� �Է��� �̸�� �ڵ�

	if (file.is_open()) {			
		// ���� ���¿� �����ϸ�
			while (file >> word >> op) {
				// �̸�� �ڵ�� �ӽ� �ڵ带 �Է¹ް�
				hashTable[word] = op;
				// �ؽ����̺� ����
			}
	}
	else {
		// ���� ���¿� �����ϸ�
		cout << "Error: ������ �������� �ʽ��ϴ�." << "\n";
		// ������ �������� �ʴٴ� ����� ����
		return 1;			// ���α׷� ����
	}
	file.close();

	int n;			// ����ڰ� �Է��� �̸�� �ڵ��� ����
	cout << "�˻��� �̸���� ������ �Է��ϼ���: ";
	cin >> n;
	for (int i = 0; i < n; i++) {
		// �Է� ������ ���߾� �ݺ��� ����
		cout << "�̸�� �ڵ带 �Է��ϼ���. �����Ϸ��� 0�� �Է��ϼ���: " << "\n";
		cin >> mne;

		if (hashTable.find(mne) != hashTable.end()) {
			// �ؽ� ���̺��� Ž���� �����ϸ�
			cout << mne << " - " << hashTable[mne] << "\n";
			// �̸�� �ڵ� - �ӽ� �ڵ� ���
		}
		else if (hashTable.find(mne) == hashTable.end() && mne != "0") {
			// Ž���� �����ϸ�
			cout << "�̸�� �ڵ尡 �������� �ʽ��ϴ�." << "\n";
			// ��� ���
		}
		if (n == 0) {
			return 0;
			// 0�� �Է��ϸ� ���α׷� ����
		}
	}

	return 0;
}