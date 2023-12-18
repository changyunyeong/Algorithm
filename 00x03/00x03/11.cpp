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
//		cout << "Error: 파일을 열 수 없습니다" << "\n";
//		// 파일이 없으면 경고문 출력
//	}
//	string line;
//	string label, opcode, operand;
//	getline(file, line);
//	istringstream src(line);
//	// 공백을 무시하기 위해 istringstream 사용
//	src >> label >> opcode >> operand;
//	if (opcode == "start") {
//		// opcode가 start이면
//		startAdd = stoi(operand, nullptr, 16);
//		// operand를 시작 주소로 설정
//		locctr = startAdd;
//		// loccation counter를 시작 주소로 초기화
//		intermediateFile(line);
//		// 중간 파일에 출력하고
//		getline(file, line);
//		// 다음 줄 읽음
//	}
//	else {
//		// opcode가 start가 아니면
//		locctr = 0;
//		// locctr 0으로 초기화
//	}
//	while (!file.eof()) {
//		// 파일의 끝까지 읽으면, 즉 opcode가 end가 아니고
//		if (line[0] != '.') {
//			// 주석이 아니고
//			if (!label.find(" ")) {
//				// label이 공백이 아니면, 즉 label에 symbol이 있으면
//				auto symbol = symtab.find(label);
//				// symtab에서 symbol 탐색
//				if (symbol != symtab.end()) {
//					// 중복된 심볼이 있으면
//					errorFlag = true;
//					// 에러 플래그 생성
//				}
//				else {
//					symtab[label] = locctr;
//					// symtab에 label, locctr 삽입
//				}
//			}
//			auto op = optab.find(opcode);
//			// optab에서 opcode 탐색
//			if (op != optab.end()) {
//				// 탐색에 성공하면
//				locctr += 3;
//				// locctr 3 증가
//			}
//			else if (opcode == "word") {
//				locctr += 3;
//				// opcode가 word이면 locctr 3 증가
//			}
//			else if (opcode == "resw") {
//				locctr += 3 * stoi(operand);
//				// opcode가 resw이면 operand의 길이에 3 곱한 것을 locctr에 더함
//			}
//			else if (opcode == "resb") {
//				locctr += stoi(operand);
//				// opcode가 resb이면 operand의 길이 locctr에 더함
//			}
//			else if (opcode == "byte") {
//				string bt = operand.substr(2, operand.size() - 3);
//				locctr += bt.length();
//				// opcode가 byte이면 바이트의 길이만큼 locctr에 더함
//			}
//			else {
//				errorFlag = true;
//				// 나머지는 에러 플래그 생성
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
//	// 프로그램 길이 구함
//
//	cout << "SYMTAB \n";
//	for (const auto& entry : symtab) {
//		cout << entry.first << " : " << entry.second << "\n";
//	}
//	cout << "Program Length: " << progLen << "\n";
//	if (errorFlag) {
//		cout << "에러 발생" << "\n";
//		// 에러가 있다면 에러 메시지 출력
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
