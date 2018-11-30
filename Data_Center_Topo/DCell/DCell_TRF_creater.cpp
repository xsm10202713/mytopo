#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
using namespace std;

int servers(int, int);
int cells(int, int);
void dcell(int, int);

int main (int argc, char **argv)
{
    int n, k;
    if (argc == 3)
    {
        n = atoi(argv[1]);
        k = atoi(argv[2]);
    }
    //  unittest();
    else{
        cout << "please input your parameters: n & k \n";
        cin >> n >> k ;
    }
    dcell(n, k);
    return 0;

}


int servers(int n, int k)
{
    int s=n;
    if(k==0) return n;
    else
    {
        for(int i=1; i<=k; i++)
        {
            s=s*(s+1);
        }
        return(s);
    }
}

int cells(int n, int k)
{
    if(k==0) return 1;
    else return (servers(n, k-1)+1);
}

void dcell(int n, int k)
{
    std::string s;
    std::stringstream out;
    ofstream fout("dcell_2_6.txt");

    //int number_of_server = servers(n, k);
    int edge = 0;
    for(int i=1; i<=k; i++)
    {
        //cells# in level i
        int number_of_cells = int(servers(n, k)/servers(n, i));

        //print the edges in each cell
        for(int j=0; j<cells(n, i); j++)
        {
            int cell = j;
            for(int v1 = j*servers(n, i-1)+j; v1<=(j+1)*servers(n, i-1)-1; v1++)
            {
                int v2 = (cell+1)*servers(n, i-1) + j;
                for(int times=0; times<=number_of_cells-1; times++)
                {
                    //cout<< v1+times*servers(n, i) << " " << v2+times*servers(n, i) << endl;
                    out << v1+times*servers(n, i) << " " << v2+times*servers(n, i) << endl;
                    edge++;
                }
                cell++;
            }
        }
    }

    for(int ver = 0; ver < servers(n, k); ver++)
    {
        int ord_of_swi = int(ver/n);
        int rank_of_swi = ord_of_swi + servers(n, k);
        //	cout << ver << " " << rank_of_swi <<endl;
        out << ver << " " << rank_of_swi <<endl;
        edge++;
    }

    fout << servers(n, k)+ servers(n, k)/n << " " << edge << " " << 2 << " " << servers(n, k) << endl;
    s = out.str();
    fout << s;
    fout.close();
}
