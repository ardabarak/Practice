#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cstdlib>

using namespace std;

/**
 * Solve this puzzle by writing the shortest code.
 * Whitespaces (spaces, new lines, tabs...) are counted in the total amount of chars.
 * These comments should be burnt after reading!
 **/

int main()
{
    int lx; // the X position of the light of power
    int ly; // the Y position of the light of power
    int tx; // Thor's starting X position
    int ty; // Thor's starting Y position
    cin >> lx >> ly >> tx >> ty; cin.ignore();

    // game loop
    while (1) {
        int remaining_turns; // The level of Thor's remaining energy, representing the number of moves he can still make.
        cin >> remaining_turns; cin.ignore();

        // Write an action using cout. DON'T FORGET THE "<< endl"
        // To debug: cerr << "Debug messages..." << endl;
        int difX = std::abs(lx - tx); // vertical   difference (absolute)
        int difY = std::abs(ly - ty); // horizontal difference (absolute)
        cerr << "Debug messages... :: difX = " << difX << endl;
        cerr << "Debug messages... :: difY = " << difY << endl;

        if (difX > difY) {      // if horizontal distance is greater
            if ((lx - tx) > 0) {
                tx += 1;
                cout << "E" << endl;
            } else if (0 > (lx - tx)) {
                tx -= 1;
                cout << "W" << endl;
            }
        }
        else if (difY > difX) { // if verical distance is greater
            if ((ly - ty) > 0) {
                ty += 1;
                cout << "S" << endl;
            }
            else if (0 > (ly - ty)) {
                ty -= 1;
                cout << "N" << endl;
            }
        }
        else if (difX == difY) { // if distance is the same in both vertical and horizontal
            cerr << "Debug messages... :: lx-tx = " << (lx - tx) << endl;
            cerr << "Debug messages... :: ly-ty = " << (ly - ty) << endl;
            if (0 > (lx - tx)) {           // x = -
                if (0 > (ly- ty)) {         // y = - 
                    ty -= 1;
                    tx -= 1;
                    cout << "NW" << endl;
                }
                else if ((ly - ty) > 0) {   // y = +
                    ty += 1;
                    tx -= 1;
                    cout << "SW" << endl;
                }
            }
            else if ((lx - tx) > 0) {      // x = +
                if (0 > (ly- ty)) {         // y = - 
                    ty -= 1;
                    tx += 1;
                    cout << "NE" << endl;
                }
                else if ((ly - ty) > 0) {   // y = + 
                    ty += 1;
                    tx += 1;
                    cout << "SE" << endl;    
                }
            }

        }


        // // A single line providing the move to be made: N NE E SE S SW W or NW
        // cout << "SE" << endl;
    }
}
