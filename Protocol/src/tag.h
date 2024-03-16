#ifndef TAG_H
#define TAG_H
#include<random>
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

inline 