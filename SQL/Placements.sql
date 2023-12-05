SELECT temp1.sn
FROM (
    SELECT S.ID AS si, S.Name AS sn, P.Salary AS ps
    FROM Students S
    JOIN Packages P ON S.ID = P.ID
) temp1
JOIN (
    SELECT FF.ID AS fi, FF.Friend_ID AS fd, PP.Salary AS pps
    FROM Friends FF
    JOIN Packages PP ON FF.Friend_ID = PP.ID
) temp2 ON temp1.si = temp2.fi AND temp1.ps < temp2.pps
ORDER BY temp2.pps ASC;
