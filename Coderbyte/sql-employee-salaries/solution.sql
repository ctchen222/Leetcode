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
