# Tree Constructor

- 題目：[Coderbyte Tree Constructor](https://coderbyte.com/editor/Tree%20Constructor:Python3)
- 難度：Medium

## 題目

輸入是一組 `"(child,parent)"` 格式的字串：

```text
["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
```

每一組數字代表一條由 parent 指向 child 的關係。例如 `(1,2)` 代表：

```text
2
└── 1
```

判斷所有關係能否共同組成一棵合法的 Binary Tree，並回傳字串 `"true"` 或 `"false"`。

這題不是 Binary Search Tree，因此不需要比較節點值的大小；只需驗證樹的結構是否合法。

## 合法 Binary Tree 的條件

| 條件 | 不合法範例 | 原因 |
|---|---|---|
| 每個 child 最多只能有一個 parent | `(1,2)`、`(1,3)` | 節點 `1` 同時屬於兩個 parent |
| 每個 parent 最多只能有兩個 children | `(1,2)`、`(3,2)`、`(5,2)` | 節點 `2` 有三個 children |
| 整體恰好只有一個 root | `(1,2)`、`(3,4)` | 形成兩棵分離的樹 |
| 所有節點都能從 root 抵達 | `(2,1)`、`(3,4)`、`(4,3)` | `3`、`4` 形成與主樹分離的 cycle |

root 是唯一沒有 parent 的節點。

## 解法思路

讀取每一組 `(child, parent)` 時，利用 hash map 和 set 記錄四種資訊：

| 資料結構 | 內容 | 用途 |
|---|---|---|
| `parent_of` | `child -> parent` | 檢查 child 是否已經有 parent |
| `children_count` | `parent -> child 數量` | 檢查 parent 是否超過兩個 children |
| `children_of` | `parent -> [children]` | 從 root 走訪所有連接的節點 |
| `nodes` | 所有出現過的節點 | 找 root，並確認所有節點都被走訪 |

處理流程：

```text
解析每組 (child, parent)
        │
        ├─ child 已存在於 parent_of？ ── 是 ──> false
        │
        ├─ parent 的 children 超過 2？ ── 是 ──> false
        │
        ▼
找出不在 parent_of 中的節點
        │
        ├─ root 數量不是 1？ ── 是 ──> false
        │
        ▼
從唯一 root 走訪 children_of
        │
        ├─ 遇到重複節點？ ── 是 ──> false
        │
        ├─ visited 不等於 nodes？ ── 是 ──> false
        │
        ▼
       true
```

## 為什麼要記錄 `nodes`？

`parent_of` 只會保存「曾經當過 child 的節點」，並不包含純 root。

以 `(1,2)` 為例：

```python
parent_of = {1: 2}
```

只看 `parent_of` 的 key，只看得到節點 `1`，看不到 root `2`。因此需要把 child 與 parent 都加入 `nodes`：

```python
nodes = {1, 2}
```

再用集合差集的概念找 root：

```text
所有節點 - 曾經當過 child 的節點 = root 候選
{1, 2} - {1} = {2}
```

程式中的 list comprehension 等同於這個集合差集：

```python
roots = [node for node in nodes if node not in parent_of]
```

`nodes` 還有第二個用途：走訪完成後比較 `visited == nodes`，確認沒有節點藏在另一個不連通的子圖或 cycle 中。

嚴格來說，不一定非得維護一個名為 `nodes` 的 set；最後也可以用所有 child 與 parent 的聯集重建完整節點集合。但演算法仍然需要知道「全部有哪些節點」，直接在解析時記錄最清楚，而且每次 set 新增平均是 `O(1)`。

## 範例追蹤

輸入：

```text
["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
```

掃描完成後：

```python
parent_of = {
    1: 2,
    2: 4,
    5: 7,
    7: 2,
    9: 5,
}

children_count = {
    2: 2,
    4: 1,
    7: 1,
    5: 1,
}

nodes = {1, 2, 4, 5, 7, 9}
```

只有 `4` 沒有出現在 `parent_of` 的 key 中，因此 `4` 是唯一 root：

```text
4
└── 2
    ├── 1
    └── 7
        └── 5
            └── 9
```

從 `4` 可以走訪全部六個節點，所以這是一棵合法的 Binary Tree。

## 完整解法

```python
def TreeConstructor(strArr):
    parent_of = {}
    children_count = {}
    children_of = {}
    nodes = set()

    for pair in strArr:
        child, parent = map(int, pair.strip("()").split(","))
        nodes.add(child)
        nodes.add(parent)

        # 每個 child 最多只能有一個 parent。
        if child in parent_of:
            return "false"
        parent_of[child] = parent

        # 每個 parent 最多只能有兩個 children。
        children_count[parent] = children_count.get(parent, 0) + 1
        if children_count[parent] > 2:
            return "false"

        children_of.setdefault(parent, []).append(child)

    roots = [node for node in nodes if node not in parent_of]
    if len(roots) != 1:
        return "false"

    visited = set()
    stack = [roots[0]]

    while stack:
        node = stack.pop()
        if node in visited:
            return "false"

        visited.add(node)
        stack.extend(children_of.get(node, []))

    return "true" if visited == nodes else "false"
```

## 為什麼只檢查 root 數量仍然不夠？

目前 `main.py` 使用：

```python
if len(roots) > 1:
    return "false"
```

這只能拒絕多個 root，無法拒絕零個 root：

```text
(1,2)、(2,1)

1 ──parent──> 2
2 ──parent──> 1
```

兩個節點都曾經當過 child，所以 `roots` 是空的；若只檢查 `> 1`，程式會誤回 `"true"`。

即使改成 `len(roots) != 1`，仍可能出現「一棵正常樹加上一個分離 cycle」：

```text
(2,1)、(3,4)、(4,3)

1                     3 <──> 4
└── 2                  disconnected cycle
```

整體仍只有一個 root `1`，但從 `1` 無法抵達 `3`、`4`。因此完整解法還會從 root 走訪，最後確認 `visited == nodes`。

## 複雜度

令 `N` 為 `(child, parent)` 關係的數量，節點數量最多為 `2N`。

### 時間複雜度：`O(N)`

- 掃描所有關係一次：`O(N)`。
- 找 root：`O(N)`。
- DFS 走訪每個節點與連線一次：`O(N)`。

合計仍為 `O(N)`。

### 空間複雜度：`O(N)`

`parent_of`、`children_count`、`children_of`、`nodes`、`visited` 與 DFS stack 最多都保存與輸入規模成正比的資料。

## 優化方式

### 1. 掃描期間提早結束

發現 child 已經有 parent，或 parent 已經有第三個 child 時，立即回傳 `"false"`，避免繼續處理必定不合法的輸入。

### 2. 用 `children_of` 同時取代 `children_count`

既然完整驗證已經需要 parent-to-children adjacency，也可以直接檢查 list 長度：

```python
children_of.setdefault(parent, []).append(child)
if len(children_of[parent]) > 2:
    return "false"
```

這能少維護一個 dictionary，但將「計數」與「走訪」拆開會讓初學者更容易理解各自的責任；兩種寫法的時間與空間複雜度都仍是 `O(N)`。

### 3. 保留整數轉換，但它不是複雜度優化

這題只比較節點身份，因此保留字串也能判斷結構。使用 `map(int, ...)` 的優點是節點型別更符合題意，並避免 `"01"` 與 `"1"` 被當成不同節點；它不會改變 Big-O。

### 4. 不需要真的建立 TreeNode

題目只要求判斷能否形成 Binary Tree，不要求回傳或遍歷實際樹物件。hash map、set 與 adjacency list 已足以驗證所有條件，建立 `TreeNode` 只會增加程式與記憶體負擔。

### 5. DFS 與 BFS 都可以

走訪目的只是確認從 root 能否抵達全部節點，因此 stack DFS 或 queue BFS 都是 `O(N)`。這裡使用 stack 是因為 Python list 的 `append()`／`pop()` 即可完成，不需要額外匯入。
