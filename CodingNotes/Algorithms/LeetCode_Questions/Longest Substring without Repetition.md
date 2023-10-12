A very naive solution is to check from beginning and move a pointer to a next character. However, this results in a N^M solution.

Let's say we are given a following string

abcdefcdet

Then, actually we don't have to start checking from 'b' again, since there is a violation in c already. so we just need to start from 'd'.