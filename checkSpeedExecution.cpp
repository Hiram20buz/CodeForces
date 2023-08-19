#include <iostream>
#include <chrono>
#include <vector>
#include <sstream>
using namespace std;

int main() {
    auto start = std::chrono::high_resolution_clock::now();
    
    // Your code here
    string input="3 3";
    istringstream iss(input);
    
    vector<int> l;
    int num;
    while (iss >> num) {
        l.push_back(num);
    }
    
    cout << (l[0] * l[1]) / 2 << endl;
    
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> duration = end - start;
    std::cout << "Execution time: " << duration.count() << " seconds" << std::endl;
    
    return 0;
}
