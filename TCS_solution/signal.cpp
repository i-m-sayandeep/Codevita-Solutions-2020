#include<bits/stdc++.h>
#define R 6371
using namespace std;
vector<float>lat;
vector<float>lon;
vector<int>ht;
vector<float>jason;

void input(int n){
    float jlat,jlon;
for(int i=0;i<n;i++){
        float la;
        cin>>la;
        lat.push_back(la);
    }
      for(int i=0;i<n;i++){
        float lo;
        cin>>lo;
        lon.push_back(lo);
    }
       for(int i=0;i<n;i++){
               int h;
               cin>>h;
               ht.push_back(h);
    }
    cout<<"enter jason";
    cin>>jlat; jason.push_back(jlat);
     cin>>jlon; jason.push_back(jlon);

}
long double toRadians(const long double degree){
    long double one_deg = (3.141592653589793238) / 180;
    return (one_deg * degree);
}
float reach(int h){
float dist;
dist=2*h*R;
dist=pow(dist,0.5);
return dist;
}
long double cal(float lat1,float long1,float lat2,float long2){
 lat1 = toRadians(lat1);
    long1 = toRadians(long1);
    lat2 = toRadians(lat2);
    long2 = toRadians(long2);

    // Haversine Formula
    long double dlong = long2 - long1;
    long double dlat = lat2 - lat1;

    long double ans = pow(sin(dlat / 2), 2) +
                          cos(lat1) * cos(lat2) *
                          pow(sin(dlong / 2), 2);

    ans = 2 * asin(sqrt(ans));

    // Radius of Earth in
    // Kilometers, R = 6371
    // Use R = 3956 for miles


    // Calculate the result
    ans = ans * R;

    return ans;
}

int main()
{
    int n,counter=0;
    cin>>n;
    input(n);
    for(int i=0;i<n;i++){
        int x,c;
        x=reach(ht[i]);
        c=cal(lat[i],lon[i],jason[0],jason[1]);
        if(c<=x){
            counter+=1;
        }

    }
     cout<<counter;
    return 0;
}
