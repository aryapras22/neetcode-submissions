impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut seen: HashMap<u8, usize> = HashMap::new();
        let mut start: usize = 0_usize;
        let mut longest: i32 = 0_i32;

        for (idx, ch) in s.bytes().enumerate() {
            if let Some(&value) = seen.get(&ch) {
                start = start.max(value + 1);
            }

            longest = longest.max((idx - start + 1) as i32);
            *seen.entry(ch)
                .and_modify(|val| *val = idx)
                .or_insert(idx);
        }

        longest
    }
}
