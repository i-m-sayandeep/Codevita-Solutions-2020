#include <bits/stdc++.h>
using namespace std;

bool Prime(int n) {
    if (n == 1 or n==0)
        return false;
    if (n == 3 or n==2)
        return true;
    if (n % 2 == 0 || n % 3 == 0)
        return false;
    for (int i = 5; i * i <= n; i = i + 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}


int main() 
{
	int x, y; 
	cin >> x >> y;
	vector<int> m, n;

	m.push_back(x);
	n.push_back(y);

	while(x > 1)
	{
		if(Prime(x))
		{
			m.push_back(1);
			break;
		}
		else
		{
			for(int i=2; i*i <= x; i++)
			{
				if(x % i == 0)
				{
					m.push_back(x/i);
					x /= i;
					break;
				}
			}
		}
	}
	while(y > 1)
	{
		if(Prime(y))
		{
			n.push_back(1);
			break;
		}
		else
		{
			for(int i=2; i*i <= y; i++)
			{
				if(y % i == 0)
				{
					n.push_back(y/i);
					y /= i;
					break;
				}
			}
		}
	}

	int val,c,d;
	c = m.size();
	d = n.size();

	set<int> t(m.begin(), m.end());

	for(int i=0; i<d; i++)
	{
		if(t.find(n[i]) != t.end())
		{
			val = n[i];
			break;
		}
	}

	int count = 0;
	for(int i=0; i<c; i++)
	{
		if(m[i] > val) 
		    count++;
		else 
		    break;
	}
	for(int i=0; i<d; i++)
	{
		if(n[i] > val) 
		    count++;
		else 
		    break;
	}

	cout << count << endl;

	return 0;
}