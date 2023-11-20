from hashlib import sha256


# words = ["marmot"]
def crack():
    words = [line.strip().lower() for line in open("words.txt")]
    cracked = 0

    records = [line.strip().split(":")[:2] for line in open("part3.txt")]
    cracked_f = open("cracked3.txt", "a")
    total_hashes = 0

    # print("Done hashing words!")
    for username, password_suite in records:
        _, salt, password_hash = password_suite.strip("$").split("$")
        word_to_hashes = {
            sha256((salt + word).encode("utf-8")).hexdigest(): word for word in words
        }
        total_hashes += len(word_to_hashes)
        if password_hash in word_to_hashes:
            print(f"Cracked {username}'s password!")
            cracked_f.write(f"{username}:{word_to_hashes[password_hash]}\n")
            cracked += 1

    print(f"Total hashes: {total_hashes}")

    cracked_f.close()


if __name__ == "__main__":
    crack()

"""
Total hashes: 731388744
        Command being timed: "python3 part3.py"
        User time (seconds): 476.61
        System time (seconds): 0.46
        Percent of CPU this job got: 99%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 7:57.09
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 121088
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 0
        Minor (reclaiming a frame) page faults: 294613
        Voluntary context switches: 150
        Involuntary context switches: 85
        Swaps: 0
        File system inputs: 0
        File system outputs: 144
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0
"""
