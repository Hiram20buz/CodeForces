#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

int main() {
    string input;
    getline(cin, input);
    istringstream iss(input);
    
    vector<int> l;
    int num;
    while (iss >> num) {
        l.push_back(num);
    }
    
    cout << (l[0] * l[1]) / 2 << endl;
    
    
    return 0;
}
