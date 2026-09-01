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

    // Inside body can be any combination of a, *, /
    return true;
}

int main() {
    const char *tests[] = {
        "/*a*/", "/**/", "/***/", "/*aaa*aaa*/", "/*a/a*/",   // Accepted
        "/**", "/**/a/**a*/", "/aaa/**/a/", "/*/", "/**a/", "/aaaa" // Rejected
    };

    int n = sizeof(tests)/sizeof(tests[0]);
    for (int i = 0; i < n; i++) {
        printf("%s -> %s\n", tests[i], isCComment(tests[i]) ? "ACCEPT" : "REJECT");
    }

    return 0;
}