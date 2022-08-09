UPDATE fine,(
    SELECT name, number_plate, violation
    FROM fine
    GROUP BY  1, 2, 3
    HAVING COUNT(3)>1
    ORDER BY 1,2,3) AS new
SET sum_fine = IF(date_payment is NULL,sum_fine*2,sum_fine)
WHERE fine.name = new.name;