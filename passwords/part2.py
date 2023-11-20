from hashlib import sha256
import itertools


# words = ["marmot"]
def crack():
    total_words = [line.strip().lower() for line in open("words.txt")]
    cracked = 0

    records = [line.strip().split(":")[:2] for line in open("part2.txt")]
    cracked_f = open("cracked2.txt", "a")
    total_hashes = 0

    for i in range(0, len(total_words)):
        prefix = total_words[i]
        # print(f"Cracking prefix {prefix}")
        wordsxwords = ["".join([prefix, word]) for word in total_words]

        word_to_hashes = {
            sha256(word.encode("utf-8")).hexdigest(): word for word in wordsxwords
        }
        total_hashes += len(word_to_hashes)

        # print("Done hashing words!")
        for username, password_hash in records:
            if password_hash in word_to_hashes:
                print(f"Cracked {username}'s password!")
                cracked_f.write(f"{username}:{word_to_hashes[password_hash]}\n")
                cracked += 1
        if cracked > 50:
            break

    print(f"Total hashes: {total_hashes}")

    cracked_f.close()


if __name__ == "__main__":
    crack()

"""
Total hashes: 1246892076
        Command being timed: "python3 part2.py"
        User time (seconds): 890.07
        System time (seconds): 0.42
        Percent of CPU this job got: 99%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 14:50.53
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 167064
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 500565
        Voluntary context switches: 169
        Involuntary context switches: 61
        Swaps: 0
        File system inputs: 472
        File system outputs: 8
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0
"""
