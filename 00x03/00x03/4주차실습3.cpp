
// #include <iomanip>  // hex manipulator를 사용하기 위한 헤더


//int main() {
//    int locctr = 0x1000;
//    string line;
//    ifstream input("srcfile.txt");
//
//    if (!input.is_open()) {
//        cout << "Error: 파일을 열 수 없습니다" << endl;
//    }
//
//    while (getline(input, line)) {
//        cout << hex << setw(4) << setfill('0') << locctr << " " << line << "\n";
//        locctr += 3;
//    }
//
//    input.close();
//}

// #define MAX 100

//struct  OPTAB {
//	char name[8];
//	int len;
//} optab[] = { {"LDA", 00}, {"STA", 12}, {"TIX", 44}, {"STL", 20}, {"JSUB", 72}, {"COMP", 40}, {"JEQ", 48},
//{"J", 60}, {"RSUB", 76}, {"BYTE", 1}, {"WORD", 3}, {"RESW", 3}, {"RESB", 1}, {"TD", 224}, {"RD", 216}, {"LDX", 04},
//{"STCH", 84}, {"JLT", 56}, {"STX", 16}, {"WD", 220}, {"LDCH", 80} };
//
//struct TABLE {
//	char label[10], opcode[10], operand[10];
//	int addlabel;
//	int object;
//}symtab[MAX];
#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <unordered_map>
// #include <iomanip>
using namespace std;
unordered_map<string, int> symtab;
unordered_map<string, int> optab;

bool errorFlag = false;
int startAdd = 0;
int progLen = 0;
int locctr = 0;

void intermediateFile(const string& line) {
	ofstream intermediate("intermediate.txt", ios::app);
	intermediate << line << "\n";
	intermediate.close();
}

void pass1() {
	ifstream file("srcfile.txt");
	if (!file.is_open()) {
		cout << "Error: 파일을 열 수 없습니다" << "\n";
	}
	string line;
	string label, opcode, operand;
	getline(file, line);
	// istringstream src(line);
	// src >> label >> opcode >> operand;
	file >> label >> opcode >> operand;
	if (opcode == "start") {
		startAdd = stoi(operand, nullptr, 16);
		locctr = startAdd;
		intermediateFile(line);
		getline(file, line);
	}
	else {
		locctr = 0;
	}
	while (opcode != "end") {
		if (line[0] != '.' && !line.empty()) {
			//istringstream src(line);
			//src >> label >> opcode >> operand;
			file >> label >> opcode >> operand;

			if (!label.empty()) {
				auto symbol = symtab.find(label);
				if (symbol != symtab.end()) {
					errorFlag = true;
				}
				else {
					symtab[label] = locctr;
				}
			}
			auto op = optab.find(opcode);
			if (op != optab.end()) {
				locctr += 3;
			}
			else if (opcode == "word") {
				locctr += 3;
			}
			else if (opcode == "resw") {
				locctr += 3 * stoi(operand);
			}
			else if (opcode == "resb") {
				locctr += stoi(operand);
			}
			else if (opcode == "byte") {
				string bt = operand.substr(2, operand.size() - 3);
				locctr += bt.length();
			}
			else {
				errorFlag = true;
			}
		}
		intermediateFile(line);
		getline(file, line);
		//istringstream src(line);
		//src >> label >> opcode >> operand;
		file >> label >> opcode >> operand;
	}
	// getline(file, line);
	// intermediateFile(line);
	progLen = locctr - startAdd;

	cout << "SYMTAB: \n";
	for (const auto& entry : symtab) {
		cout << entry.first << " : " << entry.second << "\n";
	}
	cout << "Program Length: " << progLen << "\n";
	if (errorFlag) {
		cout << "에러 발생" << "\n";
	}
	file.close();
}

//void pass1() {
//	ifstream file("srcfile.txt");
//	if (!file.is_open()) {
//		cout << "Error: 파일을 열 수 없습니다\n";
//		return;
//	}
//
//	string line;
//	string label, opcode, operand;
//
//	getline(file, line);
//	istringstream src(line);
//
//	src >> label >> opcode >> operand;
//
//	if (opcode == "start") {
//		startAdd = stoi(operand, nullptr, 16);
//		locctr = startAdd;
//		intermediateFile(line);
//		getline(file, line);
//	}
//	else {
//		locctr = 0;
//	}
//
//	while (opcode != "end") {
//		if (!line.empty() && line[0] != '.') { // 빈 줄이거나 주석이 아닌 경우
//			istringstream src(line);
//			src >> label >> opcode >> operand;
//
//			if (!label.empty()) { // 라벨이 있는 경우
//				auto symbol = symtab.find(label);
//
//				if (symbol != symtab.end()) { // 이미 심볼 테이블에 존재하는 경우
//					errorFlag = true; // 에러 플래그 설정
//				}
//				else { // 심볼 테이블에 추가
//					symtab[label] = locctr;
//				}
//			}
//
//			auto op = optab.find(opcode);
//
//			if (op != optab.end()) { // 옵코드가 OPTAB에 존재하는 경우
//				locctr += 3;
//			}
//			else if (opcode == "word") {
//				locctr += 3;
//			}
//			else if (opcode == "resw") {
//				locctr += 3 * stoi(operand);
//			}
//			else if (opcode == "resb") {
//				locctr += stoi(operand);
//			}
//			else if (opcode == "byte") {
//				string byte = operand.substr(2, operand.size() - 3);
//				locctr += byte.length();
//			}
//			else { // 알 수 없는 옵코드인 경우 에러 처리
//				errorFlag = true;
//			}
//		}
//
//		intermediateFile(line);
//
//		getline(file, line);
//
//		src.clear();
//		src.str(line);
//
//		src >> label >> opcode >> operand;
//	}
//
//	intermediateFile(line);
//
//	progLen = locctr - startAdd;
//
//	cout << "SYMTAB: \n";
//	for (auto const& entry : symtab) {
//		cout << entry.first << " : " << entry.second << "\n";
//	}
//	cout << "Program Length: " << progLen << "\n";
//
//	if (errorFlag) {
//		cout << "에러 발생\n";
//	}
//
//	file.close();
//}

int main() {
	optab["lda"] = 00;
	optab["sta"] = 12;
	optab["tix"] = 44;
	optab["stl"] = 20;
	optab["jsub"] = 72;
	optab["comp"] = 40;
	optab["jeq"] = 48;
	optab["j"] = 60;
	optab["rsub"] = 76;
	optab["byte"] = 1;
	optab["word"] = 3;
	optab["resw"] = 3;
	optab["resb"] = 1;
	optab["td"] = 224;
	optab["rd"] = 216;
	optab["ldx"] = 04;
	optab["stch"] = 84;
	optab["jlt"] = 56;
	optab["stx"] = 16;
	optab["wd"] = 220;
	optab["ldch"] = 80;
	pass1();
	return 0;
}
