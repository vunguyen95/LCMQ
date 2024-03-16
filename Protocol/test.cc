#include<iostream>
#include<random>
#include"src/tag.h"
#include<boost/dynamic_bitset.hpp>

using namespace std;
inline int scalar_product(const dbitset& a, const dbitset b){
    auto bitwise_and = a & b;
    return bitwise_and.count();
}

dbitset right_shift(const dbitset& bits, const size_t& i){
    auto temp = bits;
    return (temp >> i) | (temp << (bits.size() - i));
}


int main(){
    Tag lcmqt(10, 9 , 0.1);
    lcmqt.see_params();
    dbitset test1(4,15);
    dbitset test2(4,10);
    cout << scalar_product(test1, test2) << endl;
    cout << test2 << endl;
    
    cout << right_shift(test2, 2) << endl;
    dbitset challenge(10, 0);
    auto pair = lcmqt.response(challenge);
    cout << pair.first << endl;
    cout << pair.second << endl;
}