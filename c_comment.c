#include <stdio.h>
#include <string.h>
#include <stdbool.h>

// Function to check if a string is a valid C-style comment
bool isCComment(const char *str) {
    int len = strlen(str);

    // Must be at least 4 characters: /* */
    if (len < 4) return false;

    // Must start with /* and end with */
    if (!(str[0] == '/' && str[1] == '*')) return false;
    if (!(str[len-2] == '*' && str[len-1] == '/')) return false;

    // Ensure there are no extra "*/" inside before the end
    for (int i = 2; i < len-2; i++) {
        if (str[i] == '/' && str[i-1] == '*') {
            return false; // found premature closing
        }
    }

    return true;
}

int main() {
    printf("=====================================\n");
    printf("   DFA/NFA Simulation: C-Style Comments\n");
    printf("=====================================\n\n");

    // --- Predefined test cases ---
    printf(">> Running predefined test cases:\n");
    const char *tests[] = {
        "/*a*/", "/**/", "/***/", "/*aaa*aaa*/", "/*a/a*/",   // Accepted
        "/**", "/**/a/*aa*/", "aaa/**/aa", "/*/", "/**a/", "//aaaa" // Rejected
    };

    int n = sizeof(tests)/sizeof(tests[0]);
    for (int i = 0; i < n; i++) {
        printf("%s -> %s\n", tests[i], isCComment(tests[i]) ? "ACCEPT" : "REJECT");
    }

    // --- Interactive input ---
    printf("\n>> Try your own input!\n");
    char input[100];
    printf("Enter a string: ");
    scanf("%99s", input);

    if (isCComment(input)) {
        printf("Result: ACCEPT \n");
    } else {
        printf("Result: REJECT \n");
    }

    printf("\nProgram finished.\n");
    return 0;
}
