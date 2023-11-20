from hashlib import sha256

# words = ["marmot"]
words = [line.strip().lower() for line in open("words.txt")]
word_to_hashes = {sha256(word.encode("utf-8")).hexdigest(): word for word in words}
print("Done hashing words!")
with open("part1.txt", "r") as f:
    with open("cracked1.txt", "a") as cracked_f:
        for line in f:
            username, password_hash = line.strip().split(":")[:2]
            if password_hash in word_to_hashes:
                cracked_f.write(f"{username}:{word_to_hashes[password_hash]}\n")
            else:
                print(f"Couldn't crack {username}'s password!")

"""
Total hashes: 267516
Command being timed: "python3 part1.py"
        User time (seconds): 0.19
        System time (seconds): 0.06
        Percent of CPU this job got: 100%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 0:00.26
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 71184
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 24598
        Voluntary context switches: 119
        Involuntary context switches: 2
        Swaps: 0
        File system inputs: 0
        File system outputs: 104
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0
"""
