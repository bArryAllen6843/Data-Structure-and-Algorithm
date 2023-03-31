import collections


class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        # tasks = ["A","A","A","B","B","B"]
        # n = 2

        counts = list(collections.Counter(tasks).values())  # [3,3]
        max_count = max(counts)  # 3
        number_of_chars_with_max_count = counts.count(max_count)  # 2, A and B

        number_of_chunks_with_idles = max_count - 1  # 2 -> A  A  A

        # either a task will fill an empty place or the place stays idle,
        # either way the chunk size stays the same
        length_of_a_chunk_with_idle = n + 1  # 3 -> A _ _ A _ _ A

        # on the final chunk, there will only be most frequent letters
        length_of_final_chunk = number_of_chars_with_max_count  # 2

        # 2*3 + 2 = 8
        length_of_all_chunks = (number_of_chunks_with_idles * length_of_a_chunk_with_idle) + length_of_final_chunk

        # -> A B _ A B _ A B

        return max(len(tasks), length_of_all_chunks)


if __name__ == '__main__':
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    a = Solution()
    print(a.leastInterval(tasks, n))
