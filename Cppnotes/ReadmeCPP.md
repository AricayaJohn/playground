C++ is a compiled language that translates human instructions to what machine can read. 

int -> to create a function followed by function name
    -> input code
    -> return 0 to return output success

cout -> "see out"
std:: -> "standard library"


compiling -> getting c++ output through terminal:
$ g++ hello.cpp 
$ ./a.out
Hello World!
$ 

compiling a c++ file and adding a name name using -o
$ g++ hello.cpp -o hello
$ ./
bash: ./: Is a directory
$ ./hello
Hello World!
$ 


using cin
std::cout << "Enter your password: ";
std::cin >> password;

The name 
cin -> CHARACTER INPUT
Preview: Docs std::cin, which stands for “character input”, reads user input from the keyboard.
 refers to the standard input stream (pronounced “see-in”, for character input). The second operand of the >> operator (“get from”) specifies where that input goes.

cin user input once file is run
#include <iostream>

int main() {
  
  int tip = 0;
  
  std::cout << "Enter tip amount: ";
  std::cin >> tip;
  std::cout << "You paid " << tip << " dollars.";

return 0;
}

$ g++ tip.cpp 
$ ./a.out
Enter tip amount: 10
You paid 10 dollars.


Create a program that takes in the weight of an item and then calculates how much that item would weigh on Mars.
Create a program that asks for a distance in miles as input. The program will then output how much that distance is in kilometers.

#include <iostream>

int main() {
  // Add your code below  
  int weight;
  int distance;

  std::cout << "how many pounds is that item? \n";
  std::cin >> weight;

  int spaceforce = weight / 2;
  std::cout << "that weight will be " << spaceforce << "pounds in Mars. \n";

  std::cout << "Give me a distance in miles: \n";
  std::cin >> distance;

  double kilometers = distance * 1.60934;
  std::cout << "The distance in KM is " << kilometers << std::endl;

}

arrays: 
#declaring an array
    char grade[] = {'A', 'B', 'C', 'D', 'F'};

#accessing array elements
    char grade[] = {'A', 'B', 'C', 'D', 'F'};
    std::cout << grade[0];

//outputs: A

#iterating through arrays 
int fib[5] = {0, 1, 1, 2, 3};
for (int i = 0; i < 5; i++) {
    std::cout << fib[i];
}
//Outputs: 01123


vector -> is used to store a sequence of elements accessible by index. 
        -> can dynamically shrink and grow in size
        -> elements can be added or removed after a vector has been declared

#declaring a vector
    std::vector<char> alphabet = {'a', 'b', 'c'}


#adding an element (pushback)
    std::vector<int> weights;
    weights.pushback(25);
    weights.pushback(45);

//weights = {25, 45}

#removing an element (pop_back)
    std::vector<int> weights;
    weights.pushback(35);
    weights.pushback(50);

    weight.pop_back();
    
//weights = {35}

#forloop -> iterating through an array 
int fib[5] = {0, 1, 1, 2, 3};
    for (int i = 0; i < 5; i++){
    std::cout << fib[i] 
    }

#forloop in multi Array
char game[3][3] = {
  {'x', 'o', 'o'} , 
  {'o', 'x', 'x'} , 
  {'o', 'o', 'x'}  
};

for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
        std::cout << game[i][j];
    }
    std::cout << "\n";
}


std::vector<char> alphabet = {'a', 'b', 'c'}

#access the first element of a vector use .front
    std::cout << alphabet.front();

//output a

#access the last element of a vector use .back();
    std::cout << alphabet.back();

//output c

#returns the number of elements in the vector .size()
    std::cout << alphabet.size();

//output 3

Stacks and Queues

Stacks operate in a last-in-first-out (lifo)

#include <stack>
std::stack<int> plates;

plates.push(10);
plates.push(8);
plates.push(5);

//output: 10, 8, 5
Stack
5,
8,
10

plates.pop();
// output:
8,
10

std::cout << plates.top();
// output: 8

.size() function returns the number in the stack
tower.push(3);
tower.push(2);
tower.push(1);

std::cout << tower.size(); // outputs: 3

std::cout << tower.empty(); // outputs :  0 (false)

tower.pop();
tower.pop();
tower.pop();

std::cout << tower.empty(); // outputs: 1 (True)

#Queue -> operates in a first-in-first out context(FIFO)

#include <queue>

//Creating a queue called with strings in it and call it line

std::queue<std::string> line;

line.push("Amy");
line.push("Bella");
line.push("Chloe");

Chloe" -> "Bella" -> "Amy" (front element)

line.pop()

"Chloe" -> "Bella" (front element)

#accessing an element
std::cout << line.front();
//output: //Bella

std::cout << line.back();
//output: // Chloe

#Sets 
#include <unordered_set>

#include <set>

#creating an empt set of ints 
std::unordered_set<int> primes:

std::unordered_set<int> primes({2, 3, 5, 7});

#set Methods
.insert() adds a new element to the set

std::unordered_set<int> primes:

primes.insert(2);
primes.insert(3);

primes = ({2, 3})

#removing an Element

.erase() -> finction removes an element from the set

primes.erase(3);

//primes contain ({2})

#checking if emement is in a set

std::unordered_set<int> primes({2, 3, 5, 7});

if (primes.count(4)) {
    std::cout << "4 is a prime";
} 
else {
    std::cout<< "4 is not a prime";
}

//since 4 is not in set. 4 is not prime

#Hash Maps 
#include <unordered_map>
#include <map>

//Declare an unordered map with strings keys and integer values
std::unordered_map<std::string, int> country_codes (
    {{"India", 91}},
    {{"Italy", 39}}
);

#adding elements in hashmap 
country_codes.insert({"Thailand", 66});
country_codes.insert({"Peru", 51});

#another way of inserting an element is by using []
country_codes["Thailand"] = 66
country_codes["Peru"] = 51

#removing an element
.erase() function removes an element from the hashmap.
-> The argument is the key that identifies the element to be removed

country_codes.erase("Thailand");

//country_codes contains {"Peru", 51}

#Checking for an element
.count() function searches in the hashmap and returns the number of elements whose key matches the argument value.

std::unordered_map<std:: string, int> country_codes;

country_codes["Argentina"] = 54
country_codes["Belgium] = 32

if (country_codes.count("Belgium) {
    std::cout << "There is a code for Belgium";
}
else {
    std::cout << "There isnt a code for Belgium";
})

// Output there is a code for belgium

#accessing hashmap elements
std::cout << country_codes["Japan"];

//Outputs: 81


#if the map does not match any value using [] will create a value 
# -> use .at() method to throw an out_of_range exception if there is no match:

std::unordered_map<std:: string, int> country_codes;

country_codes["Japan"] = 81;
country_codes["Turkey"] = 90; 

std::cout << country_codes.at("Pakistan"); 

//Output: out_of_range

#iterating through a hashmap
for-each loop provides a convenient syntax for traversing a hashmap.

std::unordered_map<std::string, int> country_codes;
country_codes["Japan"] = 81;
country_codes["Turkey"] = 90;
country_codes["Pakistan"] = 92;

for(auto it: country_codes){
    std::cout << it.first << " " << it.second << "\n";
}


std::unordered_map<int, char> unordered({{2, 'b'}, {1, 'a'}, {3, 'c'}});
for(auto it: unordered){
  std::cout << it.first << " " << it.second << "\n";
}

std::cout << "\n";

std::map<int, char> ordered({{2, 'b'}, {1, 'a'}, {3, 'c'}});
for(auto it: ordered){
  std::cout << it.first << " " << it.second << "\n";
}

3 c
1 a
2 b

1 a
2 b
3 c





