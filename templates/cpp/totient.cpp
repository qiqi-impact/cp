const int MX = 100001;  
ll val[MX];

val[1] = 1;
for(int i = 2; i < MX; i++) {
    if(!val[i]) {
        val[i] = i - 1;
        for(int j = i << 1; j < MX; j += i) {
            val[j] = (j / i) % i ? (i - 1) * val[j / i] : i * val[j / i];
        }
    }
}