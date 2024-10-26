#include <iostream>
#include <string>
#include <cassert>


std::string determine_direction(int x1, int y1, int x2, int y2, int x, int y)
{
	if (x <= x1 && y >= y2)
		return "NW";
	else if (x <= x1 && y <= y1)
		return "SW";
	else if (x >= x2 && y >= y2)
		return "NE";
	else if (x >= x2 && y <= y1)
		return "SE";
	else if (y >= y2)
		return "N";
	else if (y <= y1)
		return "S";
	else if (x <= x1)
		return "W";
	else
		return "E";

}

/*
void tests()
{
	assert(determine_direction(-1, -2, 5, 3, -4, 6) == "NW");
	assert(determine_direction(-1, -2, 5, 3, -1, 10) == "NW");
	assert(determine_direction(-1, -2, 5, 3, -8, 6) == "NW");

	assert(determine_direction(-1, -2, 5, 3, 8, 9) == "NE");
	assert(determine_direction(-1, -2, 5, 3, 5, 15) == "NE");
	assert(determine_direction(-1, -2, 5, 3, 6, 3) == "NE");

	assert(determine_direction(-1, -2, 5, 3, -4, -6) == "SW");
	assert(determine_direction(-1, -2, 5, 3, -1, -10) == "SW");
	assert(determine_direction(-1, -2, 5, 3, -15, -2) == "SW");

	assert(determine_direction(-1, -2, 5, 3, 10, -5) == "SE");
	assert(determine_direction(-1, -2, 5, 3, 5, -15) == "SE");
	assert(determine_direction(-1, -2, 5, 3, 30, -2) == "SE");

	assert(determine_direction(-1, -2, 5, 3, 0, 10) == "N");
	assert(determine_direction(-1, -2, 5, 3, 12, 0) == "E");
	assert(determine_direction(-1, -2, 5, 3, 4, -2) == "S");
	assert(determine_direction(-1, -2, 5, 3, -5, 1) == "W");


	std::cout << "Complite!" << std::endl;
}
*/

int main()
{

	int x1, y1, x2, y2, x, y;
	std::cin >> x1 >> y1 >> x2 >> y2 >> x >> y;
	std::cout << determine_direction(x1, y1, x2, y2, x, y);

	// tests();
	return 0;
}