//this is my first c++ file to be compiled and shown in terminal
#include <iostream>

int main() {
    std::cout << "Hello World\n";
    return 0;
}

//heyprogrammer
//write a function greet that takes in a string argument, s, and returns the string "hey s"


#include <string>
#include <iostream>

std::string greet(std:: string s) {
    return "hey " + s;
}

void run() {
    std::cout << greet("bro") << std::endl;
}

//