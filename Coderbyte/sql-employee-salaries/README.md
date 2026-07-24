# SQL Employee Salaries

## 題目

- 資料庫：MySQL 8.0.23
- 員工資料表：`maintable_20K03`
- 部門資料表：`cb_companydivisions`

找出薪資排序第三高的員工並回傳該筆資料，同時：

1. 以 `cb_companydivisions` 中對應的 `DivisionName` 取代 `DivisionID`。
2. 若 `ManagerID` 不為 `NULL`，且該 ID 存在於員工表中，便以該名員工的 `Name` 作為 `ManagerName`。

預期輸出：

| ID | Name | DivisionName | ManagerName | Salary |
|---:|---|---|---|---:|
| 222 | Mark Red | Sales | Susan Wall | 86000 |

## 解法

```sql
SELECT
    e.ID,
    e.Name,
    d.DivisionName,
    m.Name AS ManagerName,
    e.Salary
FROM maintable_20K03 e
LEFT JOIN cb_companydivisions d
    ON e.DivisionID = d.id
LEFT JOIN maintable_20K03 m
    ON e.ManagerID = m.ID
ORDER BY e.Salary DESC
LIMIT 1 OFFSET 2;
```

### 查詢流程

1. `maintable_20K03 e`：將員工表命名為 `e`，代表目前查詢的員工。
2. 第一個 `LEFT JOIN`：使用員工的 `DivisionID` 找到對應的 `DivisionName`。
3. 第二個 `LEFT JOIN`：再次讀取員工表並命名為 `m`，使用 `e.ManagerID = m.ID` 找到經理所屬的那一列。
4. `m.Name AS ManagerName`：取出經理那一列的 `Name`，並將輸出欄位命名為 `ManagerName`。
5. `ORDER BY e.Salary DESC`：依薪資由高至低排序。
6. `LIMIT 1 OFFSET 2`：跳過前兩列，再取一列，也就是排序後的第三列。

## 為什麼需要 self join？

員工和經理都存放在同一張 `maintable_20K03` 中。`ManagerID` 只是一個指向另一位員工 `ID` 的參照，因此必須讓同一張表扮演兩個角色：

| 別名 | 角色 | 需要的欄位 |
|---|---|---|
| `e` | 目前的員工 | `e.Name`、`e.ManagerID`、`e.Salary` |
| `m` | 該員工的經理 | `m.ID`、`m.Name` |

以預期結果為例：

```text
員工列 e                         經理列 m
ID = 222                         ID = 133
Name = Mark Red                  Name = Susan Wall
ManagerID = 133  ------------->  ID = 133
```

連接條件 `e.ManagerID = m.ID` 會把 Mark Red 的 `ManagerID` 133 對應到 Susan Wall 的員工列，之後才能取得 `m.Name`。

### 為什麼不能直接使用 `e.ManagerName`？

`e` 代表 Mark Red 自己的資料列，而原始員工表只有 `Name` 與 `ManagerID`，沒有 `ManagerName` 欄位。因此：

- `e.ManagerName`：欄位不存在，MySQL 會回報 `Unknown column`。
- `e.Name`：得到的是員工本人 `Mark Red`，不是經理。
- `m.Name AS ManagerName`：從經理的資料列取得 `Susan Wall`，再把輸出欄位命名為 `ManagerName`。

這種「同一張表中的一列參照另一列」的階層關係，就是 self join 的典型用途。

## 為什麼使用 `LEFT JOIN`？

題目提到 `ManagerID` 可能為 `NULL`，也可能找不到對應的員工 ID。使用 `LEFT JOIN` 仍會保留原本的員工列，只讓 `ManagerName` 顯示為 `NULL`；若使用 `INNER JOIN`，該員工列會直接從結果中消失。

## 薪資並列時的注意事項

目前的 `LIMIT 1 OFFSET 2` 取得的是薪資排序後的「第三列」。如果題目要求的是「第三個不同的薪資」，遇到同薪員工時便需要改用 `DENSE_RANK()` 等方式處理。
