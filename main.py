from collections import deque

def lru(page_reference_string, num_frames):
    # Initialize an empty dictionary to keep track of pages in the page table
    page_table = {}
    # Initialize a deque to represent the frames (circular buffer for LRU)
    frames = deque()
    # Initialize the count of page faults
    page_faults = 0

    # Iterate over each page in the reference string
    for step, page in enumerate(page_reference_string):
        # Check if the page is not in the page table (page fault)
        if page not in page_table:
            # If frames are full, evict the least recently used page (LRU)
            if len(frames) >= num_frames:
                evicted_page = frames.popleft()  # Remove the oldest page
                del page_table[evicted_page]  # Remove the evicted page from the page table
            # Add the current page to frames and page table
            frames.append(page)
            page_table[page] = step  # Record the step of the page insertion
            page_faults += 1  # Increment page fault count
            # Print the current step details
            print(f"Step {step + 1}: Page fault ({page}) - Page Table: {set(page_table.keys())}, Frames: {list(frames)}, Faults: {page_faults}")
        else:
            # If the page is already in frames (page hit)
            frames.remove(page)  # Remove the page from frames to update its recent use
            frames.append(page)  # Add the page to frames to mark it as most recently used
            page_table[page] = step  # Update the last used step for the page
            # Print the current step details
            print(f"Step {step + 1}: Page hit ({page}) - Page Table: {set(page_table.keys())}, Frames: {list(frames)}, Faults: {page_faults}")
    
    # Print the total number of page faults for LRU
    print(f"Total Page Faults: {page_faults}")

def optimal(page_reference_string, num_frames):
    # Initialize an empty dictionary to keep track of pages in the page table
    page_table = {}
    # Initialize a deque to represent the frames (circular buffer for Optimal)
    frames = deque()
    # Initialize the count of page faults
    page_faults = 0

    # Iterate over each page in the reference string
    for step, page in enumerate(page_reference_string):
        # Check if the page is not in the page table (page fault)
        if page not in page_table:
            # If frames are full, find the page that will be accessed furthest in the future (Optimal)
            if len(frames) >= num_frames:
                farthest_page = max(page_table, key=lambda x: page_table[x])  # Find the page with maximum future access time
                frames.remove(farthest_page)  # Evict the found page
                del page_table[farthest_page]  # Remove the evicted page from the page table
            # Add the current page to frames and page table
            frames.append(page)
            page_table[page] = step  # Record the step of the page insertion
            page_faults += 1  # Increment page fault count
            # Print the current step details
            print(f"Step {step + 1}: Page fault ({page}) - Page Table: {set(page_table.keys())}, Frames: {list(frames)}, Faults: {page_faults}")
        else:
            # If the page is already in frames (page hit)
            frames.remove(page)  # Remove the page from frames to update its recent use
            frames.append(page)  # Add the page to frames to mark it as most recently used
            page_table[page] = step  # Update the last used step for the page
            # Print the current step details
            print(f"Step {step + 1}: Page hit ({page}) - Page Table: {set(page_table.keys())}, Frames: {list(frames)}, Faults: {page_faults}")
    
    # Print the total number of page faults for Optimal
    print(f"Total Page Faults: {page_faults}")

def fifo(page_reference_string, num_frames):
    # Initialize an empty set to keep track of pages in the page table
    page_table = set()
    # Initialize a deque with a maximum length to represent the frames (FIFO)
    frames = deque(maxlen=num_frames)
    # Initialize the count of page faults
    page_faults = 0

    # Iterate over each page in the reference string
    for step, page in enumerate(page_reference_string):
        # Check if the page is not in the page table (page fault)
        if page not in page_table:
            # If frames are full, evict the oldest page (FIFO)
            if len(frames) >= num_frames:
                evicted_page = frames.popleft()  # Remove the oldest page
                page_table.remove(evicted_page)  # Remove the evicted page from the page table
            # Add the current page to frames and page table
            frames.append(page)
            page_table.add(page)
            page_faults += 1  # Increment page fault count
            # Print the current step details
            print(f"Step {step + 1}: Page fault ({page}) - Page Table: {page_table}, Frames: {list(frames)}, Faults: {page_faults}")
        else:
            # If the page is already in frames (page hit)
            # Print the current step details
            print(f"Step {step + 1}: Page hit ({page}) - Page Table: {page_table}, Frames: {list(frames)}, Faults: {page_faults}")
    
    # Print the total number of page faults for FIFO
    print(f"Total Page Faults: {page_faults}")

# Sample Input
page_reference_string = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
num_frames = 4

print("For LRU Algorithm:")
lru(page_reference_string, num_frames)

print("\nFor Optimal Algorithm:")
optimal(page_reference_string, num_frames)

print("\nFor FIFO Algorithm:")
fifo(page_reference_string, num_frames)
