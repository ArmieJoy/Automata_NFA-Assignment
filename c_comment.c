#include <stdio.h>
#include <string.h>
#include <stdbool.h>

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
    const char *tests[] = {
        "/*a*/", "/**/", "/***/", "/*aaa*aaa*/", "/*a/a*/",   // Accepted
        "/**", "/**/a/*aa*/", "aaa/**/aa", "/*/", "/**a/", "//aaaa" // Rejected
    };

    int n = sizeof(tests)/sizeof(tests[0]);
    for (int i = 0; i < n; i++) {
        printf("%s -> %s\n", tests[i], isCComment(tests[i]) ? "ACCEPT" : "REJECT");
    }

    return 0;
}