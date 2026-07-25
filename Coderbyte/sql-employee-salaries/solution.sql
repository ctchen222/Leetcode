-- Solution I
-- SELECT
--    e.ID,
--    e.Name,
--   d.DivisionName,
--   m.Name AS ManagerName,
--  e.Salary
--FROM maintable_20K03 e
--LEFT JOIN cb_companydivisions d
--   ON e.DivisionID = d.id
--LEFT JOIN maintable_20K03 m
--    ON e.ManagerID = m.ID
--ORDER BY e.Salary DESC
--LIMIT 1 OFFSET 2;

-- Solution II
WITH target_employee AS (
    SELECT
        ID,
        Name,
        DivisionID,
        ManagerID,
        Salary
    FROM maintable_20K03
    ORDER BY Salary DESC, ID ASC
    LIMIT 1 OFFSET 2
  )
  SELECT
      e.ID,
      e.Name,
      d.DivisionName,
      m.Name AS ManagerName,
      e.Salary
  FROM target_employee e
  LEFT JOIN cb_companydivisions d
      ON d.ID = e.DivisionID
  LEFT JOIN maintable_20K03 m
      ON m.ID = e.ManagerID;

-- Solution III
WITH ranked AS (
  SELECT
    e.ID,
    e.Name,
    e.DivisionID,
    e.ManagerID,
    e.Salary,
    DENSE_RANK() OVER (ORDER BY e.Salary DESC) AS dr
  FROM maintable_20K03 e
)
SELECT
  r.ID,
  r.Name,
  d.DivisionName,
  m.Name AS ManagerName,
  r.Salary
FROM ranked r
LEFT JOIN cb_companydivisions d ON r.DivisionID = d.id
LEFT JOIN maintable_20K03 m ON r.ManagerID = m.ID
WHERE r.dr = 3;
