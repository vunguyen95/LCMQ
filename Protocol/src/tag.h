#ifndef TAG_H
#define TAG_H
#include<random>
#include<vector>
#include<iostream>
#include<boost/dynamic_bitset.hpp>
using dbitset = boost::dynamic_bitset<>;
using namespace std;

/*LCMQ Tag
    @m: key length
    @n, eta: LPN length and noise rate
    @k1,k2: keys. k2 is of even hamming weight.
*/


class Tag{
    private:
        dbitset k1;
        dbitset k2;
    public:
        int m;
        int n;
        float eta;
        /*Constructor
        Initialize public parameters and private keys
        */
        Tag(const int& length_m, const int& lenth_n, const float& noise_rate);
        /* see tag attributes*/
        void see_params();
        void set_keys(const dbitset& first, const dbitset& second);
        pair<dbitset, dbitset> response(const dbitset& challenge);
    
};
#endif

inline dbitset right_shift(const dbitset& bits, const size_t& i){
    auto temp = bits;
    return (temp >> i) | (temp << (bits.size() - i));
}

inline int scalar_product(const dbitset& a, const dbitset b){
    auto bitwise_and = a & b;
    return bitwise_and.count();
}

inline vector<dbitset> portrait(const dbitset& a, const int& n){
    auto length = a.size();
    //cout << " Length:" << length << endl;
    assert(length >= n);
    vector<dbitset> matrix(length);
    for(auto i = 0; i < length; i++){
        matrix[i] = right_shift(a, i);
        matrix[i] >>= (length-n);
        for(auto j = 0; j < length- n; j++){
            matrix[i].pop_back();
        }
    }
    return matrix;
}
/*inline matrix_multiplication(const dbitset& a, const vector<dbitset> C){

}*/
//inline 