import time


FILE_NAME = "leaked_email_addresses.txt"


class Timer:
     def __enter__(self):
         self.start_time = time.time()

     def __exit__(self, exc_type, exc_val, exc_tb):
         print(f"[i] Done in {round(time.time() - self.start_time, 3)} seconds")


def get_domain(email_address: str) -> str:
    domain = email_address.split("@")[-1]
    return domain


def main():
    result = dict()
    with open(FILE_NAME, "r") as in_file:
        for line in in_file:
            # Odstranenie noveho riadku na konci
            email_address = line.strip()
            domain = get_domain(email_address)
            result[domain] = result.get(domain, 0) + 1
    
    usporiadane_domeny = sorted(result.keys(), key=lambda x: result[x], reverse=True)

    print("[i] Usporiadane domeny:")
    for index, domena in enumerate(usporiadane_domeny):
        print(f"{index + 1}.\t{domena}\t{result[domena]}")


if __name__ == "__main__":
    with Timer():
        main()