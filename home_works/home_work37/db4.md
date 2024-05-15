2. Определить все товары, которые производятся в Беларуси (марка, код товара. страна)

SELECT Produce, ID, Country
FROM Ware
WHERE Country = 'Беларусь';

3. Удалите из таблицы все товары, которые произведены в Германии

DELETE FROM Ware
WHERE Country = 'Германия';

4. Замените страну-производителя Польшу на Россию (код, товар, страна, описание товара).

UPDATE Ware
SET Country = 'Россия'
WHERE Country = 'Польша';

5. Восстановите строки, удаленные в 3 пункте.

INSERT INTO Ware (ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM)
SELECT ID, Produce, Material, Color, Size, Country, ID_salespeople, Price, Count, REM
FROM BackupWare
WHERE Country = 'Германия';

6.  Выведите весь товар, который не черного цвета (продукт, цену, код продукта)

SELECT Produce, Price, ID
FROM Ware
WHERE NOT Color = 'ч';

7. Вставьте строку  NTC-117BK Micro Camera Case, нейлон, ч, 13,3x8,3x5,7, 2016, Беларусь, 1046

INSERT INTO Ware (Produce, Material, Color, Size, Country, ID_salespeople)
VALUES ('NTC-117BK Micro Camera Case', 'нейлон', 'ч', '13,3x8,3x5,7', 'Беларусь', 1046);

8. Вставьте строку POC-463BK	Compact Camera Case, полиэстер, ч, 11x7x4,5, остальные данные не определены.

INSERT INTO Ware (ID, Produce, Material, Color, Size)
VALUES (1236, 'POC-463BK Compact Camera Case', 'полиэстер', 'ч', '11x7x4,5');

9. Вывести весь товар, который поставляет продавец с кодом 2065 из России

SELECT *
FROM Ware
WHERE ID_salespeople=2065;

10. Вывести товар, цена за который находится в диапазоне от 200 до 345

SELECT Produce, Price
FROM Ware
WHERE Price BETWEEN 200 AND 345;

11. Определите все сумки из кожи с размером не менее 40х30х5

SELECT Produce, Material, Size
FROM Ware
WHERE Produce LIKE 'bag' 
AND Material = 'кожа'
AND Size >= '40x30x5';

12. Написать запрос, который выводит все сумки и коды их поставщиков, если товара меньше чем на 1200 руб.

SELECT Produce, ID_salespeople
FROM Ware
WHERE Produce LIKE 'сумка%' 
AND Price < 1200;

13. Написать запрос, который заменит код поставщика на 2000, если на складе хранится товара менее чем на 500 руб. По данному поставщику.

UPDATE Ware
SET ID_salespeople = 2000
WHERE Price < 500

14. Вывести все кожаные сумки, количество которых менее 5 шт. и общая сумма товара не превышает 450 руб

SELECT *
FROM Ware
WHERE Produce LIKE '%сумка%' 
AND Material = 'кожа'
AND Count < 5
AND (Price * Count) <= 450;

15. Напишите запрос, который выведет все нейлоновые сумки цена на которые не превышает 250 руб.

SELECT *
FROM Ware
WHERE Produce = 'Bag'
AND Material = 'нейлон'
AND Price <= 250;

16. Замените материал нейлон на брезент, если сумка стоит менее 200 руб.

UPDATE Ware
SET Material = 'брезент'
WHERE Produce LIKE '%сумка%' 
AND Material = 'нейлон'
AND Price <= 200;

17. Напишите запрос, который выводит все сумки, у которых есть косметички

UPDATE Ware
SET Material = 'брезент'
WHERE Produce LIKE 'Bag' 
AND Material = 'нейлон'
AND Price <= 200;

18. Напишите запрос, который покажет все кожаные сумки черного цвета китайского производства.

SELECT *
FROM Ware
WHERE Produce LIKE '%сумка%' 
AND Material = 'кожа'
AND Color = 'черный'
AND Country = 'Китай';

19. Напишите запрос, который покажет все сумки с размером более 15 дюймов.

SELECT *
FROM WARE
WHERE REM GLOB '*[1-9][5-9]*"*' OR REM GLOB '*[1-9][5-9]*''*'

20. Напишите запрос, который покажет всех поставщиков сумок не черного цвета.

SELECT DISTINCT ID_salespeople
FROM Ware
WHERE Produce LIKE '%сумка%' 
AND Color <> 'черный';

21. Замените материал полиэстер у сумок китайского производства на нейлон

UPDATE Ware
SET Material = 'нейлон'
WHERE Produce LIKE '%сумка%' 
AND Country = 'Китай'
AND Material = 'полиэстер';

22. В записях с кодом товара: 1015, 1041, 1032, 1010 материал нейлон заменить на полиэстер если страна-производитель Китай.

UPDATE Ware
SET Material = 'полиэстер'
WHERE ID IN (1015, 1041, 1032, 1010)
AND Country = 'Китай'
AND Material = 'нейлон';





















