#include"tag.h"

Tag::Tag(const int& length_m, const int& length_n, const float& noise_rate){
    //Public parameters
    this-> m = length_m;
    this-> n = length_n;
    this-> eta = noise_rate;

    //Private keys:
    this-> k1.resize(this-> m);
    this-> k2.resize(this-> m);

    random_device rd;
    mt19937 gen(rd());
    bernoulli_distribution distri(0.5);
    for(int i = 0; i < this-> k1.size(); i++){
        this-> k1[i] = distri(gen);
    }

    while(this->k2.none() == 1 || this->k2.count() % 2 != 0){
        for(int i = 0; i < this->k2.size(); i++){
            this->k2[i] = distri(gen);
        }
    }
    
}

void Tag::set_keys(const dbitset& first, const dbitset& second){
    this->k1 = first;
    this->k2 = second;
}
void Tag::see_params(){
    cout << "m:" << this -> m << endl;
    cout << "n:" << this -> n << endl;
    cout << "noise:" << this -> eta << endl;
    cout << "Keys: " << endl;
    cout << this-> k1 << endl;
    cout << this-> k2 << endl;
    cout << this-> k2.count();
}

pair<dbitset, dbitset> Tag::response(const dbitset& challenge){
    random_device rd;
    mt19937 gen(rd());
    bernoulli_distribution uniform(0.5);
    bernoulli_distribution noise_rate(this-> eta);
    dbitset v(this-> n, 0);
    dbitset b(this-> m, 0);
    //assert(v.size() == n);
    for(auto i = 0; i < v.size(); i++){
        v[i] = noise_rate(gen);
    }
    while(b.none() == 1 || b.all() == 1){
        for(auto i = 0; i < b.size(); i++){
            b[i] = uniform(gen);
        }
    }
    dbitset y(this-> n, 0);
    
    return pair<dbitset, dbitset>(b,v);
}