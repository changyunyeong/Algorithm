#include <iostream>
using namespace std;

int main() {
	for (int i = 1; i <= 10; i++) {
		for (int j = 10; j > i; j--) {
			cout << " ";
		}
		for (int j = 1; j <= i; j++) {
			cout << "*";
		}
		cout << endl;
	}
	for (int i = 10; i >= 1; i--) {
		for (int j = 0; j < 10 - i; j++) {
			cout << " ";
		}
		for (int j = 1; j <=i ; j++) {
			cout << "*";
		}
		cout << endl;
	}
}

//#include <iostream>
//#include <string>
//#include <fstream>
//#include <sstream>
//#include <unordered_map>
//using std::cout;
//using std::endl;
//using std::ifstream;
//using std::ofstream;
//using std::string;
//using std::getline;
//using std::istringstream;
//using std::unordered_map;
//
//unordered_map<string, int> symtab;
//unordered_map<string, int> optab;
//
//bool errorFlag = false;
//int startAdd = 0x0000;
//int progLen = 0x0000;
//int locctr = 0x0000;
//
//void intermediateFile(const string& line) {
//	ofstream intermediate("intermediate.txt", std::ios::app);
//	intermediate << line << endl;
//	intermediate.close();
//}
//
//void pass1() {
//	ifstream file("srcfile.txt");
//	if (!file.is_open()) {
//		cout << "Error: ������ �� �� �����ϴ�" << "\n";
//		// ������ ������ ��� ���
//	}
//	string line;
//	string label, opcode, operand;
//	getline(file, line);
//	istringstream src(line);
//	// ������ �����ϱ� ���� istringstream ���
//	src >> label >> opcode >> operand;
//	if (opcode == "start") {
//		// opcode�� start�̸�
//		startAdd = stoi(operand, nullptr, 16);
//		// operand�� ���� �ּҷ� ����
//		locctr = startAdd;
//		// loccation counter�� ���� �ּҷ� �ʱ�ȭ
//		intermediateFile(line);
//		// �߰� ���Ͽ� ����ϰ�
//		getline(file, line);
//		// ���� �� ����
//	}
//	else {
//		// opcode�� start�� �ƴϸ�
//		locctr = 0;
//		// locctr 0���� �ʱ�ȭ
//	}
//	while (!file.eof()) {
//		// ������ ������ ������, �� opcode�� end�� �ƴϰ�
//		if (line[0] != '.') {
//			// �ּ��� �ƴϰ�
//			if (!label.find(" ")) {
//				// label�� ������ �ƴϸ�, �� label�� symbol�� ������
//				auto symbol = symtab.find(label);
//				// symtab���� symbol Ž��
//				if (symbol != symtab.end()) {
//					// �ߺ��� �ɺ��� ������
//					errorFlag = true;
//					// ���� �÷��� ����
//				}
//				else {
//					symtab[label] = locctr;
//					// symtab�� label, locctr ����
//				}
//			}
//			auto op = optab.find(opcode);
//			// optab���� opcode Ž��
//			if (op != optab.end()) {
//				// Ž���� �����ϸ�
//				locctr += 3;
//				// locctr 3 ����
//			}
//			else if (opcode == "word") {
//				locctr += 3;
//				// opcode�� word�̸� locctr 3 ����
//			}
//			else if (opcode == "resw") {
//				locctr += 3 * stoi(operand);
//				// opcode�� resw�̸� operand�� ���̿� 3 ���� ���� locctr�� ����
//			}
//			else if (opcode == "resb") {
//				locctr += stoi(operand);
//				// opcode�� resb�̸� operand�� ���� locctr�� ����
//			}
//			else if (opcode == "byte") {
//				string bt = operand.substr(2, operand.size() - 3);
//				locctr += bt.length();
//				// opcode�� byte�̸� ����Ʈ�� ���̸�ŭ locctr�� ����
//			}
//			else {
//				errorFlag = true;
//				// �������� ���� �÷��� ����
//			}
//		}
//		intermediateFile(line);
//		getline(file, line);
//		istringstream src(line);
//		src >> label >> opcode >> operand;
//	}
//
//	intermediateFile(line);
//	progLen = locctr - startAdd;
//	// ���α׷� ���� ����
//
//	cout << "SYMTAB \n";
//	for (const auto& entry : symtab) {
//		cout << entry.first << " : " << entry.second << "\n";
//	}
//	cout << "Program Length: " << progLen << "\n";
//	if (errorFlag) {
//		cout << "���� �߻�" << "\n";
//		// ������ �ִٸ� ���� �޽��� ���
//	}
//	file.close();
//}
//
//int main() {
//	optab["lda"] = 00;
//	optab["sta"] = 12;
//	optab["tix"] = 44;
//	optab["stl"] = 20;
//	optab["jsub"] = 72;
//	optab["comp"] = 40;
//	optab["jeq"] = 48;
//	optab["j"] = 60;
//	optab["rsub"] = 76;
//	optab["byte"] = 1;
//	optab["word"] = 3;
//	optab["resw"] = 3;
//	optab["resb"] = 1;
//	optab["td"] = 224;
//	optab["rd"] = 216;
//	optab["ldx"] = 04;
//	optab["stch"] = 84;
//	optab["jlt"] = 56;
//	optab["stx"] = 16;
//	optab["wd"] = 220;
//	optab["ldch"] = 80;
//	pass1();
//	return 0;
//}
