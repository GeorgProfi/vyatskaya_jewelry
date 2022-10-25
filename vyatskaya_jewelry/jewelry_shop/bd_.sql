--
-- Файл сгенерирован с помощью SQLiteStudio v3.3.3 в Ср окт 19 12:00:33 2022
--
-- Использованная кодировка текста: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Таблица: chapter_table
CREATE TABLE chapter_table (chapter VARCHAR (50) PRIMARY KEY NOT NULL, sum INTEGER (50));
INSERT INTO chapter_table (chapter, sum) VALUES ('брошь', 20);
INSERT INTO chapter_table (chapter, sum) VALUES ('медальён', 3);
INSERT INTO chapter_table (chapter, sum) VALUES ('браслет', 5);
INSERT INTO chapter_table (chapter, sum) VALUES ('подвеска', 10);
INSERT INTO chapter_table (chapter, sum) VALUES ('кольцо', 10);

-- Таблица: collection
CREATE TABLE collection (type VARCHAR (50) PRIMARY KEY NOT NULL, metal VARCHAR (50), gems VARCHAR (50), mass DOUBLE (50), "price " INTEGER (50), volume_product INTEGER (50), chapter VARCHAR (50) REFERENCES chapter_table (chapter), photo STRING (200), id NUMERIC REFERENCES gallary (id));
INSERT INTO collection (type, metal, gems, mass, "price ", volume_product, chapter, photo, id) VALUES ('Брелок "Фрактал серпинского"', 'латунь', 'нет', 7.0, 1000, 5, 'медальён', '3A.jpg', NULL);
INSERT INTO collection (type, metal, gems, mass, "price ", volume_product, chapter, photo, id) VALUES ('Кольцо "#НетПутиНазад"', 'латунь', 'нет', 15.0, 2000, 2, 'кольцо', 'notRoudBehind.jpg', NULL);
INSERT INTO collection (type, metal, gems, mass, "price ", volume_product, chapter, photo, id) VALUES ('Кольцо "Маленькая любовь"', 'серебро', 'нет', 7.0, 4000, 4, 'кольцо', 'love_old.jpg', NULL);
INSERT INTO collection (type, metal, gems, mass, "price ", volume_product, chapter, photo, id) VALUES ('Кольцо "Любовное"', 'серебро', 'нет', 12.0, 6000, 7, 'кольцо', 'love.jpg', NULL);

-- Таблица: gallary
CREATE TABLE gallary (id INT (11) NOT NULL PRIMARY KEY, title CHAR (200) NOT NULL, img VARCHAR (200) NOT NULL);
INSERT INTO gallary (id, title, img) VALUES (4, 'Брелок "Фрактал серпинского"', '3A.jpg');
INSERT INTO gallary (id, title, img) VALUES (3, 'Кольцо "#НетПутиНазад"', 'notRoudBehind.jpg');
INSERT INTO gallary (id, title, img) VALUES (2, 'Кольцо "Маленькая любовь"', 'love_old.jpg');
INSERT INTO gallary (id, title, img) VALUES (1, 'Кольцо "Любовное" ', 'love.jpg');
INSERT INTO gallary (id, title, img) VALUES (5, 'sofi', 'sofi.png');

-- Таблица: method_delivery_table
CREATE TABLE method_delivery_table (method_delivery VARCHAR (50) PRIMARY KEY NOT NULL, price_delivery INTEGER (10));
INSERT INTO method_delivery_table (method_delivery, price_delivery) VALUES ('транспортная компания', 700);
INSERT INTO method_delivery_table (method_delivery, price_delivery) VALUES ('курьер', 1000);
INSERT INTO method_delivery_table (method_delivery, price_delivery) VALUES ('почта', 300);

-- Таблица: order
CREATE TABLE "order" (order_id NUMERIC PRIMARY KEY, method_delivery VARCHAR (50) REFERENCES method_delivery_table (method_delivery), product VARCHAR (50) REFERENCES collection (type), price_order INTEGER (50), address VARCHAR (100));

-- Таблица: user
CREATE TABLE user (user_id NUMERIC (10) PRIMARY KEY, login VARCHAR (20), order_id NUMERIC REFERENCES "order" (order_id));
INSERT INTO user (user_id, login, order_id) VALUES (1, 'abmin', NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
