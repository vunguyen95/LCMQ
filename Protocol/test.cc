#include<iostream>
#include<random>
#include"src/tag.h"
#include<boost/dynamic_bitset.hpp>

using namespace std;
int scalar_product(const dbitset& a, const dbitset b){
    auto bitwise_and = a & b;
    return bitwise_and.count();
}


int main(){
    Tag lcmqt(10, 9 , 0.1);
    lcmqt.see_params();
    dbitset test1(4,15);
    dbitset test2(4,10);
    cout << scalar_product(test1, test2) << endl;
    cout << test2 << endl;
    
    //cout << test2.rotate_right(1) << endl;;
    cout << test2 << endl;
}