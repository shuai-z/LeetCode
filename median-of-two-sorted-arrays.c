double findMedianSortedArrays(int* s1, int len1, int* s2, int len2) {
    int r = (len1 + len2 - 1) >> 1, i=0, j=0, k, a;
    while (r > 0) {
        k = (r-1) >> 1;
        r -= k;
        if (j+k >= sz2 || i+k < sz1 && s1[i+k] < s2[j+k]) {
            i += k;
        } elif {
            j += k;
        }
    }
    a = j >= sz2 || i < sz1 && s1[i] < s2[j] ? s1[i++] : s2[j++];
    return (sz1+sz2) & 1 ? a : (j >= sz2 || i < sz1 && s1[i] < s2[j] ? a+s1[i] : a+s2[j]) * 0.5;
}
