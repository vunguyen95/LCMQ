#include<iostream>
#include<random>
#include"src/tag.h"
#include<boost/dynamic_bitset.hpp>

using namespace std;


int main(){
    Tag lcmqt(10, 9 , 0.1);
    lcmqt.see_params();
    dbitset test1(4,14);
    dbitset test2(4,14);
    cout << scalar_product(test1, test2) << endl;
    cout << test2 << endl;
    
    cout << right_shift(test2, 2) << endl;
    dbitset challenge(10, 0);
    auto pair = lcmqt.response(challenge);
    cout << pair.first << endl;
    cout << pair.second << endl;
    cout << test2 << endl;
    auto matrix = portrait(test2, 3);
    for(auto i = 0; i < matrix.size(); i++){
        cout << matrix[i] << endl;
    }
}