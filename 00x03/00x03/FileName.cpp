#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <unordered_map>
using std::cout;
using std::endl;
using std::ifstream;
using std::ofstream;
using std::string;
using std::getline;
using std::istringstream;
using std::unordered_map;
unordered_map<string, int> symtab;
unordered_map<string, int> optab;

bool errorFlag = false;
int startAdd = 0;
int progLen = 0;
int locctr = 0;

void intermediateFile(const string& line) {
	ofstream intermediate("intermediate.txt", std::ios::app);
	intermediate << line << endl;
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
	 istringstream src(line);
	 src >> label >> opcode >> operand;
	// file >> label >> opcode >> operand;
	if (opcode == "start") {
		startAdd = stoi(operand, nullptr, 16);
		locctr = startAdd;
		intermediateFile(line);
	    getline(file, line);
		// src >> label >> opcode >> operand;
	}
	else {
		locctr = 0;
	}
	// src >> label >> opcode >> operand;
	// file >> label >> opcode >> operand;
	while (!file.eof()) {
		if (line[0] != '.') {
			file >> label >> opcode >> operand;
			if (!label.find(" ")) {
				auto symbol = symtab.find(label);
				if (symbol != symtab.end()) {
					errorFlag = true;
					cout << 1;
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
				cout << 2;
			}
		}
		//file >> label;
		//if (!label.empty() && label != ".") {
		//	file >> opcode >> operand;
		//	if (!label.empty()) {  // 추가된 부분
		//		auto symbol = symtab.find(label);
		//		if (symbol != symtab.end()) {
		//			errorFlag = true;
		//			cout << 1;
		//		}
		//		else {
		//			symtab[label] = locctr;
		//		}
		//	}
		//	auto op = optab.find(opcode);
		//	if (op != optab.end()) {
		//		locctr += 3;
		//	}
		//	else if (opcode == "word") {
		//		locctr += 3;
		//	}
		//	else if (opcode == "resw") {
		//		locctr += 3 * stoi(operand);
		//	}
		//	else if (opcode == "resb") {
		//		locctr += stoi(operand);
		//	}
		//	else if (opcode == "byte") {
		//		string bt = operand.substr(2, operand.size() - 3);
		//		locctr += bt.length();
		//	}
		//	else {
		//		errorFlag = true;
		//		// cout << 2;
		//	}
		//}
		intermediateFile(line);
		getline(file, line);
		istringstream src(line);
		src >> label >> opcode >> operand;
		// file >> label >> opcode >> operand;
	}
	// getline(file, line);

	intermediateFile(line);
	progLen = locctr - startAdd;

	cout << "SYMTAB \n";
	for (const auto& entry : symtab) {
		cout << entry.first << " : " << entry.second << "\n";
	}
	cout << "Program Length: " << progLen << "\n";
	if (errorFlag) {
		cout << "에러 발생" << "\n";
	}
	file.close();
}

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
