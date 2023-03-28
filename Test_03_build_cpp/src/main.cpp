#include <iostream>

int main(int argc, char* argv[]){
	
	std::string arg = "";
	if(argc > 1){
		arg = argv[1];
	}
	std::cout << "hello world (" + arg + ")" << std::endl;
	return 0;	
}