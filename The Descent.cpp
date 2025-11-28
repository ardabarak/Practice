#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * The while loop represents the game.
 * Each iteration represents a turn of the game
 * where you are given inputs (the heights of the mountains)
 * and where you have to print an output (the index of the mountain to fire on)
 * The inputs you are given are automatically updated according to your last actions.
 **/

int main()
{

    // game loop
    while (1) {
        int heights[8];                 ///array to store updated heights

        for (int i = 0; i < 8; i++) {
            int mountain_h; // represents the height of one mountain.
            cin >> mountain_h; cin.ignore();
            heights[i] = mountain_h;    ///adding inputs to arrray
        }

        int top;                        ///temp value for peak point

        for (int x = 0; x < 8; x++) {
            if (heights[x] > heights[top]) 
                {top = x;}              ///update top if new value is higher
        }

        cout << top << endl; // The index of the mountain to fire on.
    }
}
