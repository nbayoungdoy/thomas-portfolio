#include <stdio.h>

int main() {
	int var, var2;
	printf("Type in 2 integers: ");
	scanf("%i%i", &var, &var2);
	int ans = var + var2;
	printf("The sum of the numbers is %i\n", ans);

	return 0;
}

