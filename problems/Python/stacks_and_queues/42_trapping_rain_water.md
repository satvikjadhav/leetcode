```python
def trap(height):
    if not height or len(height) < 3:  # Edge case: need at least 3 bars to trap water
        return 0
        
    total_water = 0
    stack = []  # Stack to store indices of bars
    
    # Process each bar in the elevation map
    for i in range(len(height)):
        # While we have a stack and current bar is higher than the bar at top of stack
        while stack and height[i] > height[stack[-1]]:
            # Pop the top of the stack - this is our "bottom" position
            bottom = stack.pop()
            
            # If stack becomes empty, no left boundary exists
            if not stack:
                break
                
            # Calculate water trapped above the bottom position
            left = stack[-1]        # Left boundary is the current top of stack
            right = i               # Right boundary is the current position
            width = right - left - 1  # Width is the distance between boundaries minus 1
            
            # The height of water is limited by the shorter of the two boundaries,
            # minus the height of the bottom position
            water_height = min(height[left], height[i]) - height[bottom]
            
            # Water trapped = width × height
            trapped_water = width * water_height
            total_water += trapped_water
            
        # Push current index onto the stack
        stack.append(i)
    
    return total_water

# Example usage
example1 = [0,1,0,2,1,0,1,3,2,1,2,1]
print(f"Example 1: {trap(example1)}")  # Output: 6

example2 = [4,2,0,3,2,5]
print(f"Example 2: {trap(example2)}")  # Output: 9
```


## 🧠 Problem Intuition

You’re given an array where each element represents the height of a bar in an elevation map. The goal is to **calculate how much water is trapped between the bars after it rains**.

Water can only be trapped **between two taller bars**, and the amount is limited by the **shorter of the two**.

---

## 🧱 Stack-Based Intuition

This solution uses a **monotonic stack** to track the indices of the bars in ascending height.

### Let's walk through it:

1. **Purpose of the Stack**:
   - It keeps track of **potential left boundaries** for trapping water.
   - As you move through the array, you're looking for **a right boundary** (a bar taller than the one at the top of the stack).
   - Once you find it, you've now sandwiched a "valley" between two tall walls, and can compute the trapped water.

---

### 🔁 Main Loop (For each index `i`):

```python
while stack and height[i] > height[stack[-1]]:
```

- This condition says: "While there's a valley (current bar is taller than the previous one), calculate trapped water."

#### 📌 Step-by-step:

1. **Pop the top of the stack** — this is the **bottom of the valley**.
2. If the stack is now empty, break — no left boundary.
3. Otherwise:
   - Left boundary = bar at `stack[-1]`
   - Right boundary = current bar at index `i`
   - Width = `right - left - 1` (how many bars between them)
   - Height of water = `min(height[left], height[right]) - height[bottom]`
   - Water trapped = `width * height`

### 🌊 Why `min(left, right)`?

Water can't go higher than the shortest wall. For example:
```
|       |
|   _   |
|__|_|__|
```
Even if the right side is super tall, the left wall limits the trapped water.

---

## 🧮 Example Walkthrough

For `[0,1,0,2,1,0,1,3,2,1,2,1]`:

You'd see valleys at positions like `height[2]` (0 between 1 and 2), or `height[5]` (0 between 2 and 3), etc.

Each time you find a right wall that's taller than the top of the stack, it means you've found a complete container (valley), and can compute water.

---

## ✅ Why This Works Well

- The algorithm is **O(n)** in time since each bar is pushed and popped at most once.
- It efficiently handles the core principle: “Water is trapped between taller bars.”

---

## Dry Run of The Algorithm

Great! Let’s walk through a **step-by-step dry run** of your code using the first example:

```python
height = [0,1,0,2,1,0,1,3,2,1,2,1]
```

We'll track the following:

- `stack` – holds indices of bars.
- `i` – current index.
- `total_water` – accumulated trapped water.

---

### 🔁 Iteration 0:
- `i = 0`, `height[0] = 0`
- Stack: `[]` → no bar to compare to, push index 0.
- Stack becomes: `[0]`

---

### 🔁 Iteration 1:
- `i = 1`, `height[1] = 1`
- `height[1] > height[stack[-1]]` → 1 > 0, so we **pop** `0`
- Stack is now empty → break, nothing to trap
- Push `1` → Stack becomes `[1]`

---

### 🔁 Iteration 2:
- `i = 2`, `height[2] = 0`
- 0 ≤ height[1], no trap yet
- Push `2` → Stack: `[1, 2]`

---

### 🔁 Iteration 3:
- `i = 3`, `height[3] = 2`
- 2 > 0 → pop `2`
  - Stack = `[1]` (not empty)
  - Bottom = 2, Left = 1, Right = 3
  - Width = 3 - 1 - 1 = 1
  - Height = min(1,2) - 0 = 1
  - Water = 1 × 1 = **1**
  - Total water: `1`

- 2 > height[1] = 1 → pop `1`
  - Stack = `[]` → break

- Push `3` → Stack: `[3]`

---

### 🔁 Iteration 4:
- `i = 4`, `height[4] = 1`
- 1 ≤ 2 → push `4`
- Stack: `[3, 4]`

---

### 🔁 Iteration 5:
- `i = 5`, `height[5] = 0`
- 0 ≤ 1 → push `5`
- Stack: `[3, 4, 5]`

---

### 🔁 Iteration 6:
- `i = 6`, `height[6] = 1`
- 1 > 0 → pop `5`
  - Bottom = 5, Left = 4, Right = 6
  - Width = 1
  - Height = min(1,1) - 0 = 1
  - Water = 1
  - Total = 2

- 1 == 1 → push `6`
- Stack: `[3, 4, 6]`

---

### 🔁 Iteration 7:
- `i = 7`, `height[7] = 3`
- 3 > 1 → pop `6`
  - Bottom = 6, Left = 4, Right = 7
  - Width = 2
  - Height = min(1,3) - 1 = 0 → **no water**

- 3 > 1 → pop `4`
  - Bottom = 4, Left = 3, Right = 7
  - Width = 3
  - Height = min(2,3) - 1 = 1
  - Water = 3
  - Total = 5

- 3 > 2 → pop `3` → Stack empty → break

- Push `7` → Stack: `[7]`

---

### 🔁 Iteration 8:
- `i = 8`, `height[8] = 2`
- 2 < 3 → push `8`
- Stack: `[7, 8]`

---

### 🔁 Iteration 9:
- `i = 9`, `height[9] = 1`
- 1 < 2 → push `9`
- Stack: `[7, 8, 9]`

---

### 🔁 Iteration 10:
- `i = 10`, `height[10] = 2`
- 2 > 1 → pop `9`
  - Bottom = 9, Left = 8, Right = 10
  - Width = 1
  - Height = min(2,2) - 1 = 1
  - Water = 1
  - Total = 6

- 2 == 2 → push `10`
- Stack: `[7, 8, 10]`

---

### 🔁 Iteration 11:
- `i = 11`, `height[11] = 1`
- 1 < 2 → push `11`
- Stack: `[7, 8, 10, 11]`

---

### ✅ Final Result:
- Total water trapped = **6**
