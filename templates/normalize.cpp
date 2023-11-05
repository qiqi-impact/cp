void compress_fast(vector<int> &a) {
	vector<int> values(a.begin(), a.end());
	sort(values.begin(), values.end());
	values.erase(unique(values.begin(), values.end()), values.end());
	for(int &x : a) x = lower_bound(values.begin(), values.end(), x) - values.begin();
}