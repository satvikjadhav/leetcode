# Basic Hashing

Hashing is used mainly to "pre store" something and then to also "fetch" something. 

## Time Complexity of a HashMap

Storing and Fetching in a sorted HashMap takes LogN time. This is the same in best, average, and worst case. 

Storing and Fetching in a unordered HashMap takes \(O(1)\) for best and average. The worst case, however, takes \(O(n)\). 

The worst-case time complexity for a hashmap (or hash table) can be \(O(n)\) because of potential **hash collisions**. Here’s a breakdown of why this happens:

1. **Hash Collisions**: In a hashmap, keys are hashed to generate an index that determines where the key-value pair is stored. Ideally, each key would have a unique index, but in reality, different keys can sometimes generate the same hash, causing a collision. When this happens, multiple entries end up being stored in the same "bucket" or linked list at that index.

2. **Chaining or Open Addressing**: To handle collisions, hashmaps often use one of two techniques:
   - **Chaining**: Each bucket holds a linked list (or another data structure) of all entries with the same hash. In the worst case, all keys could hash to the same index, making the hashmap a single linked list of \(n\) entries, with a lookup time of \(O(n)\).
   - **Open Addressing**: Instead of linking entries, the hashmap probes (searches) for the next available slot. If there are many collisions, probing can take \(O(n)\) time in the worst case.

3. **Poor Hash Function**: A poorly designed hash function could create many collisions by mapping many keys to the same index. This results in increased chain lengths (for chaining) or longer probe sequences (for open addressing).

## Division Method
The **division method** is a simple technique used to compute hash values in a hashmap by dividing the key's numeric value by the table size and taking the remainder. It’s a common way to map keys to indices in hash tables.

### Division Method Formula
Given a key \( k \) and a hash table size \( m \), the division method defines the hash function as:

\[
h(k) = k \mod m
\]

where:
- \( h(k) \) is the hash value or index in the table.
- \( k \) is the key (converted to a numeric form if necessary).
- \( m \) is the number of slots in the hash table.

This formula calculates the **remainder** when \( k \) is divided by \( m \), which will always be a value between \( 0 \) and \( m-1 \).

### Key Points and Considerations
- **Choosing \( m \):** \( m \) should ideally be a **prime number** not close to a power of 2, which helps distribute keys more evenly and reduce the chance of collisions.
- **Why it works well for hash tables:** Taking the modulus \( m \) helps ensure that hash values wrap around within the bounds of the table size, creating a compact index range.
- **Limitations:** If \( m \) is poorly chosen (e.g., an even number or a power of 2), the hash function may generate clusters or patterns in the hash values, which could increase collisions.

### Example
Suppose we have a hash table with \( m = 10 \) slots, and we want to hash a key \( k = 12345 \).

\[
h(k) = 12345 \mod 10 = 5
\]

So, key \( 12345 \) would be mapped to index \( 5 \) in the hash table.

### Benefits and Drawbacks
- **Pros:** Simple and efficient to compute.
- **Cons:** Can lead to poor distribution if \( m \) isn’t chosen carefully, causing clustering and increased collisions.

The division method is widely used because of its simplicity, but careful selection of \( m \) is important to ensure a good distribution of keys across the hash table.

## Linear Chaining

**Chaining** (also called **separate chaining**) is a collision resolution technique where each slot in the hash table contains a list (or another data structure, like a linked list) of all the entries that hash to that slot. This means if multiple keys hash to the same index, they’re all stored together in a list at that index, effectively forming a “chain” of values for that slot.

#### How Chaining Works:
1. **Hash Function**: First, a hash function determines the index for a key.
2. **Collision Resolution**: If the slot for that index already contains a key-value pair (a collision), the new key-value pair is added to the linked list (or chain) at that index.
3. **Search and Insert**: For retrieval or insertion, the algorithm:
   - Uses the hash function to find the index.
   - Searches through the chain at that index for the specific key or inserts it at the end if it’s not present.

#### Example:
Assume a hash table of size 5 and three keys with hash values that resolve to index 2:
- Insert key-value pair `(10, "A")`: Hash function maps `10` to index 2.
- Insert key-value pair `(15, "B")`: Hash function maps `15` to index 2. This goes into a chain at index 2.
- Insert key-value pair `(20, "C")`: Again maps to index 2, so it’s added to the chain at index 2.

Now, index 2 has a chain containing: `[(10, "A"), (15, "B"), (20, "C")]`.

#### Pros and Cons of Chaining
- **Pros**:
  - Easy to implement.
  - Chains can grow as needed, so the hash table doesn’t need resizing as often.
  - Generally provides good performance if chains remain short.
  
- **Cons**:
  - Memory overhead for storing chains, especially if there are many collisions.
  - Performance degrades if many keys hash to the same index, causing long chains and slower lookups.
