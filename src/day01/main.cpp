#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

void printFile(string file) {
    cout << file.length();
    for (int i = 0; i < file.length(); i++) {
        cout << file[i] << endl;
    }
}

int main()
{
    ifstream ifs("input.txt");
    ostringstream oss;
    oss << ifs.rdbuf();
    string entireFile = oss.str();
    /*cout << entireFile << endl;*/
    printFile(entireFile);
    return 0;
}

