def simulate():
    print("internal fragmentation simulate")
    size=4096
    request=3000
    print(f"size: {size}, reqested: {request}")
    page_needed=1
    total_size=page_needed*size
    print(f"total size: {total_size}")
    wasted=total_size-request
    print(f"wasted: {wasted}")


if __name__ == "__main__":
    simulate()

    